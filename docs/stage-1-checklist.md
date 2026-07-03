# Stage 1 Checklist

## Purpose

This checklist defines what must be true before Lithos Mind can close the Project Initialization Phase and move toward the next stage.

The purpose of Stage 1 is not to build agent functionality. It is to make the repository structure, product boundary, data policy, and initial data source assumptions clear and reviewable.

## Stage 1 Goal

Stage 1 is complete when the repository clearly documents:

- What Lithos Mind is.
- What Lithos Mind is not.
- What the future V0 may include.
- What data is allowed or disallowed.
- How the `data/` directory should be used.
- How the Lithos repository may be treated as a future YAML-only data source.
- What must remain out of scope before real implementation begins.

## Repository Foundation

- [ ] `README.md` exists and explains the project positioning.
- [ ] `AGENTS.md` exists and defines Codex execution rules.
- [ ] `.gitignore` exists and excludes local environment files, cache files, build outputs, and future local data directories.
- [ ] `.env.example` exists and contains only placeholder environment variable names.
- [ ] `.gitattributes` exists and defines consistent line ending behavior.
- [ ] No real API keys, credentials, private configuration, or local environment files are committed.

## Product Documentation

- [ ] `docs/product-vision.md` exists and describes the long-term product direction.
- [ ] `docs/v0-scope.md` exists and separates future V0 goals from the current initialization phase.
- [ ] The documents clearly state that current-stage work does not include Agent implementation, RAG, embeddings, frontend, backend, or deployment.
- [ ] The project is positioned as a personal AI product management portfolio project, not a production-ready system.

## Data Boundary

- [ ] `docs/data-policy.md` exists and defines allowed and disallowed data types.
- [ ] The project is limited to public-safe personal data.
- [ ] Private messages, emails, financial records, medical records, credentials, private schedules, and other sensitive personal data are explicitly excluded.
- [ ] Sample data rules are documented.
- [ ] Codex is instructed not to invent sample records that pretend to be the user's real data.

## Data Directory

- [ ] `data/README.md` exists and explains the purpose of the `data/` directory.
- [ ] `data/samples/lithos-item-template.json` exists.
- [ ] The data template contains only a minimal YAML-only structure.
- [ ] No real data is committed in the current stage.
- [ ] No raw data, cleaned data, vector database files, or generated data artifacts are committed.

## Lithos Data Source Boundary

- [ ] `docs/lithos-data-source.md` exists.
- [ ] Lithos is documented as a future data source for Lithos Mind.
- [ ] Only YAML frontmatter from Lithos work cards is in scope for the current data source boundary.
- [ ] Markdown body content is explicitly excluded.
- [ ] Markdown body content must not be imported, indexed, embedded, summarized, or otherwise processed in the current stage.
- [ ] `data/samples/lithos-item-template.json` reflects the YAML-only boundary.

## Out of Scope for Stage 1

Stage 1 must not include:

- [ ] Real data import.
- [ ] Data extraction scripts.
- [ ] Data cleaning pipelines.
- [ ] Embedding generation.
- [ ] Vector database creation.
- [ ] Retrieval implementation.
- [ ] Agent answer generation.
- [ ] Frontend implementation.
- [ ] Backend implementation.
- [ ] API implementation.
- [ ] Deployment configuration.
- [ ] Private or sensitive data processing.

## Stage 1 Exit Criteria

Stage 1 can be considered complete when:

- [ ] The repository has a clear project identity.
- [ ] The current phase is clearly separated from future V0 implementation.
- [ ] The data policy is documented.
- [ ] The Lithos YAML-only data source boundary is documented.
- [ ] The sample data template exists and contains no real or fictional data.
- [ ] No implementation work has started prematurely.
- [ ] The repository is clean, readable, and safe to review on GitHub.

## Suggested Next Stage

After Stage 1 is closed, the next stage may focus on a minimal local YAML extraction prototype.

That future stage should still remain narrow:

- Read Lithos work cards locally.
- Extract YAML frontmatter only.
- Exclude Markdown body content.
- Output a small structured local result for review.
- Avoid embeddings, RAG, Agent logic, frontend, backend, and deployment until later stages.
