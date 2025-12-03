def get_num_words(book_text):
    words = book_text.split()
    return len(words)
def get_num_char(book_text):
    lowercased = book_text.lower()
    counts = {}
    for char in lowercased:
        counts[char] = counts.get(char, 0) + 1
    return counts
