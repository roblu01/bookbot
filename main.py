import sys
if len(sys.argv) != 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
else:
    book_path= sys.argv[1]

from stats import count_words, count_characters, convert_and_sort_char

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text(book_path)
    word_count = count_words(text)
    f_char_dict = count_characters(text)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    f_list = convert_and_sort_char(f_char_dict)
    for dict in f_list:
        if dict["char"].isalpha() == True:
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
main()