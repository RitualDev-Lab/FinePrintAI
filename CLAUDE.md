# FinePrintAI

> In-memory, zero-cloud-cost legal contract, lease, and NDA scanner evaluating 60+ legal rules directly in the browser or terminal.

## Key Principles & Architecture
- **Zero Cloud Transmission**: All document parsing, regex pattern matching, and AST evaluation occur 100% locally in-memory. Zero document bytes are ever sent to remote AI inference APIs.
- **Rule Engine**: Evaluates contracts against 60+ legal rules across 6 critical vectors:
  1. Governing Law & Jurisdiction (one-sided forum selection)
  2. Uncapped Liability & Asymmetric Indemnification
  3. Automatic Renewal & Hidden Evergreen Clauses
  4. Broad Non-Compete & IP Assignment Overreach
  5. Unilateral Modification Rights
  6. Termination Penalties & Liquidated Damages
- **Redline Synthesizer**: Generates attorney-grade redline amendment clauses instantly for flagged risk items.

## Commands
- Run CLI: `npx @ritualdev/fineprint-ai scan ./contract.pdf`
- Live In-Browser Playground: https://ritualdev.in/fineprint
