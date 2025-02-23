import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, UnstructuredExcelLoader, UnstructuredPowerPointLoader
from dotenv import load_dotenv
from pymilvus import MilvusClient
from langchain_milvus import Milvus
import fire
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

client = None

EMBED_MODEL_ID = "sentence-transformers/all-MiniLM-L6-v2"

class Main:
    @staticmethod
    def process_documents(root_dir= "./docs"):
        # Dictionary mapping file extensions to their respective loaders
        loaders = {
            '.pdf': PyPDFLoader,
            '.docx': Docx2txtLoader,
            '.xlsx': UnstructuredExcelLoader,
            '.pptx': UnstructuredPowerPointLoader
        }
        embedding = HuggingFaceEmbeddings(
            model_name=EMBED_MODEL_ID
        )
        
        # Walk through all directories
        for dirpath, dirnames, filenames in os.walk(root_dir):
            print(f"\nProcessing directory: {dirpath}")
            
            # Process each file in the current directory
            for filename in filenames:
                file_path = Path(dirpath) / filename
                file_extension = file_path.suffix.lower()
                
                # Check if we have a loader for this file type
                if file_extension in loaders:
                    try:
                        print(f"Loading {filename}")
                        loader = loaders[file_extension](str(file_path))
                        documents = loader.load()
                        print(f"Successfully processed {filename}, extracted {len(documents)} pages/documents")

                        collection = dirpath.replace("\\", "/").split("/")[-1]

                        print(f"Embedding {filename} in the collection {collection}")
                        Milvus.from_documents(
                            documents,
                            embedding,
                            collection_name=collection,
                            connection_args={"uri": os.getenv("MILVUS_URI")},
                        )
                    except Exception as e:
                        print(f"Error processing {filename}: {str(e)}")
                else:
                    print(f"No loader available for {filename}")
        
    @staticmethod
    def drop_collection(collection):
        client.drop_collection(collection)
        print(f"Collection {collection} dropped")
        
    @staticmethod
    def list_collections():
        collections = client.list_collections()
        print(f"Available collections: {collections}")
        

# Usage example
if __name__ == "__main__":
    load_dotenv()
    client = MilvusClient(uri=os.getenv("MILVUS_URI"))
    fire.Fire(Main)