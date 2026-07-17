# Data Directory

## Purpose

The `data/` directory is the central place for Lithos Mind data-related templates, samples, and future data artifacts.

This document defines:

* What data is allowed.
* What data is disallowed.
* How sample data should be handled.
* How Lithos work cards are treated as a future data source.
* Why Markdown body content is currently excluded.
* What data-related work remains out of scope.

Lithos Mind is a public-data-first personal knowledge base Agent project. The `data/` directory must remain safe to review on GitHub.

## Public-Safe Data Principle

Lithos Mind should only use public-safe personal data.

Public-safe personal data means data that:

* The project owner intentionally considers safe for a public or portfolio demo.
* Does not expose private communication, sensitive identity information, credentials, financial records, medical records, or other private records.
* Can be reviewed, cited, or demonstrated without creating privacy risk.

If the safety of a data item is unclear, it should not be committed.

## Allowed Data

Allowed data may include:

* Public learning notes.
* Public reading records.
* Public cultural collections.
* Public long-term interest logs.
* Public-safe article notes.
* Public-safe book notes.
* Public-safe personal knowledge cards.
* Public-safe manually prepared sample records.
* Empty templates.
* Small fictional examples that are clearly marked as sample or demo data.

Allowed data should still be reviewed before it is committed to the repository.

## Disallowed Data

Lithos Mind must not process, store, or commit:

* Private messages.
* Chat history from private conversations.
* Emails.
* Financial records.
* Medical records.
* Account credentials.
* Passwords or API keys.
* Government IDs or identity documents.
* Phone numbers.
* Home addresses.
* Private schedules or calendar records.
* Private work documents.
* Confidential company information.
* Sensitive personal data.
* Any data that should not be publicly reviewed on GitHub.

## Sample Data Rules

Sample data must be small, readable, and public-safe.

Sample data should either:

* Come from user-provided public-safe data.
* Remain as empty templates.
* Use fictional placeholder content that is clearly marked as sample or demo data.

Codex or other AI tools must not invent sample records that pretend to be the project owner's real notes, reading records, cultural collections, or interest logs.

## Current Data Directory Structure

The current `data/` directory contains only reviewed templates and public-safe sample files.

```text
data/
├── README.md
└── samples/
    ├── lithos-item-template.json
    └── lithos-sample-card.md
```

### `data/samples/lithos-item-template.json`

This file defines the minimal JSON wrapper for a future YAML-only extracted item:

```json
{
  "source_path": "",
  "yaml": {},
  "body_included": false
}
```

The template contains no real or fictional personal data.

### `data/samples/lithos-sample-card.md`

This file provides a small public-safe Markdown sample for testing the Stage 2 YAML extraction prototype.

It may contain Markdown body content for testing, but the current extractor must not output, process, summarize, index, or store the body content.

## Lithos Data Source Boundary

Lithos is a separate source of work cards that may later provide public-safe cultural collection metadata for Lithos Mind.

A Lithos work card may contain two parts:

* YAML frontmatter.
* Markdown body content.

In the current data boundary, only YAML frontmatter is treated as usable input for Lithos Mind.

Markdown body content remains excluded.

Lithos Mind does not yet batch import or scan the full Lithos repository. Stage 2 only provides a minimal local extractor for one explicitly provided Markdown file.

## YAML-Only Extraction Boundary

The current YAML extraction prototype preserves the YAML frontmatter inside this JSON wrapper:

```json
{
  "source_path": "",
  "yaml": {},
  "body_included": false
}
```

The extractor is intentionally schema-agnostic.

It does:

* Read one explicitly provided local Markdown file.
* Extract YAML frontmatter only.
* Preserve all YAML frontmatter fields as-is.
* Preserve custom or unknown YAML fields.
* Exclude Markdown body content.
* Keep `body_included` as `false`.

It does not:

* Require specific YAML fields.
* Remove unknown fields.
* Rename fields.
* Clean field values.
* Normalize metadata.
* Judge metadata quality.
* Determine whether metadata is useful for retrieval.
* Process Markdown body content.

## Markdown Body Exclusion

Markdown body content must not be imported, indexed, embedded, summarized, cleaned, stored, or otherwise processed in the current data boundary.

This rule exists to keep the current prototype narrow and public-safe.

Only YAML frontmatter is within the current Lithos data source boundary.

## Future Structured Record Direction

Future stages may prepare reviewed YAML metadata as normalized records for controlled, database-style querying. Any such record should remain traceable to its source and preserve the raw extracted YAML.

This is a planned direction, not a current implementation. The current boundary remains YAML-only: Markdown body content is excluded, extraction is limited to one explicitly provided file, and there is no batch import, metadata normalization implementation, database, or vector database.

## Future Data Directory Possibilities

Future stages may introduce additional local data directories, such as:

```text
data/
├── samples/
├── user-provided/
├── raw/
├── cleaned/
└── generated/
```

These directories are not required in the current stage.

Future raw, cleaned, generated, or vector database files should remain local unless explicitly reviewed and approved for public commit.

The project should not commit:

* Raw private data.
* Unreviewed extracted data.
* Local vector databases.
* Generated embeddings.
* Local database files.
* Cache files.
* Logs.
* Environment-specific data artifacts.

## Source Traceability

Future data records should preserve source information where possible, including:

* Source path.
* Source name.
* Source URL, if available.
* Creation date or collection date, if available.
* Data type.
* Tags.
* Visibility or public-safety status.

Source traceability is important for future retrieval, citation, and review.

## Current Out of Scope

The current data boundary does not include:

* Batch import.
* Full Lithos repository scanning.
* Data cleaning pipelines.
* Metadata normalization.
* Schema validation.
* Required YAML fields.
* Database implementation.
* Markdown body processing.
* Embedding generation.
* Vector database creation.
* Retrieval implementation.
* RAG.
* Agent answer generation.
* Frontend, backend, API, or deployment work.
* Private or sensitive data processing.

## Data Review Checklist

Before adding or committing any data, review the following questions:

* [ ] Is this data intentionally public-safe?
* [ ] Does it contain private messages, emails, financial records, medical records, credentials, or other sensitive information?
* [ ] Can this data be shown in a public demo or portfolio review?
* [ ] Is the source clear?
* [ ] Is the data small and reviewable?
* [ ] Should this data be committed, kept local, or excluded?
* [ ] Does this data follow the current YAML-only and Markdown-body-exclusion boundary?
