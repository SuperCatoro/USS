# Layer 3 — Diagnostic Engine (Fact API)

The Diagnostic Engine performs deterministic classification using a TF-IDF + Logistic Regression model.

- F1 Score: 0.71902 on 19,375-row validation.
- Cost: ~$0.00004 per message.
- Produces Structured Facts using an explainability-native interpretability model.
- Fully reproducible: same input → same output.

This layer provides the auditable factual basis for all policy decisions.
