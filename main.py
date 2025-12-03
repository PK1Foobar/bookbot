from stats import get_num_words
from stats import get_num_char
from stats import sort_char_counts

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    return text

def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = get_num_words(book_text)
    
    char_counts = get_num_char(book_text)
    sorted_chars = sort_char_counts(char_counts)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")

main()