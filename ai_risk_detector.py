from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

risk_labels = [
    "termination risk",
    "payment risk",
    "liability risk",
    "penalty risk",
    "confidentiality risk",
    "legal dispute risk"
]

def analyze_clause(clause):

    result = classifier(
        clause,
        risk_labels
    )

    return {
        "risk_type": result["labels"][0],
        "confidence": round(
            result["scores"][0] * 100,
            2
        )
    }
