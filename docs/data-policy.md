# Data Policy

## Purpose

This document defines the data boundary for Lithos Mind. The policy aims to:

- Keep the project public-data-first.
- Reduce privacy risk.
- Make the project safe to review and demonstrate.
- Prevent accidental inclusion of sensitive personal data.

## Public-Data-First Principle

Lithos Mind should only use public-safe personal data. Public-safe personal data means:

- Data that the project owner intentionally considers safe for a public or portfolio demo.
- Data that does not expose private communication, sensitive identity information, credentials, financial records, medical records, or other private records.
- Data that can be reviewed, cited, or demonstrated without harming privacy.

## Allowed Data Types

Allowed data types include:

- Public learning notes.
- Public reading records.
- Public cultural collections.
- Public long-term interest logs.
- Public-safe article notes.
- Public-safe book notes.
- Public-safe personal knowledge cards.
- Public-safe manually prepared sample records.

Allowed data should still be reviewed before it is committed to the repository.

## Disallowed Data Types

Lithos Mind must not process or store:

- Private messages.
- Chat history from private conversations.
- Emails.
- Financial records.
- Medical records.
- Account credentials.
- Passwords or API keys.
- Government IDs or identity documents.
- Phone numbers.
- Home addresses.
- Private schedules or calendar records.
- Private work documents.
- Confidential company information.
- Sensitive personal data.

## Sample Data Rules

- Sample data must come from user-provided public-safe data or remain as empty templates.
- Codex must not invent sample records that pretend to be the user's real notes, reading records, cultural collections, or interest logs.
- If no user-provided public-safe data is available, only data templates should be created.
- If the safety of a data item is unclear, it should not be committed.
- Fictional placeholder text may only be used inside templates when clearly marked as placeholder content.

## Source Traceability

Future data records should preserve source information where possible, including:

- Source name.
- Source URL, if available.
- Creation date or collection date.
- Data type.
- Tags.
- Visibility or public-safety status.

Source traceability is important for future retrieval and source citation.

## Repository Data Rules

- Do not commit raw private data.
- Do not commit API keys or credentials.
- Do not commit local vector databases.
- Do not commit unreviewed raw data.
- Keep raw, cleaned, and vector database directories local unless explicitly reviewed and approved.
- Use `.gitignore` to protect local data directories.

## Current Stage Boundary

The current **Project Initialization Phase** includes only:

- Data policy definition.
- Future sample data format planning.
- Public-safe data boundary clarification.

The current phase does not include:

- Real data ingestion.
- A data cleaning pipeline.
- Embedding generation.
- Vector database creation.
- Retrieval implementation.
- Agent answer generation.

## Review Checklist

Before importing data, review the following questions:

- [ ] Is this data intentionally public-safe?
- [ ] Does it contain private messages, emails, financial, medical, or credential information?
- [ ] Can this data be shown in a public demo?
- [ ] Is the source clear?
- [ ] Should this data be committed, kept local, or excluded?
