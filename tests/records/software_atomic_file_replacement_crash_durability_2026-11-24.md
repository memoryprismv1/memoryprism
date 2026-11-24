# Software Daily Test: Crash-Safe Atomic Replacement of a Configuration File — 2026-11-24

**Test ID:** MP-SOFTWARE-2026-11-24-01  
**Date:** 2026-11-24  
**Type:** Assistant-directed software inquiry; documentation-grounded failure analysis  
**Status:** Closed as a standards/documentation-informed design analysis. No code was executed and no filesystem crash test was performed.

## Starting question

An application updates a configuration file while the service is running. It writes a new version to a temporary file and renames that file over the old one. Readers never observe a half-written configuration during normal operation. Is that enough to guarantee that the new configuration survives a sudden power loss?

## Operating invariant

At all times, a reader opening the configuration path should see either the complete old version or the complete new version—never a partially written mixture. After the update reports durable success, a machine crash and reboot should not silently lose the update or leave the configuration path missing.

These are two distinct guarantees:

- **Atomic visibility:** concurrent readers do not observe an intermediate pathname replacement.
- **Crash durability:** the intended file contents and directory entry survive a crash.

## Selective Memory Prism inventory

| MP concept | Mapping to the subject |
|---|---|
| P-Memory | The persisted file and its directory entry carry the configuration state across process and machine restarts |
| Board | Filesystem, kernel, storage device, mount options, application processes and concurrent readers |
| Constraints | Write ordering, filesystem semantics, same-filesystem rename requirement, storage flush behaviour, permissions and crash timing |
| Editors | Writes, fsync, rename, directory fsync, recovery and concurrent writers |
| Ledger | Temporary and final storage space, write/flush latency, I/O budget, and the cost of retaining old and new versions during replacement |
| Architecture | Temporary-file creation, complete write, file sync, rename and parent-directory sync |
| Stability | The old-or-new visibility invariant and post-crash persistence of the acknowledged version |

## System behaviour and evidence

### 1. Rename can be atomic without being durable

On Linux, rename() replaces an existing destination atomically with respect to pathname lookup: another process attempting to access the destination does not see a moment when the destination is absent. Open file descriptors already referring to the old file remain attached to that old file; a new open by pathname can see the replacement.

That is an atomic namespace operation. It does not, by itself, promise that the rename has reached persistent storage.

### 2. File fsync and directory fsync protect different state

The Linux fsync(2) manual says that fsync() flushes modified file data and associated metadata. It also explicitly warns that syncing the file does not necessarily sync the directory entry containing it. To ensure that directory entry reaches storage, the application must separately fsync() a file descriptor for the directory.

The distinction matters because rename changes the parent directory: it removes one name and installs another. Syncing the temporary file does not automatically make that namespace change durable.

The Linux kernel's OverlayFS documentation reinforces the general warning: without explicit syncing, after a crash there is no guarantee that the observed state will be the old or new data; it may even be a mixture. Filesystem-specific behaviour and guarantees matter.

### 3. A safer Linux replacement sequence

For a file and temporary file in the same directory/filesystem, the usual crash-conscious sequence is:

1. Create a uniquely named temporary file in the target directory.
2. Write the complete new contents, handling partial writes and errors.
3. Apply required ownership, permissions and other metadata to the temporary file.
4. Call fsync() on the temporary file and check the result.
5. Close the temporary file and check relevant errors.
6. Rename the temporary file over the target path.
7. Open and fsync() the parent directory; check the result.
8. Only then report durable success to the caller.

The rename supplies atomic visibility. The file sync protects the new file's data and metadata. The directory sync protects the name-to-file relationship.

This is a Linux-oriented pattern, not a claim that identical details apply to every operating system, filesystem, network mount or storage device.

## Failure-window analysis

| Failure point | Expected concern / recovery question |
|---|---|
| Before temporary file is complete | Old target should remain untouched; incomplete temporary file may need cleanup |
| After writing but before file fsync succeeds | New content may not be durable; do not claim success |
| After file fsync, before rename | New temporary file is durable, but target still names old version |
| After rename, before directory fsync | New version may be visible to running readers, but the rename's crash persistence is not yet established |
| After successful directory fsync | The application can report the replacement as durably committed, subject to the filesystem/device honouring the sync contract |
| Any fsync or close error | Treat the outcome as uncertain or failed; do not silently report success |

A crash after rename but before directory sync is the critical trap: normal runtime tests may pass while power-loss recovery exposes the missing durability step.

## Additional design hazards

