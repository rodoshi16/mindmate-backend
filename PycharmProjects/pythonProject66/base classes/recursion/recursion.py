# Recursion is when a function calls itself on other functions
from typing import Union

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


def first_at_depth(lst: list, depth: int):
    """


    >>> first_at_depth(100, 0)
    100
    >>> first_at_depth(100,3)
    True
    >>> first_at_depth([1, [2,3], [[7,8], 9]], 2)
    :param int:
    :return:
    """
    if depth == 0:
        return lst

    if isinstance(lst, list):
        for item in lst:
            result = first_at_depth(item, depth-1)
            if result is not None:
                return result
    return None


def add_one(obj: Union[list, int]) -> None:
    """

    >>> lst = [1,[2,3], [[[5]]]]
    >>> add_one(lst)
    >>> lst
    [2, [3, 4], [[[6]]]]
    """

    if isinstance(obj, int):
        return obj + 1
    else:
        for i in range(len(obj)):
            obj[i] = add_one(obj[i])
        return obj


def fib(n: int):
    """

    >>> fib(3)
    2
    >>> fib(5)
    5
    >>> fib(7)
    13

    :param n:
    :return:
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib2(n: int, seen={}):
    """
    There is a lot of redundancy in the fibonnaci numbers being computated. For
    example, fib(28) needs to go through calculations of all fib numbers from 1
    to 27. Instead, we can save the result in a dict and reuse it. It reduces the
    steps from 357 to 95.

    >>> fib2(3)
    2
    >>> fib2(8)
    21

    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in seen:
        return seen[n]
    else:
        seen[n] = fib2(n-1, seen) + fib2(n-2, seen)
        return seen[n]



