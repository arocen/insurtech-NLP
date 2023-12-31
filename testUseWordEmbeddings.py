from gensim.models import Word2Vec
import os
from dotenv import load_dotenv

load_dotenv() # load .env file

# load and use word embeddings model
model = Word2Vec.load(os.environ.get("test_model_save_path"))


# get vector of a word
vector = model.wv['保险']
print(vector)

# get the most simliar words
sims = model.wv.most_similar('保险科技', topn=10)
print(sims)


# To-do: visualize word embeddings