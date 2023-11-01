# Run this file to train and save a word embedding model

import insurtech_word_embeddings as IWE

# preprocess
docs_by_year = IWE.load_doc()
splitted_docs = IWE.split_docs(docs_by_year)
sentences = IWE.split_into_sentences(splitted_docs)

# cut into words
cut_sentences = IWE.cut()

# save cut sentences as external txt file
IWE.save_sentences(cut_sentences)

# train model
IWE.train()