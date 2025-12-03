from stats import get_num_words
from stats import get_num_char

def get_book_text(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    return text

def main():
    book_text = get_book_text('books/frankenstein.txt')
    num_words = get_num_words(book_text)
    print("Found",num_words,"total words")
    
    char_counts = get_num_char(book_text)
    print("Found",len(char_counts),"unique characters")
    
    for char, count in char_counts.items():
        print(f"'{char}': {count}")

main()