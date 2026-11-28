# Software Daily Test: Incremental Build Correctness and Stale Outputs — 2026-11-28

**Test ID:** MP-SOFTWARE-2026-11-28-01  
**Run type:** Assistant-generated synthesis  
**Conditions:** single MP-guided documentation analysis; no baseline comparison  
**Context:** same-context · **Scorer:** self · **Blind:** no · **Execution:** standards/docs; no live build  
**Question:** Why can changing one small source file trigger a huge rebuild in a software project — or, more dangerously, why can a build system sometimes fail to rebuild something that actually needed updating?

## Scenario and operating invariant

An incremental build system should reuse work only when the inputs and conditions that determine an output have not changed. The operating invariant is:

**An incremental build must produce the same correct outputs as a clean build for the same declared source state and build environment.**

The system faces two opposing risks:
- Missing or incomplete dependencies can leave stale outputs that should have been rebuilt.
- Excessive or imprecise dependencies can invalidate too much work and cause unnecessary rebuilding.

A third risk exists in action caching: a build may reuse a result produced under a materially different tool or environment if the cache identity does not represent those differences.

## Selective pre-interpretation inventory

| MP concept | What I identify in this query |
|---|---|
| Architecture | Source files, generated files, build actions, dependency graph, outputs, local state and remote caches. |
| Constraints | Declared dependencies, compiler behaviour, build rules, execution environment, available resources and determinism requirements. |
| Board | The selected build target and its reachable dependency graph, together with the machine/toolchain context in which actions run. |
| P-Memory | Previously computed dependency information, build logs, cached action results and generated artifacts. |
| Editors (candidate) | Change detection, invalidation and cache-key rules determine which previous results remain reusable. |
| Ledger | Rebuilding consumes CPU, memory, disk and time; caching saves repeated computation but uses storage and validation resources. |
| Flow Under Constraint | Changes propagate through dependency edges toward affected outputs. |
| Stability | Incremental results must remain equivalent to clean-build results after changes. |

## System mechanisms and evidence

### Dependency graphs and invalidation

A build graph represents which outputs depend on which inputs. If a shared header changes, all outputs that depend on it may need rebuilding; if one source file changes, unrelated targets should remain reusable.

Bazel's Skyframe documentation describes invalidating the reverse transitive closure of changed inputs. It also describes change pruning: if an invalidated node is recomputed and its value is unchanged, dependent nodes can be treated as valid again. This is one way to avoid cascading work after a change that does not affect an output, such as a comment-only source edit. [1]

### Ninja and discovered dependencies

Ninja uses dependency information from build rules and compiler-generated dependency files. For C/C++, compilers can emit Makefile-style dependency information (depfiles) listing headers included by a source file. Ninja can ingest that information into its dependency database, allowing later changes to those headers to trigger the relevant rebuilds. [2]

Ninja also documents the `restat` mechanism: after an action runs, it re-stats outputs; if an output's modification time did not change, some reverse dependencies can be removed from the pending build. This can prevent downstream work when an action ran but did not materially change its output. [2]

The tool also provides `missingdeps` to find targets that depend on generated files without a proper dependency path to the generator. The manual notes that such problems can cause build flakiness on clean builds. [2]

### Failure: undeclared input

Suppose a build script reads `version.txt`, but its rule declares only `source.c` as an input. Changing `version.txt` may not invalidate the generated output because the dependency graph does not contain that edge.

Bazel's Skyframe documentation warns that reading data without registering a dependency can lead to incorrect incremental builds. It explains that well-behaved functions request inputs through dependencies so the graph captures the data flow. [1]

This is a stale-output failure: the build system reuses a result even though an actual input to the computation changed.

### Failure: incomplete action identity and remote cache reuse

Bazel's remote-caching documentation describes cases where actions can depend on environment variables and tools outside the workspace. If relevant environmental differences are not represented in the action definition, machines with different environments or compilers can incorrectly share cache hits. The documented example is a compiler from `/usr/bin/` that Bazel does not track, allowing different compiler outputs to share an action hash. [3]

This is not simply a dependency-graph invalidation issue. It is an action-identity/cache-key problem: the build system considers two computations equivalent when their actual execution conditions differ.

### Failure: over-declared dependency

If a rule declares inputs that do not actually affect its output, changes to those inputs can trigger unnecessary rebuilds. This is a performance failure rather than a stale-output correctness failure. The correct dependency graph should include all real inputs, but not arbitrary unrelated files.

## Diagnostic comparison

| Failure mode | Observable symptom | Discriminating check |
|---|---|---|
| Missing dependency edge | Incremental output remains stale after an input changes | Compare incremental output with a clean build after changing only the suspected input. |
| Over-declared dependency | Unrelated changes trigger rebuilds | Inspect the graph and determine whether the changed input can affect the action's output. |
| Incomplete action/cache identity | Different toolchains or environments reuse a cache result | Repeat with cache disabled or distinct toolchain identities and compare outputs. |
| Unstable/generated dependency discovery | Clean and incremental builds behave differently or intermittently fail | Inspect depfiles/dependency database and build from an empty output directory. |

