from __future__ import annotations


class Node_Doubly:
    def __init__(self, pre: Node_Doubly, data: int, next: Node_Doubly) -> None:
        self.pre = pre
        self.data = data
        self.next = next


class Node:
    def __init__(self, data: int, link: Node):
        self.data = data
        self.link = link
