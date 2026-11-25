# Software Daily Test: Linux Multi-Gen LRU and Memory Reclaim Under Pressure — 2026-11-25

**Test ID:** MP-SOFTWARE-2026-11-25-01  
**Date:** 2026-11-25  
**Type:** Assistant-directed software inquiry; documentation-grounded system analysis  
**Status:** Closed as an upstream Linux design analysis. No kernel was built, configured, benchmarked or instrumented.

## Starting question

When physical memory is under pressure, how does the Linux kernel decide which pages to reclaim without simply throwing out whichever page was used least recently? How does it avoid evicting something that will immediately be needed again?

## Operating invariant

The kernel must reclaim enough memory to satisfy allocation pressure while trying to preserve pages whose reuse is valuable. A poor choice can cause refaults, repeated I/O or page faults, CPU overhead and visible application stalls. The reclaim policy is therefore a trade-off between memory availability, the cost of tracking use, and the cost of evicting a page that will soon be needed again.

This record focuses on upstream Linux Multi-Gen LRU (MGLRU), not every Linux reclaim path or every distribution's configuration.

## Selective Memory Prism inventory

| MP concept | Mapping to the subject |
|---|---|
| P-Memory | Resident page contents and their current placement in memory persist across successive workload operations until reclaimed or changed |
| Board | Physical memory, NUMA nodes, memory cgroups, processes/address spaces, page tables, file descriptors, swap and storage |
| Constraints | Finite RAM, page type, dirty/writeback state, mapping state, swap availability, memory-cgroup boundaries, CPU cost of scanning and fault cost |
| Editors | Accesses update recency evidence; aging changes generation placement; eviction reclaims selected old pages; refault feedback changes protection/selection |
| Ledger | RAM capacity, swap/storage bandwidth, page-table and reverse-map scan CPU, TLB flushes, writeback, major/minor fault cost and reclaim latency |
| Flow | Page accesses through page tables or file descriptors; reclaim and refault movement between resident memory and backing storage |
| Accumulation Patterns | Repeated access and refault history build evidence about a working set; page generations and tiers aggregate this history |
| Architecture / Stability | Generational lists, tiers, page-table walks, reverse mapping, Bloom filters and feedback control form the reclaim architecture; stability is the ability to relieve pressure without sustained thrashing |

## System behaviour and evidence

### 1. Why simple least-recently-used is not enough

A page's last observed access is useful but incomplete evidence. Access patterns differ: a page repeatedly accessed through a mapped address space can have a different fault penalty and tracking uncertainty from a page accessed through a file descriptor. A clean unmapped file page can be cheap to reclaim; a dirty page may require writeback; reclaiming a mapped page can require TLB work and may cause a major fault later.

The kernel therefore has to consider more than a single global timestamp or a simple list position. The Linux MGLRU documentation explicitly describes access channels, recency, spatial locality, fast paths and self-correcting heuristics as design concerns.

### 2. Aging: build a time-relative picture of recency

MGLRU divides evictable pages into multiple generations within an `lruvec`. Generations group pages with similar access recency. The youngest and oldest generation sequence numbers define a sliding window; generations are not simply fixed wall-clock age buckets.

Aging finds pages that have been accessed through page tables and promotes them to a younger generation. It uses page-table walks and reverse-map (rmap) walks to find young page-table entries. When it finds one, it clears the accessed bit and updates the page's generation. As the generation window advances, pages not promoted become relatively older.

The kernel also exploits spatial locality: when a young page-table entry is found, nearby entries may be scanned. Bloom filters help identify page-table ranges worth revisiting, reducing unnecessary work in suitable cases.

### 3. Eviction: choose among old pages, not blindly among all pages

Eviction consumes the oldest generations. It considers anonymous and file-backed pages separately because clean file pages can be reclaimed without swap constraints that apply to anonymous memory. When the candidate types are similarly old, MGLRU compares refault percentages in their first tiers. A high refault rate indicates that pages previously selected for eviction are being needed again; the policy can then protect or choose among tiers differently.

A page accessed multiple times through file descriptors is assigned a tier based on access count. The feedback mechanism can promote a tier when refaults show that evicting it was a poor choice. This is a correction based on observed consequences, not a guarantee that every page's future value can be predicted.

### 4. Refaults provide evidence that the selection was wrong

A refault occurs when a page that was evicted is needed again and must be brought back. MGLRU's feedback loop monitors refault percentages across anonymous and file-backed pages and across tiers. The documentation describes a controller modelled after a PID controller. It uses generation sequence rather than wall-clock time for its moving averages, because reclaim scan rates vary with memory pressure.

This matters because the policy is not only trying to estimate which pages are cold. It also checks whether its own eviction choices are producing avoidable returns. That is the self-correcting part of the design.

### 5. Working-set protection has a hard resource consequence

MGLRU offers an optional minimum-generation-age protection setting, `lru_gen_min_ttl` (exposed through the admin interface as `min_ttl_ms` in documented configurations). It can protect a recent working set from eviction for a specified time window. But if that protected working set cannot fit in memory, the OOM killer is triggered.

