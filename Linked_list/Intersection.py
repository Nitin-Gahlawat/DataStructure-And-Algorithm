from .Nodes import Node

from .SingleLinkedList import Linked_list


def intersection_linked_List():
    ptr = None

    three = None
    for i in range(1001, 1005):
        t = Node(i, None)
        if three is None:
            three = t
            ptr = t
            continue
        if ptr is not None:
            ptr.link = t
        ptr = t

    one = None
    for i in range(4):
        t = Node(i, None)
        if one is None:
            one = t
            ptr = t
            continue
        if ptr is not None:
            ptr.link = t
        ptr = t

    ptr.link = three

    two = None
    for i in range(101, 105):
        t = Node(i, None)
        if two is None:
            two = t
            ptr = t
            continue
        if ptr is not None:
            ptr.link = t
        ptr = t

    ptr.link = three

    return one, two


def intersection_point(one: Node, two: Node):
    s1 = []
    s2 = []

    while one != None:
        s1.append(one)
        one = one.link

    while two != None:
        s2.append(two)
        two = two.link

    p = None
    while s1[-1] == s2[-1]:
        p = s1.pop()
        s2.pop()
    print(f"the Intersection point is {p.data}")


if __name__ == "__main__":
    ll = Linked_list()
    x, y = intersection_linked_List()
    ll.head = x
    print(ll)
    ll.head = y
    print(ll)
    intersection_point(x, y)
