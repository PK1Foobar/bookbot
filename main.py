def get_book_text(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    return text
def main():
    book_text = get_book_text('books/frankenstein.txt')
    print("Found",num_words(book_text),"total words")
def num_words(book_text):
    words = book_text.split()
    return len(words)
main()