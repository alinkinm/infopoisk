import os
import string
import pymorphy2
from bs4 import BeautifulSoup
import nltk
import re

def extract_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file.read(), 'html.parser')
        # Удаляем содержимое тегов <style> и <script>
        for tag in soup(['style', 'script']):
            tag.decompose()
        text = soup.get_text()
    return text



nltk.download('stopwords')
stopwords = set(nltk.corpus.stopwords.words('russian'))


unwanted_words = ['и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 'то', 'все', 'она', 'так', 'его', 'но', 'да', 'ты', 'к', 'у', 'же', 'вы', 'за', 'бы', 'по', 'только', 'ее', 'мне', 'было', 'вот', 'от', 'меня', 'еще', 'нет', 'о', 'из', 'ему', 'теперь', 'когда', 'даже', 'ну', 'вдруг', 'ли', 'если', 'уже', 'или', 'ни', 'быть', 'был', 'него', 'до', 'вас', 'нибудь', 'опять', 'уж', 'вам', 'ведь', 'там', 'потом', 'себя', 'ничего', 'ей', 'может', 'они', 'тут', 'где', 'есть', 'надо', 'ней', 'для', 'мы', 'тебя', 'их', 'чем', 'была', 'сам', 'чтоб', 'без', 'будто', 'чего', 'раз', 'тоже', 'себе', 'под', 'будет', 'ж', 'тогда', 'кто', 'этот', 'того', 'потому', 'этого', 'какой', 'совсем', 'ним', 'здесь', 'этом', 'один', 'почти', 'мой', 'тем', 'чтобы', 'нее', 'сейчас', 'были', 'куда', 'зачем', 'всех', 'никогда', 'можно', 'при', 'наконец', 'два', 'об', 'другой', 'хоть', 'после', 'над', 'больше', 'тот', 'через', 'эти', 'нас', 'про', 'всего', 'них', 'какая', 'много', 'разве', 'три', 'эту', 'моя', 'впрочем', 'хорошо', 'свою', 'этой', 'перед', 'иногда', 'лучше', 'чуть', 'том', 'нельзя', 'такой', 'им', 'более', 'всегда', 'конечно', 'всю', 'между']

def filter_tokens(tokens):
    filtered_tokens = []
    #print("unfiltered tokens", tokens)
    for token in tokens:
        if len(token) > 1 and token.isalpha() and token not in stopwords and not token.isdigit() \
           and re.match(r'^[а-яА-Я]*$', token) and token not in unwanted_words:
            filtered_tokens.append(token)
    #print("filtered tokens", filtered_tokens)
    return filtered_tokens

def tokenize_and_filter(text):
    tokens = nltk.word_tokenize(text.lower())
    return filter_tokens(tokens)


def remove_malformed_tokens(tokens):
    filtered_tokens = []
    for token in tokens:
        if not any(other_token in token for other_token in tokens if other_token != token):
            filtered_tokens.append(token)
    return filtered_tokens

def lemmatize_tokens(tokens):
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return lemmatized_tokens

def group_tokens_by_lemmas(tokens):
    grouped_tokens = {}
    for token in tokens:
        lemma = token
        if lemma in grouped_tokens:
            if token not in grouped_tokens[lemma]:
                grouped_tokens[lemma].append(token)
        else:
            grouped_tokens[lemma] = [token]
    return grouped_tokens


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
    all_tokens = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):
            file_path = os.path.join(folder_path, filename)
            text = extract_text_from_file(file_path)
            tokens = tokenize_and_filter(text)
            rm_tokens = remove_malformed_tokens(tokens)
            all_tokens.extend(rm_tokens)

    unique_tokens = list(set(all_tokens))
    print("unique tokens", unique_tokens)
    pymorphy2_311_hotfix()
    morph = pymorphy2.MorphAnalyzer()

    my_dict ={}
    for token in unique_tokens:
        if morph.parse(token)[0].normal_form in my_dict.keys():
            my_dict[morph.parse(token)[0].normal_form].append(token)
        else:
            my_dict[morph.parse(token)[0].normal_form] = [token]

    print(my_dict)

    with open("all_tokens.txt", "w", encoding="utf-8") as token_file:
        token_file.write('\n'.join(unique_tokens))

    with open("all_lemmatized_tokens.txt", "w", encoding="utf-8") as lemmatized_token_file:
        for key, value in my_dict.items():
            lemmatized_token_file.write(f"{key}: {' '.join(value)}\n")

if __name__ == "__main__":
    main()
