# V0 Scope Boundary

## Purpose

This document defines the intended scope boundary for a future Lithos Mind V0 public demo.

It is a development planning document, not a record of the current implementation state. For the latest project status, see `PROJECT_STATUS.md` in the repository root.

## V0 Goal

The future V0 should establish a minimal, reviewable, public-data-first personal knowledge base Agent demo.

The intended V0 loop is:

```text
public-safe data import
-> data cleaning
-> structured storage
-> retrieval
-> Agent answer
-> source citation
-> simple frontend
-> public demo
```

V0 is not expected to be a complete product. It should be a small but coherent demo that shows how public-safe personal data can become searchable, traceable, and useful for grounded Agent answers.

## Intended User Experience

A successful V0 should allow a viewer to:

- Understand what Lithos Mind is.
- Browse selected public-safe personal data.
- Ask questions about the public knowledge base.
- Receive answers grounded in retrieved records.
- See source references or citations.
- Review the project through clear documentation and a public demo.

## In Scope for V0

V0 may include:

- A small set of reviewed public-safe personal data.
- Data cleaning and normalization into a simple structured format.
- Lightweight storage for prepared records.
- Basic retrieval over prepared records.
- Agent-style answers grounded in retrieved records.
- Source references or citations for answers.
- A simple frontend or interface for demonstration.
- Public-safe documentation that explains product scope, data sources, and implementation assumptions.

## Out of Scope for V0

V0 should not include:

- Work assistant features.
- PRD generation.
- Todo management.
- Calendar or schedule management.
- Private message processing.
- Email processing.
- Financial data processing.
- Medical data processing.
- Account or credential management.
- Sensitive personal data ingestion.
- Full private vault import.
- Large-scale production infrastructure.
- Complex permission systems.
- Multi-user collaboration.
- Commercial SaaS features.

## Data Boundary for V0

V0 must remain limited to public-safe personal data.

Possible data types include:

- Public learning notes.
- Public reading records.
- Public cultural collection records.
- Public long-term interest logs.
- Public-safe article or book notes.
- Reviewed sample or demo data.

V0 must not process or commit private messages, emails, financial records, medical records, credentials, private schedules, or other sensitive personal data.

## Image Boundary for V0

Images may be used as display assets or metadata in a future V0.

Allowed future uses may include:

- Covers.
- Posters.
- Work images.
- Image titles.
- Image tags.
- Image descriptions.
- Public-safe personal comments.

V0 should not assume:

- OCR.
- Image content understanding.
- Image vector search.
- Multimodal Agent reasoning.
- Direct question answering based on image content.

The Agent direction remains primarily text-based unless a later stage explicitly defines otherwise.

## Success Criteria

V0 will be considered successful when:

- A viewer can understand the project idea from the repository and demo.
- A small public-safe dataset can be prepared and reviewed.
- The system can retrieve relevant records from that dataset.
- Agent answers are grounded in retrieved records.
- Answers include source references or citations.
- The demo does not expose sensitive or private data.
- The repository clearly documents product scope, data boundary, and implementation assumptions.

## Current Repository Relationship

The repository is still before V0 implementation.

Stage 1 and Stage 2 have been completed, but V0 capabilities such as retrieval, embeddings, vector database, Agent answers, frontend, backend, API, and deployment have not been implemented.

The next stage should be defined separately before implementation begins.