This is not free protection. It trades reclaim flexibility for a stronger attempt to avoid thrashing. The kernel documentation explicitly frames the option as a pressure-relief choice with an OOM risk when memory cannot hold the protected set.

### 6. What could distinguish a good reclaim decision from a bad one?

Two different workload explanations can produce high refaults:

- **The workload's working set genuinely shifted.** Pages that were cold at eviction time became hot after a phase change. This predicts refaults concentrated around the transition and then a new stable access pattern.
- **The reclaim policy under-protected a repeatedly useful class of pages.** This predicts persistently elevated refaults for a particular page type or tier even after the workload settles.

A useful diagnostic run would record per-generation eviction and refault behaviour, anonymous/file split, tier-level refault rates, major faults, writeback, reclaim CPU and application latency across both a steady workload and a deliberate phase-change workload. The distinction is whether the spike is transient and follows a changed workload, or persistent and concentrated in a class the policy keeps evicting.

## Main finding

Linux MGLRU is not a simple “evict the oldest page” queue. It builds a relative recency picture using generations, gathers access evidence through page tables and reverse mappings, chooses among old anonymous/file-backed pages and tiers, and uses refaults as feedback to adjust future choices. Its policy is an ongoing compromise between reclaiming memory, protecting likely working sets, and paying the CPU/I/O/fault costs of tracking and replacing pages.

The most important distinction is between **aging** (collecting and updating evidence about recency) and **eviction** (acting on the older generations). Refault feedback connects the two without making them the same operation.

## Limits

- This describes upstream Linux MGLRU as documented; it is not a universal description of all Linux reclaim implementations or configurations.
- Kernel versions and configuration affect availability and implementation details. A distribution may ship a kernel with MGLRU disabled or with different defaults.
- The documentation describes design and algorithms, not performance for a particular workload or device.
- No kernel build, runtime configuration check, trace, benchmark, memory-pressure experiment or OOM test was run.
- The two workload explanations above are diagnostic hypotheses, not findings from an executed workload.

## Sources

- Linux kernel documentation, “Multi-Gen LRU,” current documentation: https://docs.kernel.org/mm/multigen_lru.html
- Linux kernel documentation, “Multi-Gen LRU” admin guide (configuration and runtime controls): https://docs.kernel.org/admin-guide/mm/multigen_lru.html
- Linux kernel source, `mm/workingset.c`, for refault/workingset implementation: https://github.com/torvalds/linux/blob/master/mm/workingset.c

## Provenance and evaluation boundary

Assistant-selected and assistant-directed software topic. This is an upstream documentation/source-grounded design analysis. No code was executed, no kernel version was inspected on a live machine, and no performance or correctness claim was experimentally measured. The MP inventory organises the documented memory state, constraints, resource costs and feedback paths; it is not evidence that MP discovered the kernel algorithm.

## Score sheet

**Run type:** standards-grounded scenario  **Conditions:** MP-guided  **Context:** same-context  **Scorer:** self  **Blind:** no  **Execution:** standards/docs

| Dim | MP-guided | Note |
|---|---:|---|
| IQ1 Engages the question | 2 | Directly explains how MGLRU selects and corrects reclaim choices |
| IQ2 Mechanism and evidence | 2 | Describes generations, aging, eviction, tiers and refault feedback from upstream docs |
| IQ3 Evidence boundaries | 2 | Scope, configuration caveats and absence of live execution are explicit |
| IQ4 Competing explanations | 2 | Distinguishes workload phase shift from persistent class-specific under-protection and gives predictions |
| IQ5 Next question or action | 2 | Specifies metrics and workloads that would distinguish the explanations |
| IQ6 Clarity and economy | 2 | Separates aging, eviction and feedback rather than collapsing them |
| **IQ total** | **12/12** | Self-scored; not independent |

| Dim | MP-guided | Note |
|---|---:|---|
| MPF1 Inventory first and concrete | 2 | Concrete inventory precedes system interpretation |
| MPF2 Proportionate selection | 2 | Uses relevant concepts without forcing unrelated lenses |
| MPF3 Concept fidelity | 2 | Ledger, Flow and Accumulation remain distinct; constraints and editors remain distinct |
| MPF4 No unsupported mechanism | 2 | Refault feedback is tied to documented implementation, not anthropomorphised |
| MPF5 Source use | 2 | Framework, concept map and checklist consulted; domain claims grounded in kernel docs/source |
| MPF6 Reasoning audit used | 2 | Audit corrected a possible wall-clock-age simplification: generations are sequence-based and pressure-dependent |

**Integrity flags:** F1 No · F2 No · F3 No · F4 No · F5 No · F6 No  
**Difference claimed?** No demonstrated difference; single assistant-generated condition.

SCORES: IQ_mp=12/12; MPF=12/12; scorer=self; blind=no
