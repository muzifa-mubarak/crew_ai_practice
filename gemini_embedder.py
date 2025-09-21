from typing import List, Union
import google.generativeai as genai
from chromadb.api.types import EmbeddingFunction

class GeminiEmbedder(EmbeddingFunction):
    def __init__(self, model="models/embedding-001"):
        self.model = model
        self.embedding_fn = self.__call__  

    def __call__(self, input: Union[str, List[str]]) -> List[List[float]]:
        """Chroma requires this exact signature: (self, input)"""
        if isinstance(input, str):
            input = [input]

        embeddings = []
        for text in input:
            response = genai.embed_content(model=self.model, content=text)
            embeddings.append(response["embedding"])

        return embeddings




