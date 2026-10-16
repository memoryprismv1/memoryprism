# Repository Setup Notes

This page records the intended GitHub repository metadata and the remaining UI-only setup steps. It is an operational note, not part of the Memory Prism framework.

## GitHub About

**Suggested description**

> A structural framework for understanding how systems form, persist, and fail under constraint. Includes the framework PDF, a portable starter checklist, documentation, and a platform-neutral AI skill.

**Website**

https://www.memoryprism.com/

**Suggested topics**

memory-prism, systems-thinking, systems-analysis, complex-systems, constraints, cross-disciplinary, research-methodology, ai-skill

These describe the repository without claiming it is a predictive model or an established scientific discipline.

## License

The official website identifies Memory Prism v1.0 as **CC BY-NC 4.0** and lists the DOI below. The repository's [LICENSE.md](../LICENSE.md) records that declaration and scopes it to original project content, unless a file says otherwise.

- License: https://creativecommons.org/licenses/by-nc/4.0/
- Official license page: https://www.memoryprism.com/license
- DOI listed by official site: https://doi.org/10.5281/zenodo.19287268

The connected GitHub tool can edit tracked files but cannot change the repository's About metadata, set topics, or write to the separate GitHub Wiki store. Those settings must be entered through GitHub's web UI.

## Set About and topics manually

Open the repository's main page and use the gear icon in the About panel.

1. Set the description to the text above.
2. Set the website URL to https://www.memoryprism.com/.
3. Add the eight topics above.
4. Save.

## Publish the GitHub Wiki

The Wiki page seeds are in [wiki-seed/](../wiki-seed/). The repository's Wiki feature is enabled, but GitHub treats the Wiki as a separate store from ordinary repository files.

1. Open the repository's **Wiki** tab.
2. If prompted, select **Create the first page**.
3. Open wiki-seed/Home.md, copy its contents into the Wiki page titled Home, then save.
4. Create these additional Wiki pages using the matching seed files: Framework, Starter-Kit, Seven-Lenses, Using-Memory-Prism, and FAQ.
5. Check the page links, because Wiki links use page names rather than repository-relative paths.

Source files in wiki-seed/ remain version-controlled in the main repository; copying them to GitHub Wiki creates the published view. They are intentionally separated so the project can use the Wiki without losing reviewable source history.

## Source links

See [SOURCES.md](../SOURCES.md) for the framework DOI, official page, seven essay URLs, and related project references.
