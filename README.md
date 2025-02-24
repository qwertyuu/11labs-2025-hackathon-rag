# RAG part of Medibuddy

install dependencies with `pip install -r requirements.txt`

run the docker-compose using `docker-compose up -d`

Then run `python embed.py process_documents` to embed the documents to the Milvus vector database

Then run `python api.py` to start listening for queries from your LLM