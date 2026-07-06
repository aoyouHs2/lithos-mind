# Project Status

## Purpose of This Document

This document is the dynamic project-status entry point for Lithos Mind.

It is written for future ChatGPT, Codex, or other AI collaborators to quickly understand:

* What Lithos Mind is.
* What the project is trying to become.
* What has already been completed.
* What the current stage is.
* What should happen next.
* What must remain out of scope for now.

This file should be updated after each meaningful project round. It should stay concise and should not become a detailed changelog.

---

## Project Snapshot

**Project name:** Lithos Mind

Lithos Mind is a personal public-data knowledge base Agent project.

It is designed to manage, retrieve, and understand public-safe personal data, including:

* Personal learning notes.
* Cultural collections.
* Reading records.
* Long-term interest data.
* Public personal knowledge accumulation.

The core idea is not to help the user complete daily tasks. The core idea is to help the system understand the user's long-term public knowledge data.

Lithos Mind is not:

* A work assistant.
* A PRD Agent.
* A todo tool.
* A schedule manager.
* A private message processor.
* An email assistant.
* A finance assistant.
* A medical assistant.
* A credential manager.
* A generic chatbot.

More precisely, Lithos Mind is a long-term AI product management portfolio project built around public-safe personal data, structured retrieval, source citation, and eventually Agent-based answers.

---

## Long-Term Direction

The long-term belief behind Lithos Mind is that each person may gradually build a personal database from their long-term public data.

Learning notes, reading records, cultural collections, reflections, and interest traces can become the foundation for a personal knowledge base Agent.

The value of a personal Agent does not only depend on the model. It also depends on:

* The quality of personal data.
* The amount of accumulated data.
* The structure of the data.
* Whether the data can be retrieved.
* Whether the data can be understood and cited.
* Whether the data can grow over time.

Lithos Mind is therefore not a one-time demo. It is a staged, reviewable, and evolving AI product management portfolio project.

---

## V0 Direction

V0 is a future public demo, not the current implementation stage.

The future V0 may aim to connect this minimum loop:

```text
public-safe data import
→ data cleaning
→ storage
→ retrieval
→ Agent answer
→ source citation
→ frontend interaction
→ public deployment
```

A successful V0 should eventually allow a viewer to:

* Understand what Lithos Mind is.
* Browse selected public-safe personal data.
* Ask questions about the user's public knowledge base.
* Receive answers grounded in retrieved data.
* See source citations below answers.
* Review the project through a clear README, documentation, and public demo.

The current project is not yet at the V0 implementation stage.

---

## Data Source Boundary

Current and possible future data sources include:

### Lithos

Lithos may serve as a public-safe cultural collection data source.

It may include public-safe metadata about:

* Anime.
* Books.
* Manga.
* Visual works.
* Cultural collections.
* Other long-term interest records.

Lithos is treated as a structured or semi-structured source suitable for demonstrating the user's cultural interests and collection system.

### Obsidian or Other Personal Notes

Obsidian or other Markdown-based notes may later serve as public-safe learning note sources.

Only selected public-safe notes should be used. The project must not directly import a full private vault.

### Image Boundary

Images may be included later as display assets or metadata.

Allowed future image-related uses may include:

* Covers.
* Posters.
* Work images.
* Image titles.
* Image tags.
* Image descriptions.
* Personal public-safe comments.

The project should not assume the following in the current or near-term scope:

* OCR.
* Image content understanding.
* Image vector search.
* Multimodal Agent reasoning.
* Direct question answering based on image content.

For now, the Agent direction remains primarily text-based.

### Disallowed Data

Lithos Mind is limited to public-safe personal data.

The project must not process or commit:

* Private messages.
* Emails.
* Financial records.
* Medical records.
* Account credentials.
* Passwords.
* Private schedules.
* Sensitive personal data.
* Any data that should not be publicly reviewed on GitHub.

---

## Candidate Technical Direction

The possible future V0 technical direction may include:

```text
GitHub
+ Next.js
+ Supabase / pgvector
+ DeepSeek API
+ embedding model
+ Vercel deployment
```

Possible responsibilities:

| Module          | Possible Role                           |
| --------------- | --------------------------------------- |
| GitHub          | Version control and portfolio display   |
| Next.js         | Frontend and basic API layer            |
| Supabase        | Database storage                        |
| pgvector        | Vector retrieval                        |
| DeepSeek API    | Agent answer generation                 |
| Embedding model | Convert text into vectors for retrieval |
| Vercel          | Public deployment                       |

This is a candidate future direction, not the current implementation scope.

DeepSeek may be used later as the answer-generation model. Embeddings do not have to use DeepSeek and may use a dedicated embedding model.

---

## Current Stage

Current stage model:

```text
Stage 1: Project Initialization
Stage 2: Minimal YAML Extraction Prototype
Stage 3: To be defined
```

Current status:

