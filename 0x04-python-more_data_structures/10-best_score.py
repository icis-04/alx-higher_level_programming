#!/usr.bin/python3
def best_score(a_dictionary):
    ls = a_dictionary.items()
    max_ls = max(ls)
    if a_dictionary == None:
        return None
    else:
        for i in a_dictionary.keys():
            if a_dictionary[i] == max_ls:
                return i
    return
