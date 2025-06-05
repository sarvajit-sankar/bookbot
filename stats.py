def get_words(text):
    words = text.split()
    return words

def get_word_count(text):
    words = get_words(text)
    return len(words)

def get_alphabet_count(text):
    alphabet_count = {}
    text = text.lower()
    for char in text:
        alphabet_count[char] = alphabet_count.get(char, 0) + 1
    return alphabet_count

def sort_on(dict):
    return dict["num"]

def get_sorted_list_of_dicts(alphabet_count_dict):
    list_of_dicts = []
    for key in alphabet_count_dict:
        list_of_dicts.append({"char": key, "num": alphabet_count_dict[key]})
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts