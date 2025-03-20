def get_word_count(string):
    # Return word count as an int
    words = string.split()
    return len(words)

def get_char_count(string):
    char_count = dict()
    for char in string:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def sort_on_count(dict):
    return dict["count"]

def sort_char_count(char_count):
    sorted_chars = []

    for char in char_count:
        sorted_chars.append(dict(
            char = char,
            count = char_count[char]
        ))
    
    sorted_chars.sort(key=sort_on_count,reverse=True)
    return sorted_chars