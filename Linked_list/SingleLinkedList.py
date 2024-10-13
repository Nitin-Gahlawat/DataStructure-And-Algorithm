from __future__ import annotations
from .Nodes import Node


class Linked_list:

    # Time complexity O(n)
    def __init__(self, *num):
        self.head: Node = None
        ptr = None
        for i in num:
            t = Node(i, None)
            if self.head == None:
                self.head = t
                ptr = t
                continue
            if ptr is not None:
                ptr.link = t
            ptr = t

    #####################################################
    # Check if the Linked List is sorted or not
    #####################################################

    # Time complexity O(n)
    def isSorted(self) -> bool:
        temp = self.head
        x = temp.data
        while temp != None:
            if temp.data < x:
                return False
            x = temp.data
            temp = temp.link
        return True

    ###############################################
    # Insertion of int type in the Linked list
    ###############################################

    # Time complexity O(1)
    def insert_beg(self, data: int) -> None:
        if self.head == None:
            self.head = Node(data, None)
            return
        t = Node(data, self.head)
        self.head = t

    # Time complexity O(n)
    def insert_end(self, data: int) -> None:
        if self.head == None:
            self.head = Node(data, None)
            return
        t = Node(data, None)
        p = self.head
        while p.link is not None:
            p = p.link
        p.link = t

    # Time complexity O(n)
    def insert_sorted(self, ele: int):
        if self.isSorted() == False:
            raise Exception("The list is not sorted")

        # if head is none or ele is less than the first element
        if self.head == None or ele < self.head.data:
            t = Node(ele, self.head)
            self.head = t
            return

        p: Node = self.head
        q: Node = None
        while p != None and p.data < ele:
            q = p
            p = p.link
        q.link = Node(ele, p)

    def insert_pos(self, num: int, pos: int) -> None:
        if len(self) < pos:
            raise IndexError("The pos givem does not exist")

        temp: Node = self.head
        if pos == 0:
            self.head = Node(num, temp)
            return

        for i in range(1, len(self) + 1):
            if i == pos:
                temp.link = Node(num, temp.link)
                return
            temp = temp.link

    #######################################################
    # Deletion of the elements in the Linked list
    #######################################################

    # Time complexity O(n)
    def delete_last(self) -> None:
        if self.head == None:
            raise Exception("No Node to delete in the linked list")

        temp: Node = self.head

        while temp.link.link != None:
            temp = temp.link

        temp.link = None

    # Time complexity O(1)
    def deletion_first(self) -> None:
        if self.head == None:
            raise Exception("No Node to delete in the linked list")
        self.head = self.head.link

    def delete_pos(self, pos: int) -> None:
        if self.head == None:
            raise Exception("No Node to delete in the linked list")
        if (len(self) - 1) < pos:
            raise IndexError("The pos givem does not exist")

        p: Node = self.head
        q: Node = None

        # Handling 0 position as at pos==0 q is None
        if pos == 0:
            self.head = self.head.link
            return

        for i in range(0, len(self)):
            if i == pos:
                q.link = p.link
                p = q.link
                return
            q = p
            p = p.link

    # Reversing a Linked list using Changing the data of the Nodes
    # Time complexity O(n)
    def reverse_data(self):
        temp = self.head
        x = []
        # storing all the elements in an array
        while temp != None:
            x.append(temp.data)
            temp = temp.link

        temp = self.head
        while x:
            temp.data = x.pop()
            temp = temp.link

    # Reversing a Linked list using reversing links technique and Sliding pointers
    # Time complexity O(n)
    def reverse_links(self):
        p = self.head
        q = None
        r = None

        while p != None:
            r = q
            q = p
            p = p.link
            q.link = r
        self.head = q

    # p is the starting point
    def recursive_reverse_links(self, q: Node = None, p: Node = None):
        if q is None:
            p = self.head
        if p != None:
            self.recursive_reverse_links(p, p.link)
            p.link = q
        else:
            self.head = q
            return

    ###############################################
    # Get The Nth node data in Linked List
    ###############################################

    # Time complexity O(n)
    def get_nth_node_data(self, n) -> Node:
        if n > len(self):
            raise Exception(f"The n {n} given > len(linked list) {len(self)}")

        ct = 0
        temp: Node = self.head
        while n > ct:
            temp = temp.link
            ct += 1

        return temp.data

    #####################################################
    # Print the linked list on call of the print function
    #####################################################

    # Time complexity O(n)
    def __str__(self) -> str:
        if self.head == None:
            return f"{self.head}"
        else:
            all_elemnts: str = ""
            temp: Node = self.head
            while temp != None:
                all_elemnts = all_elemnts + (str(temp.data) + " ")
                temp = temp.link
            return all_elemnts

    ###############################################
    # Printing the length of the linked list
    ###############################################
    # Time complexity o(n)
    # Space complexity o(1)
    def __len__(self) -> int:
        if self.head == None:
            return 0

        temp: Node = self.head
        count: int = 1
        while temp.link != None:
            count += 1
            temp = temp.link
        return count

    ###################################################
    # Clearing the linked list
    ###################################################
    def clear(self) -> None:
        self.head = None

    ###################################################
    # Creating a copy of the LinkedList
    ###################################################
    def copy(self) -> Linked_list:
        p: Node = self.head
        new_head: Node = None
        p_new: Node = None
        while p != None:
            t = Node(p.data, None)
            if p_new is None:
                p_new = t
                new_head = p_new
            else:
                p_new.link = t
                p_new = t
            p = p.link
        new_ll: Linked_list = Linked_list()
        new_ll.head = new_head
        return new_ll


if __name__ == "__main__":

    l = Linked_list(2, 3, 4, 5, 6)
    l.insert_beg(1)
    l.insert_pos(0, 0)
    l.insert_pos(500, len(l))
    l.insert_sorted(5)
    print(l)
    l.delete_last()
    print(l)
    l.deletion_first()
    print(l)
    l.delete_pos(0)
    print(l)

    l.recursive_reverse_links()
    print(l)
