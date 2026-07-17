# Stage 3: Structured Record and Query Boundary Definition

## Status

- **Stage:** Stage 3: Structured Record and Query Boundary Definition
- **Status:** Open — definition stage

Stage 3 is a documentation-only stage. It is not complete until the project owner reviews and approves the record and query boundaries defined here.

## Purpose

Stage 3 defines how YAML frontmatter extracted from Lithos work cards may later become reviewable structured records and how a future Agent may query those records through controlled database-style operations.

This stage prepares a boundary for later implementation. It does not implement metadata normalization, a database, retrieval, or Agent behavior.

## Why Structured Records Come Before Vector Retrieval

The current Lithos source boundary contains YAML metadata rather than large unstructured text. Fields such as title, category, tags, creator, and date are better suited to explicit filtering and field-based lookup than to an early embedding and vector-search pipeline.

Prioritizing structured database-style records first should make future data easier to inspect, validate, filter, and trace back to its source. It also keeps query behavior narrow and reviewable.

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

Stage 3 treats this output as a possible future input to a separate record-preparation process. The Stage 2 extractor remains responsible only for extraction. It must continue to preserve all YAML fields as-is and must not normalize or judge them.

No record-preparation process is implemented in Stage 3.

## Current Data Boundary

The current data boundary remains unchanged:

- Only YAML frontmatter is usable input.
- Markdown body content remains excluded.
- One explicitly provided local file is the only supported extraction input.
- Unknown and custom YAML fields remain preserved.
- No strict YAML field set is required.
- No batch import or full Lithos repository scan is introduced.

Markdown body content must not be parsed, cleaned, summarized, stored, indexed, embedded, or used to answer questions in this stage.

## Conceptual Record Groups

A future normalized record may organize available metadata into the following conceptual groups. These groups describe review needs; they are not a database schema or a list of required fields.

| Record group | Purpose | Possible examples when available |
| --- | --- | --- |
| Source traceability fields | Connect a record to its reviewed source. | Source path, source name, source URL, source type |
| Display fields | Present a record clearly to a reviewer or future interface. | Title, subtitle, description, display image reference |
| Filterable fields | Support controlled exact-match, list, range, or date filters. | Category, type, tags, creator, author, year, date |
| Searchable metadata fields | Support controlled text lookup over selected metadata only. | Title, aliases, creator, description |
| Raw preserved YAML fields | Retain the original extracted metadata for review and traceability. | The complete unmodified `yaml` object |
| Public-safety review fields | Record whether an item is approved for the public-safe project boundary. | Review status, visibility, review note |

Field availability may vary between source cards. Stage 3 does not require these examples, define canonical names, or implement mapping rules.

## Raw YAML and Future Normalized Records

Raw extracted YAML and a future normalized database record serve different purposes:

| Raw extracted YAML | Future normalized record |
| --- | --- |
| Preserves source metadata as-is. | Organizes selected values for consistent review and controlled queries. |
| May contain custom, unknown, or inconsistently named fields. | May map available source values into defined conceptual groups. |
| Reflects extraction output. | Would be created by a separate, future preparation step. |
| Remains the traceable source representation. | Must retain a link to the source and the raw preserved YAML. |

Normalization must not silently replace or discard the raw YAML. Any future mapping, coercion, defaulting, or validation rules require a later implementation stage and explicit review.

## Future Agent Query Boundary

A future Agent may identify a supported user intent and translate it into an allowlisted query operation with validated parameters. A controlled application layer, not the Agent itself, should execute the database query.

Possible future supported query intents include:

- Search selected metadata by title.
- Filter records by category or type.
- Filter records by one or more tags.
- Filter by creator or author when that metadata is available.
- Filter by year or date when that metadata is available.
- Return the details of a selected record.
- Return source references for selected records.

Support for these intents is conceptual only in Stage 3. Exact matching behavior, result limits, sorting, parameter validation, and missing-field behavior must be defined before query implementation.

## Explicitly Unsupported Query Behavior

The future query boundary must not allow:

- Free-form SQL generation or execution by the Agent.
- Uncontrolled or direct Agent access to a database.
- Queries outside predefined operations and validated parameters.
- Answers derived from Markdown body content.
- Vector search in Stage 3.
- Image understanding, OCR, or image-based answering.
- Private, sensitive, or unreviewed personal data processing.

Stage 3 also does not provide Agent answer generation. It only defines a possible boundary for later controlled record retrieval.

## Acceptance Criteria

Stage 3 can be closed when:

- The project owner approves the Stage 3 name, documentation-only scope, and structured database-first direction.
- The relationship between Stage 2 extraction output and future structured records is clear.
- The YAML-only boundary and continued Markdown body exclusion are explicit.
- The conceptual record groups are understandable without being treated as a required schema.
- The distinction between raw YAML and a future normalized record is documented.
- Supported query intents and prohibited query behavior are documented.
- Source traceability and public-safety review remain part of the future record boundary.
- No implementation code, dependency, database artifact, schema, or sample personal record is added.
- A later implementation stage can be scoped without assuming vector retrieval is required.

## Out of Scope

Stage 3 does not include:

- Changes to the Stage 2 extractor.
- Batch import or full Lithos repository scanning.
- Required YAML fields or schema enforcement.
- Metadata cleaning or normalization implementation.
- Database selection, database creation, schemas, SQL, migrations, ORM code, or seed data.
- Query implementation or database access.
- Markdown body processing.
- Embeddings, vector databases, semantic search, or RAG.
- Agent answer generation.
- Image understanding.
- Frontend, backend, API, or deployment work.
- Private or sensitive data processing.

Any implementation work must be proposed and reviewed as a separate later stage.
