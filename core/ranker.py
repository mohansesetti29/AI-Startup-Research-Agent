import numpy as np
from .embedder import cosine

def rank_passages(passages, passage_embs, q_emb, top_k=4):
    scores = [cosine(e, q_emb) for e in passage_embs]
    idx = np.argsort(scores)[::-1][:top_k]
    return [(passages[i], scores[i]) for i in idx]
