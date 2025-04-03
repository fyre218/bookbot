def number_of_words(file_contents):
    words = file_contents.split()
    num = 0
    for word in words:
        num += 1
    return num

def num_char(file_contents):
    lowercase = file_contents.lower()
    char_dict = {}
    for char in lowercase:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict_item):
    return dict_item["count"]

def sort_list(dict):
    sorted_list = []
    for char in dict:
        if char.isalpha():
            char_dict = {"character": char, "count": dict[char]}
            sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list