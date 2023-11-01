# Train word embeddings with insurtech corpus

import os
import re
import jieba
from gensim.models import word2vec


# load and split documents

def load_doc(doc_folder_path:str=os.environ.get('doc_folder_path'))->list[str]:
    '''
    读取各年度文档
    返回一个列表，其中每一个元素表示一个年度内的所有文档

    folder_path: 所有txt文件所在文件夹
    '''
    # Get a list of text files in the folder and sort them by filename
    txt_files = sorted([f for f in os.listdir(doc_folder_path) if f.endswith(".txt")])
    
    docs_by_year = []
    for filename in txt_files:
        file_path = os.path.join(doc_folder_path, filename)

        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            docs_by_year.append(content)

    return docs_by_year


def split_docs(docs_by_year:list[str], split_pattern:str=os.environ.get('split_pattern'))->list[str]:
    '''
    切分每个年度内的文档
    返回一个列表，其中每一个元素表示一篇文档

    split_pattern: 用于文档切分的pattern
    '''
    splitted_docs = []
    for docs in docs_by_year:
        doc_list = re.split(split_pattern, docs)
        doc_list = doc_list[:-1]    # remove the last part
        splitted_docs.extend(doc_list)

    return splitted_docs


def split_into_sentences(splitted_docs:list[str])->list[str]:
    '''
    将文档切分为句子
    返回一个列表，其中每一个元素表示一个句子

    splitted_docs: 文档列表，一个元素代表一篇文档
    '''
    sentence_pattern = re.compile('([﹒﹔﹖﹗．；。！？]["’”」』]{0,2}|：(?=["‘“「『]{1,2}|$))')
    sentences = []
    for doc in splitted_docs:
        for i in sentence_pattern.split(doc):
            if sentence_pattern.match(i) and sentences:
                sentences[-1] += i
            elif i:
                sentences.append(i)

    return sentences




# tokenize

def cut(my_dict_path:str=os.environ.get('my_dict_path'))->list[str]:
    '''
    将列表中的句子切分为词语，返回列表, 列表中每一个元素为一个分词后的句子

    my_dict_path: 自定义词典路径
    '''
    if my_dict_path:
        # 让jieba加载自定义词典
        jieba.load_userdict(my_dict_path)

    cut_sentences = []
    for sentence in cut_sentences:
        tokens = [token for token in jieba.cut(sentence)]
        result = ' '.join(tokens)
        cut_sentences.append(result)
    return cut_sentences


def save_sentences(cut_sentences:list[str], cut_sentences_path=os.environ.get('cut_sentences_path')):
    '''
    Save the cut sentences, 1 sentence 1 line.
    '''
    try:
        with open(cut_sentences_path, "w", encoding='utf-8') as f:
            f.writelines(cut_sentences)
    except:
        print(f"Error saving cut_sentences to {cut_sentences_path}")
    return



# train model
def train(sentences=os.environ.get('cut_sentences_path'), model_save_path=os.environ.get('model_save_path')):
    '''train model'''
    sentences = word2vec.LineSentence(sentences)

    # train model, adjust the parameters
    model = word2vec.Word2Vec(sentences, vector_size=100, window=5, min_count=5)

    # save model
    model.save(model_save_path)