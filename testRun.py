# test run.py with small corpus
import os
import insurtech_word_embeddings as IWE
from dotenv import load_dotenv

load_dotenv() # load .env file

# preprocess
docs_by_year = IWE.load_doc(doc_folder_path=os.environ.get('test_doc_folder_path'))
splitted_docs = IWE.split_docs(docs_by_year)
sentences = IWE.split_into_sentences(splitted_docs)

# cut into words
cut_sentences = IWE.cut()

# save cut sentences
IWE.save_sentences(cut_sentences, cut_sentences_path=os.environ.get('test_cut_sentences_path'))

# train model
IWE.train(sentences=os.environ.get('test_cut_sentences_path'), model_save_path=os.environ.get('test_model_save_path'))