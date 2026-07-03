# V0 Scope

## Purpose

This document defines the scope boundary for a future Lithos Mind V0. The goal of V0 is to establish a minimal, demonstrable, and reviewable public-data-first personal knowledge base agent demo.

## V0 Goal

The future V0 aims to establish a minimal end-to-end flow:

```text
data import -> data cleaning -> structured storage -> retrieval -> agent answer -> source citation -> simple frontend -> public demo
```

This flow is the target direction for V0 and has not been implemented in the current initialization phase.

## In Scope for V0

- Importing a small set of public-safe personal data.
- Cleaning and normalizing the data into a simple structured format.
- Storing cleaned records in a lightweight local format.
- Basic retrieval over the prepared records.
- Agent-style answers grounded in retrieved records.
- Source citation or source reference for answers.
- A simple frontend or interface for demonstration.
- A public-safe demo that can be reviewed as a portfolio project.

## Out of Scope for V0

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
- Large-scale production infrastructure.
- Complex permission systems.
- Multi-user collaboration.
- Commercial SaaS features.

## Success Criteria

V0 will be considered successful when:

- A user can import or prepare a small public-safe dataset.
- The system can retrieve relevant records from that dataset.
- The agent can answer questions based on retrieved records.
- Answers include source references or citations.
- The demo clearly shows the product idea without exposing sensitive data.
- The repository documents product scope, data boundary, and implementation assumptions clearly.

## Current Phase vs V0

The current **Project Initialization Phase** includes only:

- Repository setup.
- Basic documentation.
- Data boundary planning.
- Environment configuration.
- Future sample data format planning.

The current phase does not include:

- Real data import.
- Retrieval.
- Agent answer generation.
- Embeddings.
- A vector database.
- A frontend.
- Deployment.

## Possible Later Stages

After V0, later stages may consider:

- A better data schema.
- More data sources.
- More reliable retrieval.
- Better source citation.
- Improved answer evaluation.
- UI improvements.
- Public deployment hardening.

These are later-stage possibilities, not V0 requirements.
