from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
import re
from fpdf import FPDF


from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema.runnable import RunnablePassthrough
# from langchain.schema.prompt_template import format_document
from langchain.schema import StrOutputParser


# in ./backend/ run command -->  .venv\Scripts\Activate
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.80)


embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", task_type="retrieval_document")

loader = DirectoryLoader('./documents/' ,glob='./*.txt', loader_cls=TextLoader)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

vectorstore = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory="./chroma_db")
vectorstore_disk = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

retriever = vectorstore_disk.as_retriever(search_kwargs={"k": 1})

# If > 0, document context is being captured
test_retrieve = len(retriever.get_relevant_documents("Amazon"))

# format document
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# llm_prompt_template = """You are an assistant for question-answering tasks.
# Use the following context to recommend 10 credit cards and provide descriptions and their links. 
# Question: {question} \nContext: {context} \nAnswer:"""

llm_prompt_template = """
You are a highly capable assistant designed to provide credit card recommendations based on specific user inquiries, using a pre-defined list of credit cards from the context. Each card has unique benefits and URLs provided. Match these cards to the user's needs based on their question, emphasizing how each recommended card suits these needs.

Question: {question}
Context Data: {context}

Analyze the details in the 'Context Data' and select up to 10 credit cards from the context data that best answer the user's question. Provide a brief description and URL for each card, clearly explaining why each card is suited for the user's requirements. List your recommendations below:
Answer:
"""


llm_prompt = PromptTemplate.from_template(llm_prompt_template)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | llm_prompt | llm | StrOutputParser()
)

# Test response
resp = rag_chain.invoke("What is the 5/24 rule?")


# Routes
@app.route("/")
def hello_world():
    return f"<p>{resp}</p><p>Text length is: {len(texts)}</p>"


@app.route('/api/receive-transactions', methods=['POST'])
def receive_transactions():
    transactions = request.json
    pdf_path = './transactionData/transactions.pdf'

    # Check if the PDF already exists
    if not os.path.exists(pdf_path):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for transaction in transactions:
            pdf.cell(200, 10, txt=f"Date: {transaction['date']} Amount: {transaction['amount']} Description: {transaction['description']}", ln=True)

        if not os.path.exists('./transactionData'):
            os.makedirs('./transactionData')

        pdf.output(pdf_path)

    # Load and split PDF
    loader = PyPDFLoader("./transactionData/transactions.pdf")
    pages = loader.load_and_split()
    combined_pages = " ".join(page.page_content for page in pages)


    llm_prompt_template = """
    The following question contains transaction data contains fields (Date, Amount, Description) and the 'Context Data' contains credit cards with fields (credit card name, description, rating, link). Based on the user's question, utilize these pieces of data to recommend credit cards from the 'Context Data'. 

    Question: {question}
    Context Data: {context}

    Analyze the details in the 'Context Data' and select up to 10 credit cards from the 'Context Data' that best answer the user's question. Provide a brief description and URL for each card, clearly explaining why each card is suited for the user's requirements. List the recommendations below and do not respond with anything else:
    Answer:
    """
    # llm_prompt = PromptTemplate.from_template(llm_prompt_template)

    rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | llm_prompt | llm | StrOutputParser()
    )

    resp = rag_chain.invoke(f"Use the following transaction data to determine what are the 5 best credit cards based on the description of the purchases and the total costs: {combined_pages}")

    return jsonify({'valid': True, 'response': resp})


if __name__ == "__main__":
    app.run(debug=True)