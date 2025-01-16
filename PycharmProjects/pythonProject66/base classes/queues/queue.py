from typing import Any
# similar data type to a stack but only you can only
# interact with the bottom


class Queue:
    _items: list

    def __init__(self):
        self._items = []

    def push(self, item: Any):
        self._items.append(item)

    def pop(self):
        if self._items:
            self._items.pop(self._items[0])

    def is_empty(self):
        return self._items == []




