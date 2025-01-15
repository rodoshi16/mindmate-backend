from typing import Any
# A data type similar to lists but you can only interact with the top


class Stack:
    _items: list

    def __init__(self):
        self._items = []

    def push(self, item: Any) -> None:
        self._items.append(item)

    def pop(self, item: Any) -> None:
        if self._items:
            self._items.pop(item)

    def is_empty(self):
        return self._items == []





