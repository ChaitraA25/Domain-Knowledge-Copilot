import chromadb 
#PersistentClient- To save the vector to disk
client= chromadb.PersistentClient(path="chroma_db")

collection=client.get_or_create_collection(name="documents")