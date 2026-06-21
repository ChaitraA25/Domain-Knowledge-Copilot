from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
#  - model returns NumPy array tolist converts to list which is easier to store in ChromaDB.

def generate_embedding(text:str):
    return model.encode(text).tolist()
