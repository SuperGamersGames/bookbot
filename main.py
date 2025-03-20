from stats import get_word_count

def get_book_text(filepath):
    # Return text in file as a string 
    with open(filepath) as f:
        return f.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    num_words = get_word_count(book_text)
    print(f"{num_words} words found in the document")

main() # Run Program