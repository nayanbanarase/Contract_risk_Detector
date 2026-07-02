import streamlit as st
import requests

st.title("📄 AI Contract Risk Detector")

uploaded_file = st.file_uploader(
    "Upload Contract PDF",
    type=["pdf"]
)

if uploaded_file:

    files = {
        "file": uploaded_file
    }

    response = requests.post(
        "http://127.0.0.1:8000/upload",
        files=files
    )

    result = response.json()

    st.success("Analysis Complete!")

    st.write("Filename:", result["filename"])
    st.write("Risks Found:", result["risks_found"])
    st.write("Risk Score:", result["risk_score"])
    st.subheader("⚠️ Risky Clauses Found")

    for clause in result["risky_clauses"]:
       st.warning(clause)