- **Same filesystem:** rename across mount points can fail with EXDEV; create the temporary file in the destination directory to avoid this class of failure.
- **Concurrent writers:** atomic rename does not serialize application-level updates. Two writers can each prepare a valid replacement and the later rename can overwrite the earlier one. Use a lock, version check or compare-and-swap design if lost updates matter.
- **Readers holding old descriptors:** a process that already opened the old file can continue reading the old inode after replacement. Atomic pathname replacement does not force all readers to switch simultaneously.
- **Metadata preservation:** replacement creates a new file object. Ownership, mode, ACLs, extended attributes, labels and other required metadata may need explicit handling before the rename.
- **Temporary-file safety:** use secure, unique creation rather than a predictable shared temporary name; clean up abandoned temporary files without deleting another writer's work.
- **Storage and filesystem semantics:** network filesystems, overlay filesystems, mount options, hardware write caches and platform differences can change the guarantees. Verify the actual deployment environment.

## Main finding

“Write temporary file, then rename” solves the partial-read problem, but it is not a complete crash-durability protocol. The parent directory is part of the persistent state. On Linux, a robust replacement normally requires syncing the new file before rename and syncing the parent directory after rename.

The important distinction is not simply file contents versus no file contents. It is the separate persistence of the file object and the directory entry that makes the object reachable by its expected name.

## Verification plan that would be required for implementation

A real implementation test should inject process termination and machine-level crash/power-loss conditions at each failure window, then inspect the recovered directory and file contents after reboot. It should also test concurrent writers, readers holding old descriptors, disk-full and I/O errors, permission/metadata preservation, and the actual target filesystem/mount configuration.

Killing only the application process is not equivalent to simulating loss of power: the kernel page cache and storage stack remain active and may flush pending writes.

## Limits

- This is a documentation-grounded Linux design analysis, not a live filesystem or power-failure test.
- The exact durability guarantee depends on filesystem, mount configuration, storage stack and device behaviour.
- The sequence is not a universal cross-platform recipe; platform-specific replacement and durability APIs may differ.
- No application code, test harness, filesystem image or storage hardware was supplied or executed.

## Sources

- Linux man-pages, fsync(2): https://www.man7.org/linux/man-pages/man2/fdatasync.2.html
- Linux man-pages, rename(2): https://man7.org/linux/man-pages/man2/rename.2.html
- Linux kernel documentation, OverlayFS — durability and copy up: https://www.kernel.org/doc/html/latest/filesystems/overlayfs.html
- Linux Kernel Internals, “fsync() after rename() is not enough — losing files after a crash”: https://kernel-internals.org/io/war-stories/

## Provenance and evaluation boundary

Assistant-selected and assistant-directed software inquiry. This is a documentation-grounded analysis of atomic visibility versus crash durability on Linux. No live filesystem, application code, crash-recovery test or production system was exercised. The MP inventory organises the system's persistent state, constraints, write/rename/sync operations and resource costs; it is not evidence of a new filesystem mechanism.


## Score sheet

**Run type:** standards-grounded scenario  **Conditions:** MP-guided  **Context:** same-context  **Scorer:** self  **Blind:** no  **Execution:** standards/docs

| Dim | MP-guided | Note |
|---|---:|---|
| IQ1 Engages the question | 2 | Directly tests whether atomic rename is sufficient for crash durability |
| IQ2 Mechanism and evidence | 2 | Correctly distinguishes file sync, rename and directory sync using Linux documentation |
| IQ3 Evidence boundaries | 2 | States platform/filesystem limits and that no crash test was run |
| IQ4 Competing explanations | 1 | Identifies filesystem/device variation but does not compare multiple filesystem-specific recovery models in depth |
| IQ5 Next question or action | 2 | Gives a concrete failure-injection plan covering each commit window |
| IQ6 Clarity and economy | 2 | Organises the protocol by guarantees and failure windows |
| **IQ total** | **11/12** | |
| MPF1 Inventory first and concrete | 2 | Inventory precedes system interpretation |
| MPF2 Proportionate selection | 2 | Selected concepts map to actual file and namespace state |
| MPF3 Concept fidelity | 2 | Ledger, flow and accumulation are not collapsed; resource cost is grounded |
| MPF4 No unsupported mechanism | 2 | No unsupported sensing, audit or governance claim |
| MPF5 Source use | 2 | Linux manual and kernel documentation ground the technical interpretation |
| MPF6 Reasoning audit used | 2 | Audit separated namespace atomicity from persistence durability and exposed the missing directory sync |
| **MPF total** | **12/12** | |

**Integrity flags:** F1 No · F2 No · F3 No · F4 No · F5 No · F6 No  
**Difference claimed?** No demonstrated difference; single assistant-generated condition.

SCORES: IQ_mp=11/12; MPF=12/12; scorer=self; blind=no
