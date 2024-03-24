import math
import os
import string
import pymorphy2
from bs4 import BeautifulSoup
import nltk
import re
import task2

#словарь появление термина в документе. значение - колво документов где есть термин
global_for_idf = {}

def pymorphy2_311_hotfix():
    from inspect import getfullargspec
    from pymorphy2.units.base import BaseAnalyzerUnit

    def _get_param_names_311(klass):
        if klass.__init__ is object.__init__:
            return []
        args = getfullargspec(klass.__init__).args
        return sorted(args[1:])

    setattr(BaseAnalyzerUnit, '_get_param_names', _get_param_names_311)

def main():
    folder_path = 'downloaded_pages'

    global_tf = [] #список словарей для каждого файла по очереди

    global_lemmas = [] #список словарей всех форм токенов

    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):
            file_tokens = []
            file_path = os.path.join(folder_path, filename)
            text = task2.extract_text_from_file(file_path)
            tokens = task2.tokenize_and_filter(text)

            #список токенов с повторениями (не приведены к начальной форме)
            file_tokens = tokens

            appear_num = {}

            appear_num_lemma = {}
            pymorphy2_311_hotfix()
            morph = pymorphy2.MorphAnalyzer()

            unique_tokens = task2.remove_malformed_tokens(file_tokens)
            my_dict = {}
            for token in unique_tokens:
                if morph.parse(token)[0].normal_form in my_dict.keys():
                    my_dict[morph.parse(token)[0].normal_form].append(token)
                else:
                    my_dict[morph.parse(token)[0].normal_form] = [token]


            for token in my_dict:
                #посчитать вхождения для каждого токена в этом листе
                if token in appear_num.keys():
                    appear_num[token] +=1
                else:
                    appear_num[token] = 0

            for token in my_dict:
                for v in my_dict[token]:
                    if v in appear_num_lemma.keys():
                        appear_num_lemma[v] +=1
                    else:
                        appear_num_lemma[v] = 0

            token_tf = {}
            lemma_tf = {}

            for token in my_dict:
                token_tf[token] = appear_num[token]/len(file_tokens)

            for token in my_dict:
                for v in my_dict[token]:
                    lemma_tf[v] = appear_num_lemma[v]/len(file_tokens)

            global_tf.append(token_tf)
            global_lemmas.append(lemma_tf)
            #список со словарями для каждого файла


    output_folder = "termins"

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for i, dictionary in enumerate(global_tf):
        idf1 = {}
        idf2 = {}
        tf_idf = {}
        for term in dictionary:
            idf1[term] = 1
            for other_dict in global_tf:
                if dictionary != other_dict:
                    if term in other_dict.keys():
                        idf1[term] += 1
        for term in dictionary:
            idf2[term] = math.log(100/idf1[term])
            tf_idf[term] = dictionary[term]*idf2[term]

        with open(os.path.join(output_folder, f"terms_{i}.txt"), "w", encoding="utf-8") as token_file:
            for term in dictionary:
                token_file.write(f'{term} {idf2[term]} {tf_idf[term]}\n')

    for i, dictionary in enumerate(global_lemmas):
        idf1l = {}
        idf2l = {}
        tf_idfl = {}
        for term in dictionary:
            idf1l[term] = 1
            for other_dict in global_lemmas:
                if dictionary != other_dict:
                    if term in other_dict.keys():
                        idf1l[term] += 1
        for term in dictionary:
            idf2l[term] = math.log(100 / idf1l[term])
            tf_idfl[term] = dictionary[term] * idf2l[term]

        with open(os.path.join(output_folder, f"lemmas_{i}.txt"), "w", encoding="utf-8") as token_file:
            for term in dictionary:
                token_file.write(f'{term} {idf2l[term]} {tf_idfl[term]}\n')

if __name__ == "__main__":
    main()