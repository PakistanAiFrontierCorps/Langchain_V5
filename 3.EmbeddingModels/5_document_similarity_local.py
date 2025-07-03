from langchain_community.embeddings import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
from dotenv import load_dotenv
import numpy as np

load_dotenv()

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Pakistan was established on August 14, 1947, following the partition of British India.",
    "Islamabad is the capital city of Pakistan, while Karachi is its largest city and economic hub.",
    "The official language of Pakistan is Urdu, but English is widely used for official and business purposes.",
    "Pakistan is home to the world's second-highest mountain, K2, located in the Karakoram range.",
    "Cricket is the most popular sport in Pakistan, and the national team won the ICC Cricket World Cup in 1992.",
]

query = 'tell me about Urdu'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query) 

scores = cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]

print("Query:", query)
print("Best Match:", documents[index])
print("Similarity Score:", score)
