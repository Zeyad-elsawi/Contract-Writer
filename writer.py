

import os
import streamlit as st
from langchain_community.document_loaders import UnstructuredWordDocumentLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

# -------------------------------
# Streamlit title
st.title("Contract Generator (TinyLlama)")

# -------------------------------
# Paths
MODEL_PATH = "./models/tinyllama-1.1b-chat"  
os.environ["HF_HUB_OFFLINE"] = "1" 
os.environ["TRANSFORMERS_CACHE"] = "./hf_cache"  

# -------------------------------
# Step 0: Contract type
contract_type = st.selectbox(
    "Select Contract Type", 
    ["Consulting Contract", "Confidentiality Agreement", "Consignment Agreement"]
)

contract_files = {
    "Consulting Contract": [
        "consulting-contract-template-37.docx",
        "consulting-contract-template-38.docx",
        "consulting-contract-template-41.docx",
        "consulting-contract-template-42.docx",
        "consulting-contract-template-43.docx",
        "consulting-contract-template-44.docx",
    ],
    "Confidentiality Agreement": [
        "confidentiality-statement-01.docx",
        "confidentiality-statement-02.docx",
        "confidentiality-statement-03.docx",
        "confidentiality-statement-04.docx",
        "confidentiality-statement-05.docx",
    ],
    "Consignment Agreement": [
        "Consignment-Agreement-Template.docx"
    ]
}



# -------------------------------
# Step 1: Load templates
documents = []
for file in contract_files[contract_type]:
    if os.path.exists(file):
        loader = UnstructuredWordDocumentLoader(file)
        documents.extend(loader.load())

# -------------------------------
# Step 2: Split into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
docs = text_splitter.split_documents(documents)

# -------------------------------
# Step 5: User input
st.header("Enter Contract Details")

col1, col2 = st.columns(2)

with col1:
    company = st.text_input("Company Name")
    company_address = st.text_area("Company Address")
    employee = st.text_input("Second Party Name")
    employee_role = st.selectbox(
        "Second Party Role", 
        ["Consultant", "Independent Contractor", "Employee", "Service Provider", "Other"]
    )
    if employee_role == "Other":
        employee_role = st.text_input("Specify Role")

with col2:
    start_date = st.date_input("Start Date")
    end_date = st.date_input("End Date")
    jurisdiction_country = st.text_input("Country/State for Jurisdiction")
    jurisdiction = f"The laws of {jurisdiction_country}" if jurisdiction_country else "The laws of [Specify Country/State]"

st.subheader("Contract Terms")
contract_value = st.text_input("Contract Value (if applicable)")
payment_terms = st.text_input("Payment Terms")
termination_clause = st.text_area("Special Termination Conditions (optional)")

# -------------------------------
# Step 7: Generate contract
if st.button("Generate Contract"):
    with st.spinner("Loading TinyLlama and generating contract..."):
        # Embeddings + FAISS
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True}
        )
        if docs:
            vectorstore = FAISS.from_documents(docs, embeddings)
            query = f"{contract_type} agreement template clauses terms"
            retrieved_docs = vectorstore.similarity_search(query, k=3)
            context_text = "\n\n".join([doc.page_content for doc in retrieved_docs])
        else:
            context_text = "Standard contract template"

        
        reference_block = f"""
Reference excerpts (for style/clauses guidance only; do not copy verbatim):
{context_text[:1200]}
""".strip()

        # Load TinyLlama
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            local_files_only=True,
            torch_dtype=torch.float32
        )
        generator = pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            device=-1
        )

        
        prompt_template = f"""
Write a complete and formal {contract_type} in English legal language.
The contract must be well-structured, numbered, and professional.

Insert the provided details directly into the contract:

- Company: {company}
- Address: {company_address if company_address else '[Company Address]'}
- Second Party: {employee}
- Role: {employee_role}
- Contract Period: {start_date} to {end_date}
- Governing Law: {jurisdiction}
- Contract Value: {contract_value if contract_value else 'As specified in Schedule A'}
- Payment Terms: {payment_terms if payment_terms else 'As agreed between parties'}
- Special Termination: {termination_clause if termination_clause else 'Standard termination applies'}

Use the following reference excerpts from uploaded templates to guide structure, clause wording, and style (do not copy verbatim; adapt to fit the details above):

{reference_block}

The contract MUST contain the following sections, in order:

1. Parties
2. Purpose
3. Scope of Services
4. Compensation
5. Confidentiality
6. Intellectual Property
7. Termination
8. Liability
9. Governing Law
10. Signatures

Ensure all sections are written in clear and formal contract language.
Do not leave placeholder text like [Insert here]. Write full clauses.
CONTRACT:
"""

        raw_output = generator(
            prompt_template,
            max_new_tokens=2000,
            do_sample=True,
            temperature=0.6,
            top_p=0.9,
            repetition_penalty=1.1,
            pad_token_id=generator.tokenizer.eos_token_id,
            eos_token_id=generator.tokenizer.eos_token_id
        )[0]["generated_text"]

        # Extract only the contract part
        if "CONTRACT:" in raw_output:
            output = raw_output.split("CONTRACT:")[-1].strip()
        else:
            output = raw_output

        st.subheader("Generated Contract")
        st.text_area("Contract Text", output, height=600)
        st.download_button("Download Contract", output, file_name="generated_contract.txt")
