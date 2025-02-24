# MediBuddy RAG System

A Retrieval-Augmented Generation (RAG) system specialized for UK medical information, built using Milvus vector database. This system enhances Large Language Model (LLM) responses with accurate, context-specific medical information from trusted UK healthcare sources.

## Features

- Vector database storage for medical documents using Milvus
- Document embedding pipeline for efficient information retrieval
- REST API for seamless integration with LLM systems
- Specialized for UK healthcare context
- Built-in document processing and chunking
- Configurable similarity search parameters

## Prerequisites

- Python 3.8+
- Docker and Docker Compose
- At least 4GB of available RAM
- Adequate storage space for document embeddings

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/medibuddy-rag.git
cd medibuddy-rag
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root with the following variables:
```env
MILVUS_URL=http://localhost:19530
```

2. Adjust the `config.py` file for custom settings:
- Document processing parameters
- Vector dimension settings
- Similarity search thresholds
- API configuration

## Usage

1. Start the Milvus server:
```bash
docker-compose up -d
```

2. Process and embed documents:
```bash
python embed.py process_documents
```

3. Start the API server:
```bash
python api.py
```

The API will be available at `http://localhost:8000`.

## API Endpoints

### Query Endpoint
```
GET /query?collection=Diabetes&q=What are the NHS guidelines for diabetes management?
```

## Document Structure

Place your medical documents in the `docs` directory. Supported formats:
- PDF (.pdf)
- Text (.txt)
- Word (.docx)
- Powerpoint (.pptx)