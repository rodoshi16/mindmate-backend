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
        lst = []
        while not self.is_empty():
            lst.append(self._items.pop())
        lst = lst[::-1]
        for item in lst:
            self.push(item)






