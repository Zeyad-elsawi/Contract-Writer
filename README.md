![Uploading Screenshot 2025-09-15 150351.png…]()

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
Excerpt from a generated consulting contract 

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
v. Providing training and technical support to Company's employees.
vi. Generating reports and analyses as requested by Company.
vii. Providing input on Company's operational processes and procedures.
viii. Providing guidance on company policies, procedures, and guidelines.
ix. Providing assistance in the development of Company's brand identity and messaging.
x. Any other services required by Company in connection with Company's business operations.

b. Consultant represents and warrants that:
i. It has the necessary qualifications, experience, and expertise to perform the services set forth in this Consulting Contract.
ii. It will conduct itself in a professional and courteous manner at all times while working with Company.
iii. It will use commercially reasonable efforts to perform the services set forth in this Consulting Contract in a timely and efficient manner.

2. SCOPE OF SERVICES

a. Consultant agrees to perform the services set forth in this Consulting Contract during the term of this Agreement, which begins on [INSERT DATE] and ends on [INSERT DATE].

b. Consultant shall provide services to Company in accordance with the specifications outlined in the attached Service Sheet.

c. Consultant shall have no obligation to provide services beyond the scope described in this section.

d. Consultant may request additional services, including but not limited to specialized services or consultancy, at any time during the term of this Agreement upon mutually agreed upon terms and conditions.

3. COMPENSATION

a. Consultant shall receive an hourly rate of [INSERT HOURLY RATE] per hour for each service rendered.

b. Consultant shall be responsible for all expenses associated with performing the services under this Agreement, including travel, lodging, and meals.

c. Consultant shall be entitled to receive reimbursement for any expenses incurred in connection with the performance of the services.

4. CONFIDENTIALITY

a. During the term of this Agreement, Consultant shall maintain the confidentiality of all information obtained in connection with the services provided to Company.

b. Consultant shall not disclose any information obtained during the course of this Agreement to any third party except as required by law or in connection with the performance of this Agreement.

c. Consultant shall take all reasonable steps to protect against unauthorized disclosure or misuse of confidential information.

5. INTELLECTUAL PROPERTY

a. All intellectual property rights arising out of the services performed by Consultant shall belong exclusively to Company.

b. Consultant shall have no right to distribute, sell, license, transfer, or otherwise dispose of any intellectual property rights owned or controlled by Company.

c. Consultant shall promptly notify Company of any unauthorized use or misappropriation of intellectual property rights.

6. TERMINATION

a. Either party may terminate this Agreement immediately in the event of breach by the other party.

b. Upon termination of this Agreement, Consultant shall immediately cease providing services to Company.

c. Consultant shall provide written notice to Company of any intent to terminate this Agreement.

7. LIABILITY

a. Consultant shall indemnify and hold harmless Company from and against any claims, damages, liabilities, losses, or expenses arising out of or in connection with the performance of the services under this Agreement.

b. Consultant shall defend and indemnify Company against any claim brought against Company by any third party arising out of or in connection with the services provided by Consultant.

c. If Consultant is found liable for any claim, Consultant shall pay all costs, including reasonable attorneys' fees, arising out of or in connection with the claim.

8. GOVERNING LAW

a. This Agreement shall be governed by and construed in accordance with the laws of [Specify Country/State].

b. Any disputes arising out of or relating to this Agreement shall be resolved through binding arbitration in accordance with the rules of the American Arbitration Association.

Closing:

I, ____________________________, hereby sign and date this Consulting Contract on ______________________ (date).

Consultant:

Name: ____________________________
Title: _____________________________
Address: ___________________________
City, State ZIP Code: ___________________
Phone Number: ______________________
Email Address: ______________________

Company:

Name: ____________________________
Title: _____________________________
Address: ___________________________
City, State ZIP Code: ___________________
Phone Number: ______________________
Email Address: ______________________
```

