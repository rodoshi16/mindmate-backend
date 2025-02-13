import doctest
from typing import Any
# A data type similar to lists but you can only interact with the top


class Stack:
    _items: list

    def __init__(self):
        self._items = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self) -> Any:
        last_e = Any
        if self._items:
            last_e = self._items.pop()
        return last_e

    def is_empty(self):
        return self._items == []

    def peek(self) -> Any:
        """"
        >>> s = Stack()
        >>> s.push(1)
        >>> s.push(2)
        >>> s.push(3)
        >>> s.push(4)
        >>> s.peek()
        >>> s.pop()
        4
        >>> s.pop()
        3
        >>> s.pop()
        2
        >>> s.pop()
        1

        """

        last_ele = self.pop()
        self.push(last_ele)
        return last_ele
        # lst = []
        # while not self.is_empty():
        #     lst.append(self._items.pop())
        # lst = lst[::-1]
        # for item in lst:
        #     self.push(item)


def balanced_parenthesis(line: str):
    """Determine if the parenthesis of the string given is a balanced or not.

    # >>> balanced_parenthesis('[(a * (3 + b))]')
    # True
    # >>> balanced_parenthesis('(a * (3 + b]]')
    # False
    >>> balanced_parenthesis('1 + 2(x -y)}')
    False
    # >>> balanced_parenthesis('3 - (x')
    # False

    """
    matching_pairs = {"(": ")", "[": "]", "{": "}"}
    s = Stack()

    for c in line:
        if c in matching_pairs:
            s.push(c)
        # not -> int, operation, closing

    for c in line:
        if matching_pairs[s.peek()] == c:
            s.pop()

    return s.is_empty()


if __name__ == '__main__':
    doctest.testmod()




