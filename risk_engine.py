risk_words = [
    "penalty",
    "termination",
    "liability",
    "indemnity",
    "lawsuit",
    "fine"
]

def detect_risks(text):

    found = []

    for word in risk_words:

        if word in text.lower():
            found.append(word)

    return found
risk_scores = {

"penalty":10,
"liability":20,
"termination":15,
"indemnity":20,
"lawsuit":25
}
def calculate_score(found_risks):

    total = 0

    for risk in found_risks:
        total += risk_scores[risk]

    return total
import re

def extract_risky_clauses(text):

    clauses = re.split(r'[.!?]', text)

    risky_clauses = []

    for clause in clauses:

        for word in risk_words:

            if word.lower() in clause.lower():

                risky_clauses.append(clause.strip())

                break

    return risky_clauses
