# Lithos Data Source Boundary

## Purpose

This document defines the current boundary for using the separate Lithos repository as a future data source for Lithos Mind.

## What Lithos Is

Lithos is a separate repository containing work cards. A work card may contain two parts:

- YAML frontmatter.
- Markdown body content.

Lithos Mind does not integrate with or import data from that repository in the current initialization phase.

## Why Lithos Is a Future Data Source

Lithos work cards may provide structured personal knowledge metadata relevant to learning, cultural collections, reading, and long-term interests. In the current data source boundary, only YAML frontmatter is treated as the usable part of these work cards, while Markdown body content remains excluded.

## Current Stage Scope

The current stage includes only:

- Defining YAML frontmatter as the permitted part of a Lithos work card.
- Defining a minimal JSON representation for one future YAML-only extracted item.
- Documenting the boundary between YAML frontmatter and Markdown body content.

No real Lithos data is imported or processed in this stage.

## Out of Scope

The current stage excludes:

- Markdown body content from Lithos work cards.
- Real data import or extraction.
- Invented YAML fields or fictional records.
- Data cleaning or transformation pipelines.
- Indexing, embeddings, retrieval, RAG, or agent processing.
- Frontend, backend, API, or deployment work.

## YAML-Only Item Template

[`data/samples/lithos-item-template.json`](../data/samples/lithos-item-template.json) represents one future YAML-only extracted item with three fields:

- `source_path`: reserved for the source card path in a future extraction step.
- `yaml`: reserved for the extracted YAML frontmatter without assuming specific YAML fields.
- `body_included`: set to `false` to record that Markdown body content is excluded.

The template contains no real or fictional Lithos data.

## Markdown Body Exclusion

Markdown body content must not be imported, indexed, embedded, summarized, or otherwise processed in the current stage. Only YAML frontmatter is within the defined future data source boundary.
