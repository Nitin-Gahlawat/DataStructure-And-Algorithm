####################################################
# Finding the Middle of the Node Linked List?
####################################################

from .SingleLinkedList import Linked_list
import math
from .Nodes import Node


# Time Complexity O(n)
# Required two loops
def middlenode_meth1(llinked: Linked_list):
    x = len(llinked) - 1
    x = math.floor(x / 2)
    ptr = llinked.head
    for i in range(0, x):
        ptr = ptr.link
    return ptr


# Time Complexity O(n)
# One loop required
def middlenode_meth2(llinked: Linked_list):
    p, q = llinked.head, llinked.head
    while p is not None:
        p = p.link
        if p != None:
            p = p.link
        else:
            break
        q = q.link

    return q


# Time Complexity O(n)
# One loop required
def middlenode_meth3(llinked: Linked_list):
    s = []
    p = llinked.head
    while p is not None:
        s.append(p)
        p = p.link

    size = math.floor(len(s) / 2)
    while size != 0:
        s.pop()
        size = size - 1

    return s.pop()


if __name__ == "__main__":
    x = Linked_list(1, 2, 3, 4, 5, 6, 7, 8, 9)
    ptr: Node = middlenode_meth1(x)
    print(ptr.data)
    ptr: Node = middlenode_meth2(x)
    print(ptr.data)
    ptr: Node = middlenode_meth3(x)
    print(ptr.data)
