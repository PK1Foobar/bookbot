import sys
from stats import get_num_words
from stats import get_num_char
from stats import sort_char_counts

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    
    char_counts = get_num_char(book_text)
    sorted_chars = sort_char_counts(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

main()