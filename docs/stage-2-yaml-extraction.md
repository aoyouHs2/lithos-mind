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
---

This Markdown body is outside the Stage 2 data boundary.
```

The parsed YAML value must be an object/dictionary. Empty frontmatter and top-level scalar or list values are rejected.

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
    ]
  },
  "body_included": false
}
```

`body_included` is always `false`. The Markdown body is not parsed, cleaned, summarized, stored, or output.

Invalid input produces a clear error on standard error and exits with a non-zero status. This includes a missing file, missing opening or closing frontmatter delimiters, malformed YAML, empty frontmatter, and frontmatter that does not parse into an object/dictionary.

## Current Limitations

This prototype processes one explicitly provided local file only. It is not a batch importer or repository scanner.

Stage 2 does not provide a data cleaning pipeline, embedding system, vector database, RAG system, Agent answer generation, backend, frontend, API, or deployment configuration.
