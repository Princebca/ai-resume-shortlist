# model.py
import json
from sentence_transformers import SentenceTransformer, util
import numpy as np


MODEL_NAME = 'all-MiniLM-L6-v2' # small & fast


class Embedder:
def __init__(self, model_name=MODEL_NAME):
self.model = SentenceTransformer(model_name)


def encode(self, texts):
# texts: str or list[str]
if isinstance(texts, str):
texts = [texts]
emb = self.model.encode(texts, convert_to_numpy=True, show_progress_bar=False)
return emb




embedder = Embedder()




def embedding_to_json(emb):
return json.dumps(emb.tolist())




def json_to_embedding(s):
arr = np.array(json.loads(s))
return arr




def score_resume_against_job(resume_text, job_text):
# returns cosine similarity score (0..1)
e = embedder.encode([resume_text, job_text])
sim = util.cos_sim(e[0], e[1]).item()
return float(sim)
