from __future__ import annotations

from .Nodes import Node_Doubly


class Doubly_Linked_List:

    # Construct a Doubly Linked List
    # Time Complexity O(n)
    def __init__(self, *num):
        self.head = None
        self.tail = None
        temp = self.head

        for i in num:
            t = Node_Doubly(None, i, None)
            if temp is None:
                self.head = t
            else:
                temp.next = t
            t.pre = temp
            temp = t
        self.tail = temp

    # Return the length of the doubly linked list
    # Time Complexity O(n)
    def __len__(self) -> int:
        temp = self.head
        ct = 0
        while temp is not None:
            ct += 1
            temp = temp.next
        return ct

    # Insert a node at the beginning
    # Time Complexity O(1)
    def Insert_beg(self, data) -> None:
        t = Node_Doubly(None, data, None)
        t.next = self.head
        if (self.head is None) and (self.tail is None):
            self.head = self.tail = t
        else:
            self.head.pre = t
            self.head = t

    # Insert a node at the end
    # Time Complexity O(1)
    def Insert_end(self, data) -> None:
        t = Node_Doubly(None, data, None)
        if (self.head is None) and (self.tail is None):
            self.head = self.tail = t
        else:
            self.tail.next = t
            t.pre = self.tail
            self.tail = t

    # Insert a node at the pos
    # Time Complexity O(n)
    def Insert_pos(self, data, pos):
        if (len(self)) < pos or pos < 0:
            raise Exception("The Position does not exist")
        if pos == 0:
            self.Insert_beg(data)
            return

        t = Node_Doubly(None, data, None)
        ptr = self.head
        for i in range(pos - 1):
            ptr = ptr.next

        t.next = ptr.next
        ptr.next = t
        t.pre = ptr
        if t.next is not None:
            t.next.pre = t
        else:
            self.tail = t

    # Delete a node form the beginning
    # Time Complexity O(1)
    def delete_beg(self) -> int:
        if self.head is None:
            raise Exception("No Node present to delete")

        data = self.head.data
        if self.head is not self.tail:
            self.head = self.head.next
            if self.head is not None:
                self.head.pre = None
            return data

        self.tail = self.head = None
        return data

    # Delete a node from the end
    # Time Complexity O(1)
    def delete_end(self) -> int:
        if self.tail is None:
            raise Exception("No Node present to delete")

        data = self.tail.data
        if self.head is not self.tail:
            self.tail = self.tail.pre
            if self.tail is not None:
                self.tail.next = None
            return data

        self.tail = self.head = None
        return data

    # Delete a node from position pos
    # Time Complexity O(n)
    def delete_pos(self, pos) -> int:
        if len(self) - 1 < pos or pos < 0:
            raise Exception("The Position does not exist")
        if pos == 0:
            return self.delete_beg()

        temp = self.head
        for i in range(pos):
            temp = temp.next
        temp.pre.next = temp.next
        if temp.next is not None:
            temp.next.pre = temp.pre

        data = temp.data
        return data

    # Reverse a linked list
    # Time Complexity O(n)
    def reverse(self) -> None:
        temp = self.head
        while temp is not None:
            # Ṣwaping next and previous Of every node
            p = temp.next
            temp.next = temp.pre
            temp.pre = p
            temp = temp.pre
            if (temp is not None) and (temp.next is None):
                self.tail = self.head
                self.head = temp

    # print the doubly linked list using forward link
    # Time Complexity O(n)
    def forward_print(self) -> str:
        temp = self.head
        res = ""
        while temp is not None:
            res += f" {temp.data} ,"
            temp = temp.next
        return "[" + res[0 : len(res) - 1] + "]"

    # print the doubly linked list using backward link
    # Time Complexity O(n)
    def backward_print(self) -> str:
        temp = self.tail
        res = ""
        while temp is not None:
            res += f" {temp.data} ,"
            temp = temp.pre
        return "[" + res[0 : len(res) - 1] + "]"

    # print the doubly linked list using forward link
    # Time Complexity O(n)
    def __str__(self) -> str:
        return self.forward_print()


if __name__ == "__main__":
    x = Doubly_Linked_List(1, 2, 3, 4, 5, 6, 7, 8, 9)
    print(x)
    print(x.backward_print())
    x.delete_pos(4)
    print(x)
    print(x.backward_print())
