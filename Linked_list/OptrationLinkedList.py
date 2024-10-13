from __future__ import annotations

# import Linked_list
from Linked_list.SingleLinkedList import Linked_list
from .Nodes import Node


class OptrationLinkedList:
    def __init__(self, LinkedList) -> None:
        self.LinkedList = LinkedList

    ###################################################
    # Finding The maximum and minimum in the Linked List
    ###################################################

    # Time complexity O(n)
    def Finding_min_max(self) -> tuple[int]:
        if self.LinkedList.head == None:
            raise Exception(f"The given linked list is empty")

        temp: Node = self.LinkedList.head
        max, min = temp.data, temp.data

        while temp != None:
            if max < temp.data:
                max = temp.data
            if min > temp.data:
                min = temp.data
            temp = temp.link
        return min, max

    ###############################################
    # Finding no of occurence in the linked list
    ###############################################
    # Time complexity O(n)
    def Finding_occurence(self) -> dict[int, int]:
        temp: Node = self.LinkedList.head
        duplicate_data = {}
        while temp != None:
            if temp.data not in duplicate_data:
                duplicate_data[temp.data] = 1
            else:
                duplicate_data[temp.data] += 1
            temp = temp.link

        return duplicate_data

    ###############################################
    # Sum of all elements in a Linked List
    ###############################################
    # Time complexity O(n)
    def sum(self) -> int:
        temp: Node = self.LinkedList.head
        sum_var = 0
        while temp != None:
            sum_var += temp.data
            temp = temp.link
        return sum_var

    ###################################################
    # Removing Duplucate element form the linked list
    ###################################################
    # Time complexity O(n)
    # Space complexity O(n)
    def remove_duplicate(self) -> None:
        p = self.LinkedList.head
        q = p.link
        while q != None:
            if p.data != q.data:
                p = q
                q = q.link
            else:
                p.link = q.link
                q = p.link

    #####################################################
    # Add Two Linked List
    #####################################################
    def concat(self, LinkedList2):
        if self.LinkedList.head is LinkedList2.head:
            LinkedList2 = LinkedList2.copy()

        temp = self.LinkedList.head
        if self.LinkedList.head is None:
            self.LinkedList.head = LinkedList2
        while temp.link != None:
            temp = temp.link
        temp.link = LinkedList2.head

    ######################################################################
    # Add Two sorted Linked List in Sorted manner(it sorts the LinkedList)
    ######################################################################
    # Time complexity O(m+n)
    def Mearging(self, ll2):
        first: Node = self.LinkedList.head
        second: Node = ll2.head
        Third, last = None, None

        if first.data < second.data:
            Third = first
            last = first
            first = first.link
            last.link = None
        else:
            Third = second
            last = second
            second = second.link
            last.link = None

        while first is not None and second is not None:
            if first.data < second.data:
                last.link = first
                last = last.link
                first = first.link
                last.link = None
            else:
                last.link = second
                last = last.link
                second = second.link
                last.link = None

        if first != None:
            last.link = first
        if second != None:
            last.link = second

    ###############################################
    # Linear search in Linked List
    ###############################################
    # Time complexity O(n)
    def Linear_search_ll_meth1(self, key: int) -> bool:
        if self.LinkedList.head == None:
            raise Exception("The Linked  list is empty")

        temp: Node = self.LinkedList.head
        while temp != None and temp.data != key:
            temp = temp.link
        if temp != None and temp.data == key:
            return True
        else:
            return False

    # Time complexity O(n)
    def Linear_search_pos(self, key) -> Node:
        if self.LinkedList.head == None:
            raise Exception("The Linked  list is empty")
        ct = 0
        temp: Node = self.LinkedList.head
        while temp != None:
            if temp.data == key:
                return ct
            temp = temp.link
            ct += 1

        if temp == None:
            return None

    # Time complexity O(n)
    def Linear_search_Move_to_head(self, Key: int) -> bool:
        if self.LinkedList.head == None:
            raise Exception("The Linked  list is empty")

        p: Node = self.LinkedList.head.link
        q: Node = self.LinkedList.head

        while p != None:
            if p.data == Key:
                q.link = p.link
                p.link = self.LinkedList.head
                self.LinkedList.head = p
                break
            q = p
            p = p.link

        if p == None:
            return False
        return True


if __name__ == "__main__":
    x = Linked_list(1, 2, 3, 4, 5)
    y = Linked_list(10, 20, 30, 40, 50)
    l = OptrationLinkedList(x)
    l.concat(x)
    print(x)
