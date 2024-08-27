from __future__ import annotations
## using coordinate list to store the elements
class Element:
    def __init__(self: Element, i: int, j: int, k: int) -> None:
        self.i = i
        self.j = j
        self.k = k

    def __str__(self: Element) -> str:
        return f"i={self.i+1} j={self.j+1} k={self.k}"