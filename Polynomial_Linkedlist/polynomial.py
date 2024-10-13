from __future__ import annotations
import math


class Node_Polynomial:
    def __init__(self, coff, exp, link=None) -> None:
        self.coff: int = coff
        self.exp: int = exp
        self.link: Node_Polynomial = link


class Polynomial:
    # Create
    # Time Complexity O(n)
    def __init__(self, *x):
        ptr = None
        head = None
        for i in x:
            t = Node_Polynomial(i[0], i[1], None)
            if ptr is None:
                ptr = t
                head = ptr
                continue
            else:
                ptr.link = t
                ptr = t
        self.head = head

    # Time Complexity O(n)
    def __str__(self) -> None:
        ptr = self.head
        res = ""
        while ptr != None:
            if ptr.coff < 0:
                res += f" {ptr.coff}x{ptr.exp}"
            else:
                res += f" +{ptr.coff}x{ptr.exp}"

            ptr = ptr.link
        return res

    # Time Complexity O(n)
    def addition(self, poly2: Polynomial) -> Polynomial:
        newNode = None
        ptr = None
        x = self.head
        y = poly2.head
        while (x is not None) and (y is not None):
            if x.exp == y.exp:
                t = Node_Polynomial(x.coff + y.coff, x.exp, None)
                x = x.link
                y = y.link
            elif x.exp > y.exp:
                t = Node_Polynomial(x.coff, x.exp, None)
                x = x.link
            elif x.exp < y.exp:
                t = Node_Polynomial(y.coff, y.exp, None)
                y = y.link

            if ptr == None:
                ptr = t
                newNode = ptr
                continue
            ptr.link = t
            ptr = t

        while x is not None:
            t = Node_Polynomial(x.coff, x.exp, None)
            ptr.link = t
            ptr = t
            x = x.link

        while y is not None:
            t = Node_Polynomial(y.coff, y.exp, None)
            ptr.link = t
            ptr = t
            y = y.link

        new_poly = Polynomial()
        new_poly.head = newNode
        return new_poly

    # Time Complexity O(n)
    def subtraction(self, poly2: Polynomial) -> Polynomial:
        x = self.head
        y = poly2.head
        newNode = None
        ptr = None
        while (x is not None) and (y is not None):
            if x.exp == y.exp:
                t = Node_Polynomial(x.coff - y.coff, x.exp, None)
                x = x.link
                y = y.link
            elif x.exp > y.exp:
                t = Node_Polynomial(x.coff, x.exp, None)
                x = x.link
            elif x.exp < y.exp:
                t = Node_Polynomial(-y.coff, y.exp, None)
                y = y.link

            if ptr == None:
                ptr = t
                newNode = ptr
                continue

            ptr.link = t
            ptr = t

        while x is not None:
            t = Node_Polynomial(x.coff, x.exp, None)
            ptr.link = t
            ptr = t
            x = x.link

        while y is not None:
            t = Node_Polynomial(-y.coff, y.exp, None)
            ptr.link = t
            ptr = t
            y = y.link

        x = Polynomial()
        x.head = newNode
        return x

    # Time Complexity O(n)
    def eval(head: Node_Polynomial, xval) -> int:
        res = 0
        ptr = head
        while ptr != None:
            res += ptr.coff * math.pow(xval, ptr.exp)
            ptr = ptr.link
        return res


if __name__ == "__main__":
    p = Polynomial([4, 3], [9, 2], [6, 1], [7, 0])
    q = Polynomial([5, 4], [7, 3], [9, 1])
    print(p)
    print(q)
    x = q.addition(p)
    print(x)
