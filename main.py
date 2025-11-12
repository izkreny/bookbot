import sys
from stats import (
    number_of_words_in,
    characters_occurrence_in,
    sort_characters_occurrence_descending
)

def main():
    if len(sys.argv) < 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book_path = sys.argv[1]

    book_text = get_text_from(book_path)
    number_of_words_in_book = number_of_words_in(book_text)
    characters_occurrence = characters_occurrence_in(book_text)
    sorted_characters_occurrence = sort_characters_occurrence_descending(characters_occurrence)

    print_report(book_path, number_of_words_in_book, sorted_characters_occurrence)

    return 0

def get_text_from(filepath):
    with open(filepath) as file:
        return file.read()

def print_report(book_path, number_of_words_in_book, sorted_characters_occurrence):
    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {book_path}...")

    print('----------- Word Count ----------')
    print(f"Found {number_of_words_in_book} total words")

    print('--------- Character Count -------')
    for character in sorted_characters_occurrence:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")

    print("============= END ===============")


main()
