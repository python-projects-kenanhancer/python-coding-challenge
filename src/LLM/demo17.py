from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Create documents directly (no file needed)
documents = [
    Document(
        page_content="""
        VACATION POLICY: All full-time employees are entitled to 20 days of paid time off (PTO) per year.
        PTO accrues at a rate of 1.67 days per month. Unused PTO can be carried over to the next year,
        up to a maximum of 30 days.
        """,
        metadata={"section": "vacation", "policy": "time_off"},
    ),
    Document(
        page_content="""
        SICK LEAVE: Employees receive 10 days of sick leave per year, separate from PTO.
        Sick leave does not carry over to the next year. Doctor's notes are required for
        absences longer than 3 consecutive days.
        """,
        metadata={"section": "sick_leave", "policy": "time_off"},
    ),
    Document(
        page_content="""
        REMOTE WORK: Employees may work remotely up to 3 days per week with manager approval.
        Full remote work requires special authorization from HR. All remote workers must be
        available during core hours (10 AM - 3 PM EST).
        """,
        metadata={"section": "remote_work", "policy": "work_arrangements"},
    ),
    Document(
        page_content="""
        EXPENSES: Business expenses must be submitted within 30 days with receipts.
        Per diem for travel: $50 for meals, $200 for lodging. Company credit cards are
        available for employees who travel frequently.
        """,
        metadata={"section": "expenses", "policy": "reimbursement"},
    ),
]

# Split documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Create embeddings and vector store
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector_store = Chroma.from_documents(
    documents=chunks, embedding=embeddings, persist_directory="./policy_db"
)

# Create retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# Create LLM
llm = ChatOllama(
    model="llama4",  # Changed from llama4
    temperature=0.7,
)

# Create prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that answers questions about company policies based on the provided context.",
        ),
        (
            "human",
            """Answer the question based only on the following context:

Context:
{context}

Question: {question}

Answer:""",
        ),
    ]
)


# Define a function to format documents
def format_docs(docs):
    return "\n\n".join(
        f"Content: {doc.page_content}\nMetadata: {doc.metadata}" for doc in docs
    )


# Create the LCEL chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# Test it
questions = [
    "How many vacation days do I get?",
    "Can I work from home?",
    "What's the meal allowance for travel?",
    "Do sick days carry over?",
]

for question in questions:
    print(f"\nQ: {question}")
    answer = rag_chain.invoke(question)
    print(f"A: {answer}")
