# Project Status

## Purpose

This file is the dynamic project-status entry point for Lithos Mind.

It helps future ChatGPT, Codex, or other AI collaborators quickly understand:

* The current project state.
* Which stages have been completed.
* What should happen next.
* What must remain out of scope.
* Which documents contain detailed context.

This file should stay concise. It should not duplicate the full content of README, data documentation, V0 planning documents, or stage closeout records.

---

## Project Snapshot

**Project name:** Lithos Mind

Lithos Mind is a personal public-data knowledge base Agent project.

It is built around public-safe personal learning notes, cultural collections, reading records, and long-term interest data.

The project is a long-term AI product management portfolio project. It should be developed through small, reviewable stages with clear scope boundaries.

For general project background and positioning, see:

* [`README.md`](README.md)

---

## Current Stage Status

Current stage model:

```text
Stage 1: Project Initialization
Stage 2: Minimal YAML Extraction Prototype
Stage 3: Structured Record and Query Boundary Definition
```

Current status:

| Stage   | Name                                            | Status            | Notes                                                                              |
| ------- | ----------------------------------------------- | ----------------- | ---------------------------------------------------------------------------------- |
| Stage 1 | Project Initialization                          | Closed            | Repository foundation and initial project boundaries completed.                    |
| Stage 2 | Minimal YAML Extraction Prototype               | Closed            | Single-file YAML frontmatter extraction completed. Markdown body remains excluded. |
| Stage 3 | Structured Record and Query Boundary Definition | Open (definition) | Complete text-first card record and controlled query boundary; no implementation.   |

The project is currently in the Stage 3 definition stage.

---

## Documentation Map

Use these documents for detailed context:

* [`README.md`](README.md): concise project background, positioning, and boundaries.
* [`AGENTS.md`](AGENTS.md): stable Codex repository execution guidance.
* [`data/README.md`](data/README.md): data rules, Stage 2 YAML-only boundary, and future text-first record direction.
* [`docs-dev/v0/scope.md`](docs-dev/v0/scope.md): future V0 scope boundary.
* [`docs-dev/v0/stage-1-project-initialization.md`](docs-dev/v0/stage-1-project-initialization.md): Stage 1 closeout record.
* [`docs-dev/v0/stage-2-yaml-extraction.md`](docs-dev/v0/stage-2-yaml-extraction.md): Stage 2 YAML extraction prototype, extraction boundary, and manual verification.
* [`docs-dev/v0/stage-3-structured-record-query-boundary.md`](docs-dev/v0/stage-3-structured-record-query-boundary.md): Stage 3 text-first card record and controlled query boundary.

---

## Completed Work Summary

### Stage 1: Project Initialization

Stage 1 is closed.

It established:

* Repository foundation.
* Project positioning.
* Future V0 boundary.
* Public-safe data policy.
* Lithos YAML-only data source boundary.
* Initial sample data template.
* Stage 1 closeout checklist.

Detailed record:

* [`docs-dev/v0/stage-1-project-initialization.md`](docs-dev/v0/stage-1-project-initialization.md)

### Stage 2: Minimal YAML Extraction Prototype

Stage 2 is closed.

It established:

* A minimal local YAML frontmatter extractor.
* A public-safe sample Lithos Markdown card.
* A minimal Python dependency declaration.
* A documented extraction boundary.
* Manual verification guidance.
* Stage 2 closeout documentation.

Detailed record:

* [`docs-dev/v0/stage-2-yaml-extraction.md`](docs-dev/v0/stage-2-yaml-extraction.md)

---

## Current Working State

The repository currently has:

* A concise project README.
* Stable Codex execution guidance.
* A dynamic project status file.
* Consolidated data documentation under `data/README.md`.
* V0 development-stage documents under `docs-dev/v0/`.
* A minimal YAML frontmatter extraction prototype.
* Public-safe sample and template files.

The Stage 2 extractor currently supports only one explicitly provided local Markdown file.

It extracts YAML frontmatter only and excludes Markdown body content.

For full data and extraction boundaries, see:

* [`data/README.md`](data/README.md)
* [`docs-dev/v0/stage-2-yaml-extraction.md`](docs-dev/v0/stage-2-yaml-extraction.md)

---

## Next Recommended Step

Review and finalize the Stage 3 documentation before implementation begins.

The review should confirm the complete text-first record model, body-text preservation, source-hash behavior, image exclusion, and controlled query boundary.

---

## Explicitly Out of Scope Now

The project should not currently add:

* Batch import.
* Full Lithos repository scanning.
* Data cleaning pipeline.
* Metadata normalization implementation.
* Schema validation.
* Required YAML fields.
* Database implementation.
* Query implementation.
* Markdown body parsing or record preparation implementation.
* Embedding.
* Vector database.
* RAG.
* Agent answer generation.
* Frontend.
* Backend.
* API.
* Deployment.
* Private or sensitive data processing.

These may become relevant in later stages, but they are not part of the current state.

---

## Recent Decisions

Recent project decisions:

* README should remain a concise project background and positioning document, not a detailed status log.
* Data-related documentation has been consolidated into `data/README.md`.
* V0 planning and development-stage documents are organized under `docs-dev/v0/`.
* `AGENTS.md` defines stable Codex execution rules.
* `PROJECT_STATUS.md` should act as a lightweight project status index and AI handoff document.
* Detailed V0, data, and stage-specific information should remain in the dedicated documents listed above.
* Structured database-style querying is prioritized before vector retrieval for selected metadata and short card notes.
* Vector retrieval may be considered later if larger unstructured text or semantic-search needs are introduced.
* Original `.md` cards remain the source of truth; derived Agent records should use a complete text-first model rather than a minimal query-only model.
* Future records may include selected Agent-facing YAML fields, `body_text` that preserves body content as-is without YAML frontmatter, and `raw_yaml_json` for complete metadata preservation.
* `source_hash` should be generated by future import logic for change detection, not manually added to source cards.
* Full `raw_markdown` storage is not currently recommended.
* Image references such as `cover` are not Agent-facing fields and may only remain passively preserved in `raw_yaml_json`.
* Stage 3 documentation must be reviewed and finalized before implementation begins.

---

## Update Protocol

Update this file after each meaningful project round.

Update it when:

* A stage is opened or closed.
* A major artifact is created.
* A task is completed.
* The next recommended step changes.
* An important scope decision is made.
* A previously planned direction is revised.
* The documentation structure changes.

Keep updates concise.

Do not turn this file into a detailed changelog.

Do not duplicate full content from README, `data/README.md`, or `docs-dev/v0/`.

When project context is needed in a new AI-assisted round, use this file as the first status reference.