## Diagnostic experiment

A small reproducible project can expose the missing-dependency failure:

1. Create a source file and a generator that also reads a configuration file.
2. Deliberately omit the configuration file from the declared build inputs.
3. Build once, change only the configuration file, then run an incremental build.
4. Compare the generated output with a clean build from the same source state.
5. Add the missing dependency edge and repeat.
6. Change the compiler or relevant environment and check whether action identity invalidates or partitions the cache correctly.

The key comparison is incremental output versus clean-build output, not merely whether the build command exits successfully. This experiment was proposed, not executed in this run.

## Findings and limits

Incremental build correctness depends on a complete representation of the inputs that determine each output. Performance comes from reusing previous work; correctness depends on refusing to reuse it when a real input or execution condition has changed.

The graph and cache solve different parts of the problem. Dependency tracking determines what is affected; action identity determines whether an equivalent operation has already been performed and can be reused. Missing dependencies and incomplete cache keys can therefore produce stale outputs through different mechanisms.

The investigation is documentation-grounded. No Ninja or Bazel project was built; no clean-versus-incremental comparison, cache poisoning test or toolchain-switch test was run. The cited Bazel remote-cache page is a versioned documentation snapshot, so its specific caveats should be checked against the deployed Bazel release.

## Sources

1. Bazel, “Skyframe”: dependency registration, reverse transitive closure invalidation, change pruning and incorrect incremental results from unregistered reads: https://bazel.build/reference/skyframe
2. Ninja, “The Ninja build system manual”: depfiles, dependency database, `restat` and `missingdeps`: https://ninja-build.org/manual.html
3. Bazel, “Remote Caching” documentation: environment variables, tools outside the workspace and cache-hit correctness: https://bazel.build/remote/caching

## Score sheet

**Run type:** assistant-generated synthesis **Conditions:** single MP-guided documentation analysis **Context:** same-context **Scorer:** self **Blind:** no **Execution:** standards/docs

| Dim | MP-guided | Note (failure mode for any 0/1) |
|---|---:|---|
| IQ1 Engages the question | 2 | Directly addresses both excessive rebuilding and stale outputs. |
| IQ2 Mechanism and evidence | 2 | Separates graph invalidation, discovered dependencies and action-cache identity with documentation support. |
| IQ3 Evidence boundaries | 2 | Clearly states no build or cache experiment was run. |
| IQ4 Competing explanations | 2 | Missing edges, excessive edges, incomplete action identity and unstable dependency discovery have distinct symptoms and checks. |
| IQ5 Next question or action | 2 | Gives a concrete incremental-versus-clean diagnostic sequence. |
| IQ6 Clarity and economy | 1 | The answer is clear but carries several build-system mechanisms and examples for a single question. |
| **IQ total** | **11/12** | |

| MPF dimension | Score | Note |
|---|---:|---|
| MPF1 Inventory first and concrete | 2 | Inventory precedes interpretation and identifies concrete build-system elements. |
| MPF2 Proportionate selection | 2 | Uses relevant core concepts and lenses without forcing the full set. |
| MPF3 Concept fidelity | 1 | Ledger is present but resource accounting is only briefly stated, not quantified as inputs and minimum maintenance payments. |
| MPF4 No unsupported mechanism | 2 | Invalidation and cache mechanisms are tied to build-system documentation. |
| MPF5 Source use | 2 | Framework checklist consulted; Bazel and Ninja claims linked to their documentation. |
| MPF6 Reasoning audit actually used | 1 | The final explanation distinguishes graph invalidation from cache identity, but no further material correction is visible in the delivered answer. |
| **MPF total** | **10/12** | |

**Integrity flags:** F1 No · F2 No · F3 No · F4 No · F5 No · F6 No.  
**Difference claimed?** No comparison condition was run.

**SCORES:** IQ_mp=11/12; MPF=10/12; scorer=self; blind=no

## Repository provenance

**Protocol retrieval (UTC):** 2026-11-28T08:40:42Z  
**Current main commit:** `436bef7071a93f083480c62ba9383902a19d05fb`

| File | Git blob SHA | SHA-256 |
|---|---|---|
| `tests/daily/README.md` | `04d295a20c67ff0774d89711c07a475616bf503e` | `d69d5220b45d68920d3cc9e1778dc1e0ff17d022dddcadac7ebb3770b09a8e74` |
| `tests/daily/SCORING.md` | `0b4f359fdeefdcdc55d55b94a94e8c8d801280a3` | `7f5045b4a3912ed1e951a79e6ac0b8b977fb70804074787d6454ab79d9bc9c79` |
| `tests/records/DEVELOPMENT_LOG.md` | `b46268bca9422f8156b5e84359b2a705f5abe392` | `62732e82c6e49046963ffd3eb7510a04f68de3c41b34a61d3def296f1f25b88a` |
