import os
from typing import Union
from fastapi import FastAPI
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_milvus import Milvus
from dotenv import load_dotenv


load_dotenv()
# Configuration
EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"

app = FastAPI()

# Création des embeddings
embedding = HuggingFaceEmbeddings(
    model_name=EMBED_MODEL_ID,
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/query")
def query(q: Union[str, None] = None, collection: str = "hackathon"):
    if q is None:
        return {"result": []}
    vector_store_saved = Milvus(
        embedding,
        collection_name=collection,
        connection_args={"uri": os.getenv("MILVUS_URI")},
    )
    res = vector_store_saved.search(
        query=q,
        search_type="similarity",
    )

    return {"result": [hit.page_content for hit in res]}
