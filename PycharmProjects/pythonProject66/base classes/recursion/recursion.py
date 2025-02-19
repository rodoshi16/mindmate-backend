# Recursion is when a function calls itself on other functions

def sum_list(l):
    if len(l) == 0:
        return 0
    else:
        return l[0] + sum_list(l[1:])


# What if its nested again: [ 1, [5,3], 8, [4,[9,7]] ]

def nested_list(l: list):
    if isinstance(l, list):
        # elem will get called recursively as many times until it hits base case
        s = 0
        for elem in l:
            s += sum_list(elem)
        return s
    else:
        return l

