
def flatten(lst):
    new_list = []
    for item in lst:
        if isinstance(item, list):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)
    return new_list

nested_list = [1, 2, [3, 4, [5, [6]], 7], 8, 9, 10]

############################################
wynik = flatten(nested_list)
print(wynik)
