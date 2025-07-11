import streamlit as st
import json
import google.generativeai as genai

# Load local knowledge base
with open("knowledge_base.json", "r", encoding="utf-8") as f:
    knowledge_base = json.load(f)

# Configure Gemini API
genai.configure(api_key="AIzaSyAEho69-SwcfSIy0WEWeQe0HGwsraXGJKg")

model = genai.GenerativeModel("gemini-1.5-flash")

# Streamlit app UI
st.title("Legal AI Assistant (BNS & BSA)")
st.write("Ask me questions related to Bharatiya Nyaya Sanhita (BNS), banking acts, or case summaries.")

question = st.text_input("Enter your legal question:")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Build context from knowledge base
        context_text = (
            "BNS: " + knowledge_base["bns"] + "\n\n"
            "BSA and Banking Acts: " + knowledge_base["bsa"] + "\n\n"
            "Case Summaries: " + "\n".join(knowledge_base["case_summaries"])
        )

        # Prepare prompt for Gemini
        prompt = f"""Answer the following legal question in detail, using the context below.

Context:
{context_text}

Question:
{question}
"""

        # Generate response
        response = model.generate_content(prompt)
        answer = response.text

        st.markdown("### Answer")
        st.write(answer)
