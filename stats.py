def get_num_words(book_text):
    words = book_text.split()
    return len(words)
def get_num_char(book_text):
    lowercased = book_text.lower()
    for char in book_text:
        count = lowercased.count(char)
    return len(count)