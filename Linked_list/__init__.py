from __future__ import annotations

# from Lin.ArrayOprations import ArrayOprtations.
from Linked_list.CircularDoubly import CircularDoubly
from Linked_list.CircularLinkedList import CircularLinkedList
from Linked_list.DoublyLinkedList import Doubly_Linked_List
from Linked_list.LoopLinkedList import CreateLoop, Isloop, print_loop, isloop_address
from Linked_list.MiddleNode import (
    middlenode_meth1,
    middlenode_meth2,
    middlenode_meth3,
)
from Linked_list.Intersection import intersection_linked_List, intersection_point
from Linked_list.OptrationLinkedList import OptrationLinkedList
from Linked_list.SingleLinkedList import Linked_list


def introduction():
    print("\Linked List")
    print("-" * 120)
    print(
        "This Module contains all the algorithm related to the Linked List datastructure"
    )
    print("example of Linked List algorithm")
    x = Linked_list(100, 101, 102, 103, 104)
    print(f"Consider a Linked List {x}")
    x.reverse_links()
    print(f"The reverse of the Linked List is {x}")
