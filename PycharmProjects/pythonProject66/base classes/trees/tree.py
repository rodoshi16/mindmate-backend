from __future__ import annotations
from typing import Optional, Any


class Tree:
    _root: Optional[Any]
    _subtrees: list[Tree]

    def __init__(self, root: Optional[Any], subtrees: list[Tree]):
        self._root = root
        self._subtrees = subtrees

    def is_empty(self):
        return self._root is None

    def __len__(self):
        """

        >>> t2 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> len(t2)
        3
        >>> t3 = Tree(2, [Tree(7, [Tree(1, [])]), Tree(5, [Tree(2, [])])])
        >>> len(t3)
        5

        :return:
        """
        length = 0
        if self._root is None:
            return 0
        else:
            length += 1
            for subtree in self._subtrees:
                length += len(subtree)

        return length

    def leaves(self) -> list:
        """Return a list of all leaves in a tree.

        >>> t3 = Tree(2, [Tree(7, [Tree(1, [])]), Tree(5, [Tree(2, [])])])
        >>> t3.leaves()
        [1, 2]
        >>> t1 = Tree(3, [Tree(4, []), Tree(1, [])])
        >>> t1.leaves()
        [4, 1]
        """

        if self._subtrees == []:
            return [self._root]
        else:
            lst = []
            for subtree in self._subtrees:
                lst.extend(subtree.leaves())
            return lst

    def average(self):
        """Return an average of all values in this tree.

        >>> t3 = Tree(2, [Tree(7, [Tree(1, [])]), Tree(5, [Tree(2, [])])])
        >>> t3.average()
        3.4
        >>> t6 = Tree(2, [Tree(5, []), Tree(6, [])])
        >>> t7 = Tree(3, [Tree(7, [])])
        >>> t8 = Tree(4, [Tree(8, [])])
        >>> t9 = Tree(1, [t6, t7, t8])
        >>> t9.average()
        4.5
        >>> t1 = Tree(2, [Tree(5, []), Tree(6, []), Tree(7, [])])
        >>> t2 = Tree(3, [Tree(8, []), Tree(9, []), Tree(10, [])])
        >>> t3 = Tree(4, [Tree(11, []), Tree(12, []), Tree(13, [])])
        >>> t4 = Tree(1, [t1, t2, t3])
        >>> t4.average()
        7.0


        """
        if self._root is None:
            return 0.0
        elif self._subtrees == []:
            return float(self._root)
        else:
            size = 1
            val = self._root
            for subtree in self._subtrees:
                curr = subtree.average_helper()
                val += curr[0]
                size += curr[1]
            return val/size

    def average_helper(self):
        """

        >>> t3 = Tree(2, [Tree(7, [Tree(1, [])]), Tree(5, [Tree(2, [])])])
        >>> t3.average_helper()
        (17, 5)


        :return:
        """
        if self._root is None:
            return 0, 0
        elif self._subtrees == []:
           return self._root, 1
        else:
            size = 1
            value = self._root
            for subtree in self._subtrees:
                curr = subtree.average_helper()
                value += curr[0]
                size += curr[1]
            return value, size















