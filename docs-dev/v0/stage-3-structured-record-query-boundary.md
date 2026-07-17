# Stage 3: Structured Record and Query Boundary Definition

## Status

- **Stage:** Stage 3: Structured Record and Query Boundary Definition
- **Status:** Open — definition stage

Stage 3 is a documentation-only stage. It is not complete until the project owner reviews and approves the record and query boundaries defined here.

## Purpose

Stage 3 defines a text-first card record boundary for a future Agent database. Original Lithos Markdown cards remain the source of truth, while the future database is a derived, query-ready copy containing selected YAML metadata and Markdown body text.

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

A future import or sync process should preserve `source_path` and `source_hash`, or equivalent traceability metadata, so records can be connected to source files and source changes can be detected. Stage 3 does not implement source hashing or synchronization.

## Current Implementation Boundary

The implemented boundary remains unchanged:

- Stage 2 reads one explicitly provided local Markdown file.
- It extracts YAML frontmatter only.
- It excludes Markdown body content and keeps `body_included` as `false`.
- It preserves unknown and custom YAML fields.
- It does not provide batch import or full repository scanning.

Stage 3 does not parse, store, index, or otherwise process Markdown body text. It only defines how body text may be handled by a later implementation stage.

## Agent-Facing Record Content

A future text-first Agent record may include:

| Record group | Conceptual fields |
| --- | --- |
| Source traceability | `source_path`, `source_hash` |
| Selected structured metadata | `type`, `title`, `original_title`, `year`, `url`, `tags`, `my_rating`, `date`, `repeat_dates`, `external_id`, `data_source` |
| Card note text | `body_text` |
| Raw metadata preservation | `raw_yaml_json` |

This is a conceptual field list, not a final database schema or a required YAML schema. Field availability may vary, and mapping, validation, naming, and normalization rules require a later implementation stage.

## Markdown Body Text

Future Agent records may store the Markdown body as `body_text`. Card bodies can contain the project owner's own short notes, which may support future retrieval, answering, and citation.

Storing `body_text` is different from storing the entire raw Markdown file. The future record would keep the useful body text as an Agent-facing field while the original `.md` file remains canonical.

Stage 3 does not implement Markdown body parsing. The Stage 2 extractor remains YAML-only, and any future full-card parser must be defined in a later implementation stage.

## Raw YAML

`raw_yaml_json` is recommended as a preservation field because it can retain all original YAML metadata, prevent metadata loss, and support future remapping or reinterpretation.

It may contain fields that are not Agent-facing query fields. Preserving a value inside `raw_yaml_json` does not automatically expose that value to the Agent or make it normalized, indexed, searchable, or filterable.

## Raw Markdown

Storing full `raw_markdown` in the Agent database is not currently recommended. The original `.md` file is the source of truth, and the database should remain a query-ready derived copy.

For the current conceptual boundary, `source_path`, `source_hash`, `body_text`, and `raw_yaml_json` provide sufficient traceability and text content. Full raw Markdown storage may be reconsidered only if a later stage identifies a concrete need.

## Image and Cover Boundary

Image references such as `cover` are non-Agent metadata:

- Image files are not stored in the Agent database.
- Image references are not separately extracted, normalized, indexed, queried, or embedded as Agent-facing data.
- Image references may remain passively preserved inside `raw_yaml_json`.
- The Agent database does not parse, copy, summarize, or reason over image files or image paths.
- The Agent must not answer questions based on image content.
- Display concerns remain outside the current Agent database scope.

## Future Agent Query Boundary

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

Stage 3 can be closed when:

- The project owner approves the documentation-only scope, text-first card record boundary, and structured database-first direction.
- Original `.md` cards are documented as the source of truth.
- The distinction between the Stage 2 YAML-only extractor and a future full-card record is clear.
- The conceptual Agent-facing fields are understandable without being treated as a final database or YAML schema.
- Future `body_text` handling is documented without implementing Markdown body parsing.
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
