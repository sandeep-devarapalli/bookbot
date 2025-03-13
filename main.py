import sys
from stats import get_num_words
from stats import charater_counts
from stats import print_dict_sorted_by_value

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else: 
        book_path = sys.argv[1]
        text = get_book_text(book_path)
        num_words = get_num_words(text)
        char_counts = charater_counts(text)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        print_dict_sorted_by_value(char_counts)
        print("============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()