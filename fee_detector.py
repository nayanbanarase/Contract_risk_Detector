fee_words = [
    "service charge",
    "processing fee",
    "late fee",
    "additional fee"
]

def detect_fees(text):

    found = []

    for fee in fee_words:

        if fee in text.lower():
            found.append(fee)

    return found
