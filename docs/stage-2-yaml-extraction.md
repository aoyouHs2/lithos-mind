# Stage 2: Minimal YAML Extraction Prototype

## Purpose

Stage 2 provides one minimal local script that reads a single Markdown file and extracts its YAML frontmatter. It verifies the YAML-only data boundary defined for Lithos work cards.

The script stops reading at the closing frontmatter delimiter. Markdown body content is intentionally excluded and is never included in the JSON output.

## Input Format

The input must be one local UTF-8 Markdown file that begins with non-empty YAML frontmatter enclosed by `---` delimiter lines:

```markdown
---
title: Example Work
category: reading
tags:
  - literature
  - note
custom_field: preserved
rating: 4
---

This Markdown body should not be included.
```

The parsed YAML value must be an object/dictionary. Empty frontmatter and top-level scalar or list values are rejected. This is an input-shape requirement, not a metadata schema.

## Extraction Boundary

The extractor is intentionally schema-agnostic. It does not require specific YAML fields. All fields parsed from the YAML frontmatter are preserved as-is inside the `yaml` object, including custom or unknown fields.

The extractor does not:

- Remove extra fields.
- Rename fields.
- Clean or normalize field values.
- Judge field values or metadata quality.
- Determine whether metadata is useful or suitable for retrieval.

The only current guarantees are:

- YAML frontmatter is extracted.
- Markdown body content is excluded.
- Output follows the existing JSON wrapper structure.
- `body_included` remains `false`.

## Usage

Install the minimal dependency in a local Python environment:

```bash
python -m pip install -r requirements.txt
```

Run the extractor with one Markdown file path:

```bash
python scripts/extract_lithos_yaml.py data/samples/lithos-sample-card.md
```

## Output Format

The script writes one JSON object to standard output:

```json
{
  "source_path": "data/samples/lithos-sample-card.md",
  "yaml": {
    "title": "Example Work",
    "category": "reading",
    "tags": [
      "literature",
      "note"
    ],
    "custom_field": "preserved",
    "rating": 4
  },
  "body_included": false
}
```

`body_included` is always `false`. The Markdown body is not parsed, cleaned, summarized, stored, or output.

Invalid input produces a clear error on standard error and exits with a non-zero status. This includes a missing file, missing opening or closing frontmatter delimiters, malformed YAML, empty frontmatter, and frontmatter that does not parse into an object/dictionary.

## Manual Verification

Run the basic verification command:

```bash
python scripts/extract_lithos_yaml.py data/samples/lithos-sample-card.md
```

Verify that the extractor:

- Outputs JSON to standard output.
- Preserves all YAML frontmatter fields.
- Preserves custom YAML fields.
- Excludes Markdown body content.
- Keeps `body_included` as `false`.
- Returns clear errors for invalid inputs.

Invalid inputs that should return errors include:

- A missing file.
- Missing YAML frontmatter.
- A missing closing frontmatter delimiter.
- Malformed YAML.
- Empty YAML.
- YAML with a top-level value that is not an object/dictionary.

## Current Limitations

This prototype processes one explicitly provided local file only. It is not a batch importer or repository scanner.

Stage 2 does not provide a data cleaning pipeline, embedding system, vector database, RAG system, Agent answer generation, backend, frontend, API, or deployment configuration.

## Stage 2 Closeout

Stage 2 can be considered complete when the extractor behavior, extraction boundary, manual verification steps, and current limitations have been reviewed, committed, and pushed to the remote repository.
