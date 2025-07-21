from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Step 1: Create documents
documents = [
    Document(
        page_content="""
        VACATION POLICY: All full-time employees are entitled to 20 days of paid time off (PTO) per year.
        PTO accrues at a rate of 1.67 days per month. Unused PTO can be carried over to the next year,
        up to a maximum of 30 days.
        """,
        metadata={"section": "vacation"},
    ),
    Document(
        page_content="""
        SICK LEAVE: Employees receive 10 days of sick leave per year, separate from PTO.
        Sick leave does not carry over to the next year. Doctor's notes are required for
        absences longer than 3 consecutive days.
        """,
        metadata={"section": "sick_leave"},
    ),
    Document(
        page_content="""
        REMOTE WORK: Employees may work remotely up to 3 days per week with manager approval.
        Full remote work requires special authorization from HR. All remote workers must be
        available during core hours (10 AM - 3 PM EST).
        """,
        metadata={"section": "remote_work"},
    ),
    Document(
        page_content="""
        EXPENSES: Business expenses must be submitted within 30 days with receipts.
        Per diem for travel: $50 for meals, $200 for lodging. Company credit cards are
        available for employees who travel frequently.
        """,
        metadata={"section": "expenses"},
    ),
]

# Step 2: Chunk documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)

# Step 3: Embeddings + Vector Store
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(
    documents=chunks, embedding=embeddings, persist_directory="./policy_db"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

# Step 4: LLM
llm = ChatOllama(model="llama4")

# Step 5: Compose RAG Chain
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | RunnableLambda(
        lambda x: f"Answer the question based on the context:\n\nContext:\n{x['context']}\n\nQuestion: {x['question']}"
    )
    | llm
    | StrOutputParser()
)

# Step 6: Ask questions
questions = [
    "How many vacation days do I get?",
    "Can I work from home?",
    "What's the meal allowance for travel?",
    "Do sick days carry over?",
]

for q in questions:
    print(f"\nQ: {q}")
    answer = rag_chain.invoke(q)
    print(f"A: {answer}")
