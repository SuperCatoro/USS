# Layer 3 — Diagnostic Engine (Fact API)

The Diagnostic Engine performs deterministic classification using a TF-IDF + Logistic Regression model.

- F1 Score: 0.71902 on 19,375-row validation.
- Cost: ~$0.00004 per message.
- Produces Structured Facts using an explainability-native interpretability model.
- Fully reproducible: same input → same output.

This layer provides the auditable factual basis for all policy decisions.

## Fact API – v0.1 (Training Stub)

This layer performs diagnostic classification only.
It does not apply policy, moderation, or enforcement.

### Input
- raw_text: string
- user_age_stage: enum (Child, Teen, Self-Selecting Early Career)

### Output (Structured Fact)
- persona_vector: one of 13 diagnostic categories
- confidence_score: float (0–1)
- flags: list of diagnostic markers
- timestamp
- deterministic_hash

### Guarantees
- Same input always produces the same output
- No policy logic exists in this layer
- Output is auditable and replayable


## Run locally (training stub)

From the repo root:

```bash
pip install -r layer3_diagnostic/requirements.txt
uvicorn layer3_diagnostic.app.main:app --reload
