from stats import number_of_words
from stats import num_char
from stats import sort_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    file_content = get_book_text("./books/frankenstein.txt")
    char_count = num_char(file_content)
    sorted_list = sort_list(char_count)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words(file_content)} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_list:
        char = char_dict["character"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()