from __future__ import annotations

from .Nodes import Node


class CircularLinkedList:
    # Time Complexity O(n)
    def __init__(self, *num):
        if len(num) == 0:
            self.head = None
        else:
            p = last = None
            for i in range(len(num) - 1, -1, -1):
                if len(num) - 1 == i:
                    p = Node(num[i], last)
                    last = p
                else:
                    p = Node(num[i], p)
            self.head = p
            last.link = self.head

    # Time Complexity O(n)
    def __str__(self) -> str:
        p = self.head
        res = "["
        if self.head is not None:
            while True:
                # print(p.data)
                res += f"{p.data},"
                p = p.link
                if id(p) == id(self.head):
                    return res[0 : len(res) - 1] + "]"
        return ""

    # Return the length of the Circular linked list
    # Time Complexity O(n)
    def __len__(self) -> int:
        ct = 0
        p = self.head
        while True:
            ct = ct + 1
            if p is None:
                return 0
            p = p.link
            if id(p) == id(self.head):
                return ct

    # insert the element at the end of the linked list
    # Time Complexity O(n)
    def append(self, data):
        t = Node(data, None)
        ptr = self.head
        if self.head is None:
            self.head = t
            t.link = t
            return

        while True:
            ptr = ptr.link
            if id(ptr.link) == id(self.head):
                ptr.link = t
                t.link = self.head
                return

    # Time Complexity O(n)
    def insert(self, data, pos):
        # cheacking if the position is correct or not
        if len(self) < pos or pos < 0:
            raise Exception("The Position does not exist")

        # if head is none execute this function
        t = Node(data, None)
        if self.head is None:
            self.head = t
            t.link = self.head
            return

        if pos == 0:
            ptr = self.head
            while True:
                ptr = ptr.link
                # print("running")
                if id(ptr.link) == id(self.head):
                    break
            ptr.link = t
            t.link = self.head
            self.head = t

        else:
            ptr = self.head
            for i in range(pos - 1):
                ptr = ptr.link
            t.link = ptr.link
            ptr.link = t

    # Time Complexity O(n)
    def delete(self, pos):
        if (len(self) - 1) < pos or pos < 0:
            raise Exception("The Position does not exist")

        if pos == 0:
            ptr = self.head
            while True:
                ptr = ptr.link
                if id(ptr.link) == id(self.head):
                    break
            ptr.link = self.head.link
            self.head = ptr.link

        else:
            ptr = self.head
            for i in range(pos - 1):
                ptr = ptr.link
            ptr.link = ptr.link.link

    # Time Complexity O(n)
    def reverse(self):
        # If empty
        if self.head is None:
            raise Exception("The array is Empty")

        # Filling address of all the items in a stack
        x = []
        ptr = self.head
        while True:
            x.append(ptr)
            ptr = ptr.link
            if ptr is self.head:
                break

        # Using the stack to reverse the links
        temp = ptr
        while x:
            ptr.link = x.pop()
            temp = temp.link
            ptr = temp

        # shifting the head to the next node
        self.head = self.head.link


if __name__ == "__main__":
    c = CircularLinkedList(1, 2, 3, 4, 5, 6)
    c.insert(45, 6)
    print(c)
    c.reverse()
    print(c)
