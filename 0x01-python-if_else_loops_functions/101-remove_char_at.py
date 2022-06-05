#!usr/bin/python3
def remove_char_at(str, n):
    m = list(str)
    for i in m:
        if i == n:
            m.remove(m[i])
            print("".join(m))
        else:
            print("".join(m))
