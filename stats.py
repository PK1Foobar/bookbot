def get_num_words(book_text):
    words = book_text.split()
    return len(words)
def get_num_char(book_text):
    lowercased = book_text.lower()
    counts = {}
    for char in lowercased:
        counts[char] = counts.get(char, 0) + 1
    return counts

def sort_char_counts(char_counts):
    """Convert character counts dict to a sorted list of dictionaries.
    
    Filters to only alphabetical characters and sorts by count (greatest to least).
    Returns list of dicts with 'char' and 'num' keys.
    """
    def get_num(d):
        return d["num"]
    
    char_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=get_num, reverse=True)
    return char_list
