from fastapi import FastAPI, UploadFile
from backend.pdf_reader import extract_text
from backend.risk_engine import (
    detect_risks,
    calculate_score,
    extract_risky_clauses
)
from backend.ai_risk_detector import analyze_clause

app = FastAPI()

@app.post("/upload")
async def upload_contract(file: UploadFile):

    content = await file.read()

    with open(file.filename, "wb") as f:
        f.write(content)

    text = extract_text(file.filename)

    found_risks = detect_risks(text)

    risk_score = calculate_score(found_risks)

    risky_clauses = extract_risky_clauses(text)

    ai_analysis = []

    for clause in risky_clauses:

        result = analyze_clause(clause)

        ai_analysis.append({
            "clause": clause,
            "risk_type": result["risk_type"],
            "confidence": result["confidence"]
        })

    return {
        "filename": file.filename,
        "risks_found": found_risks,
        "risk_score": risk_score,
        "risky_clauses": risky_clauses,
        "ai_analysis": ai_analysis
    }
