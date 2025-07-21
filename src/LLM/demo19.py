from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.documents import Document

from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# Document creation remains the same...
documents = [
    Document(
        page_content="""
    VACATION POLICY: All full-time employees are entitled to 20 days of paid time off (PTO) per year. 
    PTO accrues at a rate of 1.67 days per month. Unused PTO can be carried over to the next year, 
    up to a maximum of 30 days.
    """,
        metadata={"section": "vacation", "policy": "time_off"},
    ),
    # ... other documents
]

# Splitting and vector store setup are also the same...
text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
chunks = text_splitter.split_documents(documents)
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vector_store = Chroma.from_documents(documents=chunks, embedding=embeddings)

# 1. Create a retriever
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 2. Create the LLM
llm = ChatOllama(
    model="llama4",
    temperature=0.7,
)

# 3. Create a prompt template
# This step gives you explicit control over the prompt sent to the LLM.
prompt = ChatPromptTemplate.from_template(
    """
Answer the user's question based only on the following context:

<context>
{context}
</context>

Question: {input}
"""
)

# 4. Create the main chain
# First, a chain to combine documents
document_chain = create_stuff_documents_chain(llm, prompt)

# Then, the retrieval chain that combines the retriever and the document chain
retrieval_chain = create_retrieval_chain(retriever, document_chain)


# 5. Test it
questions = [
    "How many vacation days do I get?",
    "Can I work from home?",
    "What's the meal allowance for travel?",
    "Do sick days carry over?",
]

for question in questions:
    print(f"\nQ: {question}")
    # Invoke the new chain with the 'input' key
    response = retrieval_chain.invoke({"input": question})
    # The answer is in the 'answer' key of the response dictionary
    print(f"A: {response['answer']}")
    # You can also inspect the retrieved documents:
    # print(response['context'])
