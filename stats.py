def get_word_count(string):
    # Return word count as an int
    words = string.split()
    return len(words)

def get_char_count(string):
    result = dict()
    for char in string:
        char = char.lower()
        if char not in result:
            result[char] = 0
        result[char] += 1
    return result