```text
Stage 1: Closed
Stage 2: Closed
Stage 3: Not started
```

Stage 3 should be defined separately before implementation begins.

---

## Stage Progress

| Stage   | Name                              | Status      | Notes                                                                                                                 |
| ------- | --------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------- |
| Stage 1 | Project Initialization            | Closed      | Repository foundation, product boundaries, data policy, Lithos data source boundary, and initial checklist completed. |
| Stage 2 | Minimal YAML Extraction Prototype | Closed      | Single-file YAML frontmatter extraction completed. Markdown body content remains excluded.                            |
| Stage 3 | To be defined                     | Not started | Define the next stage before implementation begins.                                                                   |

---

## Completed Work

### Stage 1: Project Initialization

Stage 1 completed the repository foundation and project boundary documentation.

Completed artifacts:

```text
README.md
AGENTS.md
.gitignore
.env.example
.gitattributes
docs/product-vision.md
docs/v0-scope.md
docs/data-policy.md
docs/lithos-data-source.md
docs/stage-1-checklist.md
data/README.md
data/samples/lithos-item-template.json
```

Stage 1 established:

* Project positioning.
* Long-term product direction.
* Future V0 boundary.
* Public-safe data policy.
* Lithos YAML-only data source boundary.
* Basic repository structure.
* Initial sample data template.
* Clear out-of-scope boundaries before implementation.

### Stage 2: Minimal YAML Extraction Prototype

Stage 2 created the first minimal runnable data-entry prototype.

Completed artifacts:

```text
scripts/extract_lithos_yaml.py
data/samples/lithos-sample-card.md
docs/stage-2-yaml-extraction.md
requirements.txt
```

Stage 2 established:

* A local YAML frontmatter extractor.
* A public-safe sample Lithos Markdown card.
* A minimal Python dependency declaration.
* A documented extraction boundary.
* Manual verification guidance.
* Stage 2 limitations and closeout criteria.

---

## Current Working State

The Stage 2 extractor currently:

* Reads one explicitly provided local Markdown file.
* Extracts YAML frontmatter only.
* Excludes Markdown body content.
* Preserves all YAML frontmatter fields as-is.
* Preserves custom YAML fields.
* Outputs a JSON wrapper.

Current JSON wrapper:

```json
{
  "source_path": "",
  "yaml": {},
  "body_included": false
}
```

Current behavior:

* `body_included` is always `false`.
* Normal JSON output goes to stdout.
* Error messages go to stderr.
* Invalid input returns a non-zero exit code.

The extractor is intentionally schema-agnostic.

It does not:

* Require specific YAML fields.
* Remove unknown fields.
* Rename fields.
* Clean field values.
* Normalize metadata.
* Judge metadata quality.
* Determine whether metadata is useful for retrieval.
* Process Markdown body content.

---

## Next Recommended Step

The next step should be to define Stage 3 before any implementation begins.

Stage 3 should not be assumed automatically.

Possible future directions may include:

* Preparing a small public-safe sample dataset.
* Defining a minimal local data normalization boundary.
* Designing how extracted YAML records should become reviewable local data objects.
* Deciding whether Lithos-only data should come before Obsidian or other notes.

The next stage must be explicitly defined before writing code.

---

## Explicitly Out of Scope Now

The project should not currently add:

* Batch import.
* Full Lithos repository scanning.
* Data cleaning pipeline.
* Metadata normalization.
* Schema validation.
* Required YAML fields.
* Markdown body processing.
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

* Stage 1 is closed.
* Stage 2 is closed.
* Stage 2 focused only on minimal YAML frontmatter extraction.
* The extractor is schema-agnostic.
* The extractor preserves all YAML fields as-is.
* The extractor does not judge metadata quality.
* The extractor does not determine retrieval usefulness.
* Markdown body content remains excluded.
* `body_included` remains fixed as `false`.
* `PROJECT_STATUS.md` should become the dynamic project-state entry point for future AI-assisted work.
* This file should be updated after each meaningful project round.

---

## Collaboration Workflow

The intended workflow is:

```text
Discuss product direction and stage boundaries in ChatGPT
→ Generate a constrained implementation task if needed
→ Let Codex execute repository changes
→ Review Codex results in ChatGPT
→ Commit and push when the stage or task is ready
→ Update PROJECT_STATUS.md after meaningful progress
```

ChatGPT is mainly used for:

* Product positioning.
* Stage planning.
* Scope control.
* Task decomposition.
* Codex Prompt writing.
* Result review.
* Portfolio narrative refinement.

Codex is mainly used for:

* Repository edits.
* Script implementation.
* Documentation updates.
* Small scoped engineering tasks.

Repository-facing files should be written in English.

Discussion with ChatGPT and Codex task instructions may be written in Chinese.

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

Keep updates concise.

Do not turn this file into a detailed changelog.

Detailed implementation notes should remain in stage-specific documentation files.

When starting a new AI-assisted project round, read this file first.
