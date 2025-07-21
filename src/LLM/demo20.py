from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import Chroma
from langchain_community.vectorstores import DocArrayInMemorySearch


texts = ["Metin 1", "Metin 2", "Metin 3"]

embeddings = OpenAIEmbeddings()

vector_store_faiss = FAISS.from_texts(texts, embeddings)
vector_store_chroma = Chroma.from_texts(texts, embeddings)
vector_store_docarray = DocArrayInMemorySearch.from_texts(texts, embeddings)

results_faiss = vector_store_faiss.similarity_search("Metin", k=2)
results_chroma = vector_store_chroma.similarity_search("Metin", k=2)
results_docarray = vector_store_docarray.similarity_search("Metin", k=2)

print(results_faiss)
print(results_chroma)
print(results_docarray)
