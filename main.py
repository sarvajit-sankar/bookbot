import os

def number_of_words(file_contents):
    words = file_contents.split()
    return words

def number_of_letters(file_content):
    dict_of_letters = {}
    for character in file_content:
        if (character.lower() in dict_of_letters) and (ord(character.lower()) >= 97 and ord(character.lower()) <= 122):
            dict_of_letters[character.lower()] = dict_of_letters[character.lower()] + 1
        elif character.isalpha():
            dict_of_letters[character.lower()] = 1
    return dict_of_letters

path_to_file = "books/frankenstein.txt"
file_content = ""
os.makedirs(os.path.dirname(path_to_file), exist_ok=True)
with open(path_to_file) as f:
    file_content = f.read()

words = number_of_words(file_content)
print(len(words))

dict_of_letters = number_of_letters(file_content)
print(dict_of_letters)

sorted_dict_of_letters = sorted(dict_of_letters.items(), key=lambda x:x[1], reverse=True)

book_name = path_to_file.split("/")[-1]
path_to_report = f"reports/{book_name}-report.txt"
os.makedirs(os.path.dirname(path_to_report), exist_ok=True)
with open(path_to_report, 'w') as w:
    w.write(f"--- Begin report of {path_to_file} ---\n")
    w.write(f"Total non-whitespaced words in doc are: {len(words)} \n\n")
    for letter in sorted_dict_of_letters:
        w.write(f"The '{letter[0]}' character was found {letter[1]} times\n")
    w.write(f"\n\n")
    w.write(f"-----  End of the report ----")