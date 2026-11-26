# Software Daily Test: Certificate Renewed, Old Certificate Still Served — 2026-11-25

**Test ID:** MP-SOFTWARE-2026-11-25-02
**Run type:** Live implementation (toy reproduction) plus documentation-grounded scenario
**Conditions:** conventional baseline vs MP-guided
**Context:** same-context · **Scorer:** self · **Blind:** no · **Execution:** live run (a Python TLS server, not nginx) plus standards/docs

## Scenario and operating invariant

A team's certbot renewal job logs success every time, yet users hit expired-certificate errors. Why, and how do we stop it recurring?

**Invariant:** every network path that terminates TLS for the hostname presents a certificate that is valid now and has at least N days remaining.

## Condition A — Conventional baseline

The usual cause: nginx loads certificates when it reads its config, so renewed files on disk aren't used until nginx reloads. With `certbot certonly` you need `--deploy-hook "systemctl reload nginx"`. Also check other servers or load balancers, and add expiry monitoring.

## Condition B — MP-guided

### Selective inventory

| MP concept | What I identify in this query |
|---|---|
| P-Memory | The certificate held in the running server's memory: the residue of the last config load, which outlives changes to the files on disk |
| Constraints | The certificate's `notAfter` (clients refuse after it); the server reads cert files only at config load; CA lifetimes and rate limits |
| Translator | TLS clients, which extract `notAfter`/chain from the presented cert and refuse it. Also the monitoring probe: it translates whatever it reads, disk or handshake, and those are different structures |
| Viability band / correction window | Time from first renewal attempt to expiry. Let's Encrypt renews at about two-thirds of lifetime, roughly 30 days on 90-day certs, and this shrinks as lifetimes fall |
| Lag | The stale in-memory cert works perfectly until `notAfter`, so the failure is masked for weeks |
| Working Lines | The deploy path (hook → config test → reload) that carries the new cert is the same path where a failure leaves the old one in place |

Left out: Editors, Identity, Accumulation.

### System states kept distinct

issued by CA → written to `/etc/letsencrypt/live/…` → **loaded by the serving process** → served on **every** path (each node, LB listener, CDN, container) → accepted by clients.

"Renewal succeeded" only certifies the first two.

### Evidence

- [Fact, docs] nginx `HUP`/reload starts new workers with the new config and gracefully shuts down old ones. Old workers keep serving their existing connections until done.
- [Fact, community/maintainer answers] The most common cause is that nginx isn't reloaded after renewal. `--nginx` handles it, otherwise use `--deploy-hook`. With `certonly`, certbot reports "New certificate deployed without reload" and doesn't know what the hook does.
- [Fact, secondary] A failing deploy hook is reported but doesn't make certbot exit nonzero. Monitor deployment as its own outcome and compare the served leaf fingerprint from fresh handshakes on every path. *(Checked via oneuptime's write-up, which cites certbot docs. I did not open the certbot docs page itself.)*
- [Fact] Let's Encrypt is moving to 64-day certificates on 10 Feb 2027 and 45-day on 16 Feb 2028. A hardcoded 60-day renewal interval won't be enough. CA/B Forum SC-081 caps public certs at 47 days by March 2029.

### Live reproduction (toy)

`assets/2026-11-25_tls_reload_demo/tls_reload_demo.py`: a Python `ssl` server that loads its cert once, like nginx at config load. Probes compare the disk fingerprint with the served fingerprint from a fresh handshake.

```
1 start (old cert loaded)              disk=5020bda5… served=5020bda5… match=True
2 renewal wrote new files, no reload   disk=4f530eb4… served=5020bda5… match=False
  -> reload ok
3 after reload                         disk=4f530eb4… served=4f530eb4… match=True
  -> reload FAILED (SSLError); old context kept
4 bad files + failed reload            disk=5020bda5… served=4f530eb4… match=False
```

- Step 2 reproduces the incident: files renewed, old cert served.
- Step 4 shows the reverse. A failed reload keeps the *old good* context, while the disk now holds a broken pair. A disk-reading probe would raise a false alarm here, and in step 2 it would show a false all-clear.
- So the probe must read the handshake, not the disk.

*This is a toy. It models the load-at-start behaviour, not nginx's worker draining, multi-node topologies or certbot itself.*

### Competing explanations for a real incident, and what separates them

| Explanation | Distinguishing evidence |
|---|---|
| No reload after renewal | Master/worker start time earlier than the renewal time; no "Running deploy-hook" in `letsencrypt.log` |
| Reload attempted but failed (config error) | Hook ran; `nginx -t` error or reload failure in logs; workers unchanged |
| Another termination point wasn't updated (second node, LB, CDN, container with a copied cert) | Served fingerprint differs by IP/path; the host itself serves the new cert |
| Renewal itself failed and the success was misread | `notAfter` of the file on disk is still old |
| Chain/intermediate problem, not expiry | Client error is "unknown issuer," not "expired" |

### Recommended fix, ordered

1. Use a deploy hook that runs `nginx -t && systemctl reload nginx` and fails loudly.
2. Add a served-certificate check: after each renewal, and continuously, compare the renewed leaf's SHA-256 against a fresh handshake on every IP and listener. Alert on mismatch, or on less than about a third of lifetime remaining.
3. Before Feb 2027, check that renewal timing is lifetime-relative (or uses ARI), not a fixed 60 days.

## Comparison

The baseline gets the main cause and the main fix. MP-guided added:
- the issued/written/loaded/served state chain;
- the finding that disk-based monitoring is the wrong translator, which can both hide and invent failures (demonstrated live in steps 2 and 4);
- a table of explanations with separating evidence;
- the shrinking correction window from shorter lifetimes.

The live run, not MP, supplied the strongest evidence. MP's contribution was pointing at *what* to measure: served state, not stored state.

## Limits

Toy Python server, not nginx. No multi-node, LB or CDN test. Certbot behaviour taken from community answers and a secondary write-up, not from the certbot docs. The baseline is contaminated (written after reading MP). Self-scored, unblinded.

## Score sheet

**Run type:** live implementation (toy) + standards/docs **Conditions:** baseline, MP-guided **Context:** same-context **Scorer:** self **Blind:** no **Execution:** live run + docs

| Dim | Baseline | MP-guided | Note (failure mode for any 0/1) |
|---|---:|---:|---|
| IQ1 Engages the question | 2 | 2 | |
| IQ2 Mechanism and evidence | 1 | 1 | Baseline unsourced. MP: certbot hook-exit claim via a secondary source (F1) |
| IQ3 Evidence boundaries | 1 | 2 | Toy vs nginx stated; docs vs community labelled |
| IQ4 Competing explanations | 1 | 2 | Baseline names "other servers" but no separating evidence |
| IQ5 Next question or action | 1 | 2 | Baseline fix is right but "add expiry monitoring" would miss the disk-vs-served gap |
| IQ6 Clarity and economy | 2 | 1 | MP version much longer |
| **IQ total** | **8/12** | **10/12** | |
| MPF1 Inventory first and concrete | n/a | 2 | |
| MPF2 Proportionate selection | n/a | 2 | |
| MPF3 Concept fidelity | n/a | 1 | Ledger not used, although retry budget and CA rate limits bear on the correction window; folded into the viability row instead |
| MPF4 No unsupported mechanism | n/a | 2 | No editor or audit asserted. The proposed served-cert check is *what would create* an audit |
| MPF5 Source use | n/a | n/a | |
| MPF6 Reasoning audit actually used | n/a | 2 | Audit flagged the unverified certbot claim and the toy-vs-nginx boundary |
| **MPF total** | n/a | **9/10** | |

**Integrity flags:** F1 Yes (certbot hook-exit-status claim checked only via a secondary article; IQ2 ≤ 1 applied). F2–F6 No.

**Reading:** 2-point IQ difference, below the 3-point threshold, so **no demonstrated difference**. Qualitatively, MP's state-distinction framing led directly to the disk-vs-handshake probe, which the live run then confirmed.

## Sources
- nginx, *Controlling nginx* (signals: HUP reload, graceful worker shutdown)
- Let's Encrypt community: "Certificate renewed, old one is used"; "Why does certbot not reload if it does run the deploy hook?"; "Certificate is renewed but connection shows as not secure till you restart nginx"
- OneUptime, *Alert When Let's Encrypt Renews but a Service Uses the Old Certificate* (2026-08-26)
- Let's Encrypt, *Decreasing Certificate Lifetimes to 45 Days* (2025-12-02) and *Upcoming Features*
- The Register, *New SSL/TLS certs to each live no longer than 47 days by 2029* (2025-04-14)

## Score line

SCORES: IQ_baseline=8/12; IQ_mp=10/12; MPF=9/10; scorer=self; blind=no