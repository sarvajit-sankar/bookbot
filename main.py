from stats import get_word_count, get_alphabet_count, get_sorted_list_of_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(filepath, words_count, sorted_alphabet_list):
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {words_count} total words")
    print("--------- Character Count -------")
    for alphabet_dict in sorted_alphabet_list:
        if alphabet_dict["char"].isalpha():
            print(f"{alphabet_dict['char']}: {alphabet_dict['num']}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_location = sys.argv[1]
    file_contents = get_book_text(file_location)
    # print(file_contents)
    words_count = get_word_count(file_contents)
    # print(f"{words_count} words found in the document")
    alphabet_count_dict = get_alphabet_count(file_contents)
    # print(alphabet_count_dict)
    sorted_alphabet_list = get_sorted_list_of_dicts(alphabet_count_dict)

    print_report(file_location, words_count, sorted_alphabet_list)
if __name__ == "__main__":
    main()