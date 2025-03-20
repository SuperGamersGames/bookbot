from stats import get_word_count,get_char_count,sort_char_count

def get_book_text(filepath):
    # Return text in file as a string 
    with open(filepath) as f:
        return f.read()

def main(filepath):
    print(f"============ BOOKBOT ============")

    book_text = get_book_text(filepath)
    print(f"Analyzing book found at {filepath}...")
    
    print(f"----------- Word Count ----------")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")
    

    print(f"----------- Character Count ----------")
    char_count = sort_char_count(get_char_count(book_text))
    for index in char_count:
        if index["char"].isalpha():
            print(f"{index["char"]}: {index["count"]}")

    print(f"============= END ===============")

main("books/frankenstein.txt") # Run Program