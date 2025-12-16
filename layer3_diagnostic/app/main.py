from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Literal
from hashlib import sha256
from datetime import datetime, timezone


AgeStage = Literal["Child", "Teen", "Self-Selecting Early Career"]


class FactRequest(BaseModel):
    raw_text: str = Field(..., min_length=1)
    user_age_stage: AgeStage


class StructuredFact(BaseModel):
    persona_vector: str
    confidence_score: float
    flags: List[str]
    timestamp: str
    deterministic_hash: str


app = FastAPI(
    title="USS Fact API (Layer 3)",
    version="0.1.0",
    description="Deterministic diagnostic classification layer. Produces auditable structured facts only.",
)


@app.get("/health")
def health():
    return {"status": "ok", "layer": 3, "service": "fact-api", "version": "0.1.0"}


def deterministic_hash(raw_text: str, user_age_stage: str) -> str:
    payload = f"{user_age_stage}||{raw_text}".encode("utf-8")
    return sha256(payload).hexdigest()


@app.post("/v1/fact", response_model=StructuredFact)
def create_fact(req: FactRequest):
    # TRAINING STUB:
    # For now we return a deterministic placeholder classification based on the hash.
    h = deterministic_hash(req.raw_text, req.user_age_stage)

    # Simple deterministic “bucket” so output changes predictably with input
    bucket = int(h[:2], 16) % 13
 # TRAINING STUB that already matches Option 2 output style
labels = [f"persona_{i:02d}" for i in range(13)]

primary = labels[bucket]
# fake “passed labels”: always include primary, sometimes include a second one
passed = [primary]
if int(h[2:4], 16) % 4 == 0:
    passed.append(labels[(bucket + 1) % 13])

persona_vector = primary
flags = passed
confidence = 0.50


 return StructuredFact(
    persona_vector=persona_vector,
    confidence_score=confidence,
    flags=flags,
    timestamp=datetime.now(timezone.utc).isoformat(),
    deterministic_hash=h,
)
