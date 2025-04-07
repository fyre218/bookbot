import sys
from stats import number_of_words, num_char, sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    file_content = get_book_text(book_path)
    char_count = num_char(file_content)
    sorted_list = sort_list(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(file_content)} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list:
        char = char_dict["character"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()