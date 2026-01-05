def number_of_words(str):
    words = str.split()
    return len(words)

def character_count(str):
    lower_str = ""
    char_count = {}

    for i in str:
        lower_str += i.lower()
    for i in lower_str:
        char_count[i] = 0
    for i in lower_str:
        char_count[i] += 1
    return char_count

def char_and_num(char_count):
    char_num_list = []

    for k, v in char_count.items():
        char_num_list.append({"char": k, "num": v})

    char_num_list.sort(reverse=True, key=sort_on)
    return char_num_list

def sort_on(items):
    return items["num"]