import faiss
import pickle
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("vector_store/faiss_index.pkl", "rb") as f:
    index, docs = pickle.load(f)

def rag_node(state):
    query = state["query"]
    embedding = model.encode([query])
    _, I = index.search(np.array(embedding), k=3)
    retrieved_docs = " ".join([docs[i] for i in I[0]])
    return {"query": query, "info": retrieved_docs}