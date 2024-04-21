from flask import Flask
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.schema.runnable import RunnablePassthrough
# from langchain.schema.prompt_template import format_document
from langchain.schema import StrOutputParser


# in ./backend/ run command -->  .venv\Scripts\Activate
app = Flask(__name__)

load_dotenv()
api_key = os.getenv('GOOGLE_API_KEY')

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", temperature=0.85)

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", task_type="retrieval_document")

loader = DirectoryLoader('./documents/' ,glob='./*.txt', loader_cls=TextLoader)
documents = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
texts = text_splitter.split_documents(documents)

vectorstore = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory="./chroma_db" )
vectorstore_disk = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

retriever = vectorstore_disk.as_retriever(search_kwargs={"k": 1})

# If > 0, document context is being captured
test_retrieve = len(retriever.get_relevant_documents("lorem"))

# format document
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


llm_prompt_template = """You are an assistant for question-answering tasks.
Use the following context to recommend or reject credit cards. 
If the context doesn't contain an answer, provide an answer.
Question: {question} \nContext: {context} \nAnswer:"""

llm_prompt = PromptTemplate.from_template(llm_prompt_template)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | llm_prompt | llm | StrOutputParser()
)

# Test response
resp = rag_chain.invoke("What is the 5/24 rule? What cards should I avoid?")

@app.route("/")
def hello_world():
  return f"<p>{resp}</p><p>  text length is: {len(texts)}</p>"  
