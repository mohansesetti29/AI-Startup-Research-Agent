from sentence_transformers import SentenceTransformer
import numpy as np

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer(EMBEDDING_MODEL)

    def encode(self, texts):
        return self.model.encode(texts, convert_to_numpy=True)

def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-10)
