## Contract Generator (TinyLlama 1.1B)
Generate well-structured consulting contracts using a lightweight local LLM (TinyLlama 1.1B). Fill in party names, dates, payment terms, and governing law; the app composes a complete contract using the provided consulting templates as style/structure references.

## What It Does
- **Input**: Company details, party information, contract terms, dates, payment terms, governing law
- **Output**: Complete, professional consulting contract with proper legal structure and numbering
- **Features**: Multiple contract types (Consulting, Confidentiality, Consignment), template-based generation, downloadable results

## How It Works
1. **Template Processing**: Loads and chunks consulting contract templates using LangChain's document loaders
2. **Vector Search**: Creates embeddings from templates and uses FAISS for similarity search to find relevant contract clauses
3. **Context Building**: Retrieves the most relevant template sections to guide the AI's writing style and structure
4. **AI Generation**: Uses TinyLlama 1.1B to generate a complete contract based on:
   - User-provided details (company, parties, dates, terms)
   - Retrieved template context for legal language and structure
   - Structured prompt ensuring all required sections are included
5. **Output Processing**: Extracts the generated contract text and provides it for display/download

## Model Used
- TinyLlama 1.1B Chat: [`TinyLlama/TinyLlama-1.1B-Chat-v1.0`](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0)

## Download Script
- `download_model.py` — downloads the model to `./models/tinyllama-1.1b-chat`

```bash
python download_model.py
```

## Consulting Contract Templates Used
- `consulting-contract-template-37.docx`
- `consulting-contract-template-38.docx`
- `consulting-contract-template-41.docx`
- `consulting-contract-template-42.docx`
- `consulting-contract-template-43.docx`
- `consulting-contract-template-44.docx`

## Quickstart
1) Install dependencies (Python 3.9+ recommended):

```bash
pip install streamlit transformers torch sentence-transformers faiss-cpu langchain-community unstructured
```

2) Download the model:

```bash
python download_model.py
```

3) Run the app:

```bash
streamlit run writer.py
```

## Usage
- Open the app in your browser (Streamlit will print the local URL)
- Select contract type (e.g., Consulting Contract)
- Enter company/party details, dates, payment terms, governing law
- Click Generate to produce the full contract and download the text

## Project Structure
- `writer.py` — Streamlit app
- `download_model.py` — model downloader
- `models/tinyllama-1.1b-chat/` — downloaded TinyLlama weights
- `consulting-contract-template-*.docx` — reference templates used for structure/style

## Sample Generated Contract
Excerpt from a generated consulting contract (full example saved at `c:\Users\Zeyad Elsawi\Downloads\generated_contract (2).txt`):

```text
This Consulting Contract ("Contract") is made and entered into by and between LINKTER ("Company"), located at [INSERT ADDRESS], ("Company") and LINKTER Consultants, LLC ("Consultant"), located at [INSERT ADDRESS], ("Consultant").

WHEREAS, Company desires to engage Consultant to perform certain services in connection with Company's business operations; and

WHEREAS, Consultant agrees to provide such services to Company in accordance with the terms and conditions set forth herein.

NOW, THEREFORE, in consideration of the mutual covenants and agreements contained herein, the parties agree as follows:

1. PURPOSE

a. This Consulting Contract sets forth the scope of services to be performed by Consultant, including but not limited to:
i. Providing research and analysis related to Company's products and services.
ii. Developing strategic plans and proposals.
iii. Reviewing and updating Company's marketing materials and presentations.
iv. Conducting market research and analysis.
```
