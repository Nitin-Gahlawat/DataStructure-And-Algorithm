from __future__ import annotations

from .Nodes import Node_Doubly


class CircularDoubly:
    # Time Complexity O(n)
    def __init__(self, *num) -> None:
        self.head = None
        if len(num) == 0:
            return

        temp = None

        for i in num:
            t = Node_Doubly(None, i, None)
            if temp is None:
                self.head = t
            else:
                temp.next = t
            t.pre = temp
            temp = t
        temp.next = self.head
        self.head.pre = temp

    # Time Complexity O(n)
    def append(self, data):
        t = Node_Doubly(None, data, None)
        if self.head == None:
            t.next = t
            t.pre = t
            self.head = t
        else:
            ptr = self.head
            while True:
                if id(self.head) == id(ptr.next):
                    t.next = ptr.next
                    t.pre = ptr
                    ptr.next.pre = t
                    ptr.next = t
                    return
                ptr = ptr.next

    # Time Complexity O(n)
    def __len__(self) -> int:
        if self.head is None:
            return 0
        ptr = self.head
        ct = 0
        while True:
            ptr = ptr.next
            ct += 1
            if id(self.head) == id(ptr):
                return ct

    # Time Complexity O(n)
    def __str__(self) -> str:
        return self.forward_print()

    # Time Complexity O(n)
    def forward_print(self):
        if self.head is None:
            return "[]"
        ptr = self.head
        res = "["
        while True:
            res += f"{ptr.data},"
            ptr = ptr.next
            if id(self.head) == id(ptr):
                return res[0 : len(res) - 1] + "]"

    # Time Complexity O(n)
    def backward_print(self):
        if self.head is None:
            return "[]"

        ptr = self.head.pre
        res = "["
        while True:
            res += f"{ptr.data},"
            if id(self.head) == id(ptr):
                return res[0 : len(res) - 1] + "]"
            ptr = ptr.pre

    # Time Complexity O(n)
    def inset(self, data: int, pos: int) -> None:
        if pos > len(x) or pos < 0:
            raise IndexError("The pos givem does not exist")

        t = Node_Doubly(None, data, None)
        if self.head == None:
            t.next = t
            t.pre = t
            self.head = t
            return
        if pos == 0:
            ptr = self.head
            while True:
                ptr = ptr.next
                if id(self.head) == id(ptr.next):
                    t.next = ptr.next
                    t.pre = ptr
                    ptr.next = t
                    self.head.pre = t
                    self.head = t
                    return
        else:
            temp = self.head
            for i in range(0, pos - 1):
                temp = temp.next
            t.next = temp.next
            t.pre = temp
            temp.next.pre = t
            temp.next = t

    # Time Complexity O(1)
    def delete_beg(self):
        if self.head is None:
            raise Exception("can not delete form the Empty linked list")

        ptr = self.head
        ptr.pre.next = ptr.next
        ptr.next.pre = ptr.pre
        self.head = ptr.next

    # Time Complexity O(n)
    def delete_pos(self, pos):
        if len(self) - 1 < pos or pos < 0:
            raise Exception("The Position does not exist")

        if pos == 0:
            self.delete_beg()
        else:
            ptr = self.head
            for i in range(pos - 1):
                ptr = ptr.next
            ptr.next.pre = ptr
            ptr.next = ptr.next.next

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
            ptr = ptr.next
            if ptr is self.head:
                break

        temp = ptr
        while x:
            t = x.pop()
            ptr.next = t
            t.pre = ptr
            temp = temp.next
            ptr = temp

        # Moving
        self.head = self.head.next


if __name__ == "__main__":
    x = CircularDoubly(1, 2, 3, 4)
    print(x)
    x.reverse()
    print(x.backward_print())
