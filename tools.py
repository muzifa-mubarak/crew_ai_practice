# tools.py

'''from embedchain import App
import chromadb.utils.embedding_functions as embedding_functions

# Initialize HuggingFace embedding function for ChromaDB
huggingface_ef = embedding_functions.HuggingFaceEmbeddingFunction(
    api_key="",  # No API key required for sentence-transformers models
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create EmbedChain app using Chroma-compatible embeddings
app = App(embedding_model=huggingface_ef)

# Example: load a YouTube tool
from crewai_tools import YoutubeChannelSearchTool

yt_tool = YoutubeChannelSearchTool(
    config={"app": app}
)'''
from embedchain import App
import chromadb.utils.embedding_functions as ef

# Create a HuggingFace / ONNX MiniLM embedding function (runs locally)
local_embedding = ef.ONNXMiniLM_L6_V2()

# Initialize App with local embeddings
app = App(embedding_model=local_embedding)




