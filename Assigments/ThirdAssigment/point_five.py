import json

def save_list(lst, filename):
    path = r"/workspaces/Programming-IV/Assigments/ThirdAssigment/" + filename
    with open(path, "w") as f:
        json.dump(lst, f)

def separate_list(lst):
    numbers = [x for x in lst if isinstance(x, int)]
    strings = [x for x in lst if isinstance(x, str)]
    save_list(numbers, "numbers.json")
    save_list(strings, "strings.json")

def replace_odds(lst):
    new_list = ["reemplazo" if isinstance(x, int) and x % 2 != 0 else x for x in lst]
    save_list(new_list, "replacement.json")

def print_half(lst):
    half = len(lst) // 2
    print(lst[:half])

lst = [1, 1991, "taller", 200, 3, "programacion", 700, "utp", "POO"]

save_list(lst, "original_list.json")

separate_list(lst)

replace_odds(lst)

print_half(lst)
