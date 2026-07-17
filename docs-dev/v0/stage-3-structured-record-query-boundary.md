# Stage 3: Structured Record and Query Boundary Definition

## Status

- **Stage:** Stage 3: Structured Record and Query Boundary Definition
- **Status:** Closed

Stage 3 was a documentation-only definition stage. It is closed after the project owner reviewed and approved the record and query boundaries defined here.

## Purpose

Stage 3 defines a complete text-first card record boundary for a future Agent database. Original Lithos Markdown cards remain the source of truth, while the future database is a derived, query-ready copy containing selected YAML metadata and Markdown body text.

This stage also defines how a future Agent may query those records through controlled database-style operations. It does not implement card parsing, metadata normalization, a database, retrieval, or Agent behavior.

## Why Structured Records Come Before Vector Retrieval

Lithos cards combine structured YAML metadata with short Markdown notes. Fields such as title, type, tags, year, and date are suited to explicit filtering, while card notes can remain available as text for future retrieval, answering, and citation.

Prioritizing structured database-style records first should make future data easier to inspect, validate, filter, and trace back to its source. Text-first means that Agent-facing records focus on selected metadata and useful card text, not display assets or image content.

Vector retrieval is not permanently rejected. It may be considered in a later stage if the project introduces larger unstructured text sources or a clear need for semantic search.

## Relationship to Stage 2

Stage 2 extracts YAML frontmatter from one explicitly provided local Markdown file and returns a schema-agnostic wrapper:

```json
{
  "source_path": "",
  "yaml": {},
  "body_included": false
}
```

The Stage 2 extractor remains YAML-only. It continues to preserve all YAML fields as-is, excludes Markdown body content, and does not normalize or judge metadata.

Stage 3 expands only the conceptual boundary for a future full-card record. It does not change the Stage 2 extractor or implement a full-card parser.

## Source of Truth

Original `.md` card files remain the canonical source of truth. A future Agent database should contain derived, query-ready records rather than replace or become the canonical copy of those files.

The database must not be treated as the canonical original. Each derived record should remain traceable to its source file through `source_path`.

## Current Implementation Boundary

The implemented boundary remains unchanged:

- Stage 2 reads one explicitly provided local Markdown file.
- It extracts YAML frontmatter only.
- It excludes Markdown body content and keeps `body_included` as `false`.
- It preserves unknown and custom YAML fields.
- It does not provide batch import or full repository scanning.

Stage 3 does not parse, store, index, or otherwise process Markdown body text. It only defines how body text may be handled by a later implementation stage.

## Complete Text-First Card Record Model

A future Agent database should use a complete text-first card record model rather than a minimal query-only record. The derived record should preserve the card's useful text content for querying, answering, and citation instead of retaining only a few filter fields.

A future record may include:

| Record group | Conceptual fields |
| --- | --- |
| Source traceability | `source_path`, `source_hash` |
| Selected structured metadata | `type`, `title`, `original_title`, `year`, `url`, `tags`, `my_rating`, `date`, `repeat_dates`, `external_id`, `data_source` |
| Card note text | `body_text` |
| Raw metadata preservation | `raw_yaml_json` |

This is a conceptual field list, not a final database schema or a required YAML schema. Field availability may vary, and mapping, validation, naming, and normalization rules require a later implementation stage.

## Agent-Facing YAML Fields

The confirmed conceptual Agent-facing YAML fields are:

- `type`
- `title`
- `original_title`
- `year`
- `tags`
- `my_rating`
- `date`
- `repeat_dates`
- `url`
- `external_id`
- `data_source`

These fields are neither a required YAML schema nor a final database schema. A future implementation may map source YAML names such as `id` to `external_id` and `dataSource` to `data_source`, but Stage 3 does not implement any mapping.

## Markdown Body Text

Future Agent records may store the Markdown body as `body_text`. It should preserve the Markdown body content as-is while excluding YAML frontmatter. Markdown headings, dates, and note structure inside the body should remain preserved.

Card bodies can contain the project owner's own short notes, which may support future retrieval, answering, and citation.

Storing `body_text` is different from storing the entire raw Markdown file. The future record would keep the useful body text as an Agent-facing field while the original `.md` file remains canonical.

Stage 3 does not implement Markdown body parsing. The Stage 2 extractor remains YAML-only, and any future full-card parser must be defined in a later implementation stage.

## Raw YAML

`raw_yaml_json` is recommended as a preservation field because it can retain all original YAML metadata, prevent metadata loss, and support future remapping or reinterpretation.

It may contain fields that are not Agent-facing query fields. Preserving a value inside `raw_yaml_json` does not automatically expose that value to the Agent or make it normalized, indexed, searchable, or filterable.

## Raw Markdown

Storing full `raw_markdown` in the Agent database is not currently recommended. The original `.md` file is the source of truth, and the database should remain a query-ready derived copy.

For the current conceptual boundary, `source_path`, `source_hash`, `body_text`, and `raw_yaml_json` provide sufficient traceability and text content. Full raw Markdown storage may be reconsidered only if a later stage identifies a concrete need.

