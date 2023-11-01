# Train word embeddings with insurtech corpus

import os
import re


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

    split_pattern: 文档切分pattern
    '''
    splitted_docs = []
    for docs in docs_by_year:
        doc_list = re.split(split_pattern, docs)
        doc_list = doc_list[:-1]    # remove the last part
        splitted_docs.extend(doc_list)

    return splitted_docs



# tokenize

def tokenize(my_dict_path:str=os.environ.get('my_dict_path')):
    '''
    将列表中的句子切分为词语，返回列表, 列表中每一个元素为一个分词后的句子

    my_dict_path: 自定义词典路径
    '''
    # To-do

    return




# train model


# save model