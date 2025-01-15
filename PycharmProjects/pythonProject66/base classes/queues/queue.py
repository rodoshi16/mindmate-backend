from typing import Any
# similar data type to a stack but only you can only
# interact with the bottom


class Queue:
    self._items: list

    def __init__(self):
        self.items = []

    def push(self, item: Any):
        self.items.append(item)

    def pop(self):
        if self._items:
            self.items.pop(self._items[0])

    def is_empty(self):
        return self.items == []




