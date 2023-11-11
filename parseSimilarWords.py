# parse print-out results of similar words queries
# e.g.
'''
保险科技
[('科技', 0.6716184616088867), ('。保险科技', 0.6438056230545044), ('互联网保险', 0.6431641578674316), ('科技创新', 0.620501697063446), ('保险行业', 0.5627226233482361), ('保险', 0.5144356489181519), ('保险业', 0.4898820221424103), ('。科技', 0.4826793670654297), ('技术创新', 0.4789864420890808), ('技术', 0.45731592178344727)]


互联网保险
[('保险科技', 0.6431641578674316), ('互联网', 0.6324694156646729), ('中介', 0.5867980122566223), ('保险行业', 0.5346170663833618), ('。互联网保险', 0.5332195162773132), ('人身险', 0.5269761085510254), ('保险', 0.5028257369995117), ('。保险科技', 0.4988291561603546), ('水滴', 0.49777156114578247), ('健康险', 0.4863740801811218)]
'''

from dotenv import load_dotenv
import os
import ast

load_dotenv()
results_path = os.environ.get("query_results")
save_path = os.environ.get("words_save_path")

def load(path:str=results_path)->list[str]:
    '''load results from txt file'''
    with open(path, "r", encoding="utf-8") as f:
        results = f.read()
        rlist = results.split("\n\n\n") # 3 newline characters
    return rlist

def extractWords(rlist:list[str])->list[str]:
    '''extract words from loaded result list'''
    # gain header words and similar words
    headers = []
    sims = []
    for r in rlist:
        parts = r.split("\n")
        header, similar_words = parts[0], parts[1]
        headers.append(header)
        # To-do: transfer str into list
        similar_words = ast.literal_eval(similar_words)
        for pair in similar_words:
            sim = pair[0]
            sims.append(sim)


    
    words = headers + sims
    # drop duplicate words
    words = list(set(words))
    return words

def save_words(save_path, words):
    with open(save_path, "w", encoding="utf-8") as f:
        for word in words:
            f.write(word + "\n")
    return


# 根据相似度可视化某一条查询的结果



rlist = load()
# print(rlist)
words = extractWords(rlist)
print("number of words:", len(words))
print(words)
# 保存到txt
save_words(save_path, words)