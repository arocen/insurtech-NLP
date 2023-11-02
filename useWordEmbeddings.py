from gensim.models import Word2Vec
import os
from dotenv import load_dotenv

load_dotenv() # load .env file

# load and use word embeddings model
model = Word2Vec.load(os.environ.get("model_save_path"))


# get vector of a word
vector = model.wv['保险']
print(vector)

# get the most simliar words
keywords = ['保险科技', '人工智能', '大数据']
keywords2 = ['保险科技', '互联网保险', '科技', '大数据', '人工智能', '区块链', '云计算', '无人驾驶汽车', '无人机', '物联网', '车联网', '基因检测', '可穿戴设备', '互联网营销', '互联网理财', '第三方支付', '在线支付', '移动支付', '智能投保', '机器学习', '数字营销', '智能客服', '智能理赔']

def get_similar_words(keywords:list[str], topn:int=10):
    '''对于keywords中每个词语，返回topn个最相似的词'''
    for word in keywords:
        sims = model.wv.most_similar(word, topn=10)
        print(word)
        print(sims)
        print('\n')
    return

get_similar_words(keywords2)

# To-do: think about other ways to figure out keywords about insurtech


# To-do: visualize word embeddings