from __future__ import annotations
from typing import Any


class _Node:
    item: int
    next: _Node

    def __init__(self, item: Any):
        self.item = item
        self.next = None


class Linked_List:
    _first: _Node

    def __init__(self):
        self._first = None

    def __len__(self):
        length = 0
        curr = self._first

        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def get_item(self, index: int) -> Any:
        """Return the item at position index in this list. Raise IndexError if
        index is the length of this list."""

        curr = self._first
        curr_index = 0

        if index > len(self):
            raise IndexError

        while curr is not None:
            if curr_index == index:
                return curr.item
            curr = curr.next
            index += 1

    def __eq__(self, other: Linked_List):

        if len(self) != len(other):
            return False

        curr1 = self._first
        curr2 = other._first

        while curr1 is not None:
            if curr1.item != curr2.item:
                return False
            curr1 = curr1.next
            curr2 = curr2.next
