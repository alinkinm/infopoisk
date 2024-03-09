import os
import task2

def load_inverted_index(file_path):
    inverted_index = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split()
            term = parts[0]
            documents = set(parts[1:])
            inverted_index[term] = documents
    return inverted_index

def boolean_search(query, inverted_index):
    terms = query.split()
    result_set = None
    operator = None
    for term in terms:
        term = term.strip('()')
        if term in {'AND', 'OR'}:
            operator = term
        else:
            term_set = inverted_index.get(term, set())
            if result_set is None:
                result_set = term_set
            elif operator == 'AND':
                result_set = result_set.intersection(term_set)
            elif operator == 'OR':
                result_set = result_set.union(term_set)

    return result_set

def main():
    folder_path = 'downloaded_pages'
    dictionary = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.html'):

            file_path = os.path.join(folder_path, filename)
            text = task2.extract_text_from_file(file_path)
            tokens = task2.tokenize_and_filter(text)
            rm_tokens = task2.remove_malformed_tokens(tokens)

            for word in rm_tokens:
                if word in dictionary:
                    if filename.split(".")[0] not in dictionary[word]:
                        dictionary[word] = dictionary[word]+" "+filename.split(".")[0]
                else:
                    dictionary[word] = filename.split(".")[0]


    with open("inverted_index.txt", "w", encoding="utf-8") as lemmatized_token_file:
        for key, value in dictionary.items():
            lemmatized_token_file.write(f"{key} {value}\n")


    # Пример
    inverted_index = load_inverted_index('inverted_index.txt')
    query = "(толстой AND каренина AND аз) OR отмщение"
    try:
        result = boolean_search(query, inverted_index)
        print("Результат поиска:", result)
    except ValueError as e:
        print("Ошибка:", e)



if __name__ == "__main__":
    main()