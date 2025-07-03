from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "I love Pakistan",
    "Karachi was first capital of Pakistan",
    "Sindh is known as Bab-ul-Islam"
]

vector = embedding.embed_documents(documents)

print(str(vector))