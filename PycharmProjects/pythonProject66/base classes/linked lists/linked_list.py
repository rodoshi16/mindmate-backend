from __future__ import annotations
from typing import Any


class _Node:
    val: Any
    next: _Node

    def __init__(self, val: int):
        self.val = val
        self.next = None


class Linked_list:
    _first: _Node

    def __init__(self):
        self._first = None

    def to_list(self) -> list:
        """
        >>> n1 = _Node(1)
        >>> l = Linked_list()
        >>> l._first = n1
        >>> n2 = _Node(2)
        >>> n1.next = n2
        >>> n3 = _Node(3)
        >>> n2.next = n3
        >>> l.to_list()
        [1, 2, 3]
        """
        curr = self._first
        lst = []
        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        return lst


