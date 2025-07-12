import chromadb
from chromadb.utils import embedding_functions

embedding_fn = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="book_versions", embedding_function=embedding_fn)

def save_version(text, version_id):
    collection.add(documents=[text], ids=[version_id], metadatas=[{"version": version_id}])

def semantic_search(query, n=2):
    return collection.query(query_texts=[query], n_results=n)