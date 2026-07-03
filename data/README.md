# Data Directory

## Purpose

The `data/` directory is intended for files related to Lithos Mind's future public-safe data. In the current phase, it provides documentation only and contains no real data, cleaned data, or vector database files.

## Current Stage

During the **Project Initialization Phase**, the `data/` directory contains this guide and a minimal YAML-only template under `data/samples/`. The current phase does not include:

- Real data ingestion.
- Raw data storage.
- Cleaned data storage.
- Vector database files.
- A data cleaning pipeline.
- Embedding generation.

## Planned Data Categories

Future stages may support:

- Public learning notes.
- Public reading records.
- Public cultural collections.
- Public long-term interest logs.
- Public-safe article notes.
- Public-safe book notes.
- Public-safe personal knowledge cards.

## Suggested Future Directory Structure

The following structure may be introduced in future stages. These directories are not created in the current phase.

```text
data/
├── README.md
├── samples/
├── user-provided/
├── raw/
├── cleaned/
└── vector_db/
```

- `samples/` is for public-safe templates or reviewed sample records.
- `user-provided/` is for temporary user-provided public-safe data during local development.
- `raw/` is for local raw data only and should not be committed unless reviewed.
- `cleaned/` is for local cleaned data only and should not be committed unless reviewed.
- `vector_db/` is for generated vector database files and should not be committed.

## Data Commit Rules

- Do not commit private data.
- Do not commit unreviewed raw data.
- Do not commit emails, private messages, financial records, medical records, credentials, or sensitive personal data.
- Do not commit local vector database files.
- Only commit public-safe data or templates after review.
- Sample data must be based on user-provided public-safe data or remain as templates.
- Codex must not invent sample records that pretend to be the user's real data.

## Relationship to Data Policy

See [`docs/data-policy.md`](../docs/data-policy.md) for the complete data boundary and review rules.

## Current Repository Status

The `data/` directory currently contains:

- `README.md`
- `samples/lithos-item-template.json`

The `samples/` directory currently contains only a YAML-only template. It does not contain real or fictional sample records.

No `user-provided/`, `raw/`, `cleaned/`, or `vector_db/` directories or real data files exist at this stage.
