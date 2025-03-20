import os
import sys
from stats import get_word_count,get_char_count,sort_char_count

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def get_book_text(filepath):
    # Return text in file as a string 
    with open(filepath) as f:
        return f.read()

def main():
    args = sys.argv
    error = f"{bcolors.FAIL}{bcolors.BOLD}Error:{bcolors.ENDC}{bcolors.FAIL}"
    usage = f"{bcolors.WARNING}{bcolors.BOLD}Usage:{bcolors.ENDC}{bcolors.WARNING}"

    if len(args) != 2:
        print(f"{error} Missing Argument. Expected args to be 2 but instead received {len(args)}{bcolors.ENDC}\n{usage} python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = args[1]
    
    if not os.path.exists(filepath):
        print(f"{error} Invalid Argument. \"{filepath}\" is not a valid filepath.{bcolors.ENDC}\n{usage} python3 main.py <path_to_book>")
        sys.exit(2)
    
    print(f"\n============ BOOKBOT ============")

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

    print(f"============= END ===============\n")

main() # Run Program