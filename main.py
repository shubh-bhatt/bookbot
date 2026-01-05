from stats import number_of_words, character_count, char_and_num
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
   

    
    str = get_book_text(sys.argv[1])



    num_words = number_of_words(str)
    print(f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
""")
    char_count = character_count(str)
    result = char_and_num(char_count)

    for i in result:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()