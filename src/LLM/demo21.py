from langchain_openai import OpenAIEmbeddings


embeddings_default = OpenAIEmbeddings()
embeddings_small = OpenAIEmbeddings(model="text-embedding-3-small")  # 1536 boyut
embeddings_large = OpenAIEmbeddings(model="text-embedding-3-large")  # 3072 boyut

embeddings = embeddings_default

kedi_vector = embeddings.embed_query("Kedi")
kopek_vector = embeddings.embed_query("Köpek")

print("=== OpenAI Embeddings ===")
print(f"Kedi vektör boyutu: {len(kedi_vector)}")  # 1536
print(f"Köpek vektör boyutu: {len(kopek_vector)}")  # 1536
print(f"\nKedi vektörü (ilk 5): {kedi_vector[:5]}")
print(f"Köpek vektörü (ilk 5): {kopek_vector[:5]}")
# print(f"Kedi vektörü (ilk 5): {kedi_vector[:5]}")
# print(f"Köpek vektörü (ilk 5): {kopek_vector[:5]}")
# print(f"Benzerlik: {cosine_similarity([kedi_vector], [kopek_vector])[0][0]:.3f}\n")