## Source Path and Source Hash

`source_path` identifies the original `.md` file from which a derived database record was created.

`source_hash` is a future system-generated technical field. Users should not manually add it to source cards. A future import process may compute it from the original `.md` file content and store it in the derived Agent database record.

During a future sync, the system may recompute the current file hash and compare it with the stored database hash. A changed hash indicates that the source file likely changed and that the derived record may need to be refreshed.

Stage 3 does not implement hashing, import, refresh, or synchronization behavior.

## Image and Cover Boundary

Image references such as `cover` are non-Agent metadata:

- Image files are not stored in the Agent database.
- Image references are not separately extracted, normalized, indexed, queried, or embedded as Agent-facing data.
- Image references may remain passively preserved inside `raw_yaml_json`.
- The Agent database does not parse, copy, summarize, or reason over image files or image paths.
- The Agent must not answer questions based on image content.
- Display concerns remain outside the current Agent database scope.

## Controlled Query Boundary

A future Agent may identify a supported user intent. A controlled application layer should translate that intent into an allowlisted query operation with validated parameters and execute the database query. The Agent must not generate or execute free-form SQL.

Possible future supported query intents include:

- Search by title or original title.
- Search selected text fields, including `body_text`, when later implementation rules allow it.
- Filter records by type.
- Filter records by one or more tags.
- Filter by year or date when that metadata is available.
- Find records by external identifier or data source when available.
- Return the details of a selected record.
- Return source references for selected records.

Future query operations should use defined Agent-facing text and metadata fields, not image files or image paths. `raw_yaml_json` remains a preservation field and is not automatically queryable.

Support for these intents is conceptual only in Stage 3. Exact text-search behavior, matching rules, result limits, sorting, parameter validation, and missing-field behavior must be defined before query implementation.

## Explicitly Unsupported Query Behavior

The future query boundary must not allow:

- Free-form SQL generation or execution by the Agent.
- Uncontrolled or direct Agent access to a database.
- Queries outside predefined operations and validated parameters.
- Automatic exposure of every field preserved in `raw_yaml_json`.
- Queries or answers based on image files, image content, or image paths.
- Vector search in Stage 3.
- Image understanding, OCR, or image-based answering.
- Private, sensitive, or unreviewed personal data processing.

Stage 3 also does not provide Agent answer generation. It only defines a possible boundary for later controlled record retrieval.

## Acceptance Criteria

Stage 3 was closed after these criteria were met:

- The project owner approves the documentation-only scope, complete text-first card record boundary, and structured database-first direction.
- Original `.md` cards are documented as the source of truth.
- The distinction between the Stage 2 YAML-only extractor and a future full-card record is clear.
- The conceptual Agent-facing YAML fields are understandable without being treated as a final database or required YAML schema.
- Future `body_text` handling preserves body content as-is while excluding YAML frontmatter, without implementing Markdown body parsing.
- `source_hash` is documented as a future system-generated field for change detection, not a manually maintained source-card field.
- The roles of `raw_yaml_json` and the original source file are explicit, and full `raw_markdown` is not required.
- Image references remain outside Agent-facing query fields and may only be passively preserved through raw YAML.
- Supported query intents and prohibited query behavior are documented.
- No implementation code, dependency, database artifact, schema, or sample personal record is added.
- A later implementation stage can be scoped without assuming vector retrieval is required.

## Out of Scope

Stage 3 does not include:

- Changes to the Stage 2 extractor.
- Batch import or full Lithos repository scanning.
- Required YAML fields or schema enforcement.
- Metadata cleaning or normalization implementation.
- Markdown body parsing or full-card record preparation.
- Source hashing or synchronization implementation.
- Database selection, database creation, schemas, SQL, migrations, ORM code, or seed data.
- Query implementation or database access.
- Required storage of full `raw_markdown`.
- Embeddings, vector databases, semantic search, or RAG.
- Agent answer generation.
- Image storage, image-reference extraction or normalization, image understanding, OCR, or image embeddings.
- Frontend, backend, API, or deployment work.
- Private or sensitive data processing.

Any implementation work must be proposed and reviewed as a separate later stage.

## Stage 3 Closeout

Stage 3 is closed after the project owner approved:

- A complete text-first card record model with original `.md` cards as the source of truth and derived Agent database records as query-ready text copies.
- Markdown `body_text` preserved as-is without YAML frontmatter, selected YAML metadata as conceptual Agent-facing fields, and `raw_yaml_json` for complete YAML metadata preservation.
- Full `raw_markdown` not currently recommended and image references excluded from Agent-facing fields.
- `source_path` and a future system-generated `source_hash` for traceability and change detection.
- A structured database-first direction before vector retrieval and a controlled future Agent query boundary.

Stage 3 did not implement a database, parser, Markdown body extraction, hashing, synchronization, query execution, Agent answer generation, vector retrieval, frontend, backend, API, or deployment.
