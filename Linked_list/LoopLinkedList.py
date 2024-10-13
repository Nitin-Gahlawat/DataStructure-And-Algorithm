####################################################
# Is linked list contain loop ?
####################################################


from __future__ import annotations


from .Nodes import Node


def CreateLoop() -> Node:
    head = None
    p_new: Node = None
    for i in range(1, 5):
        t = Node(i, None)
        if p_new is None:
            p_new = t
            head = p_new
        else:
            p_new.link = t
            p_new = t

    add = Node(5, None)
    p_new.link = add
    p_new = add

    for i in range(6, 10):
        t = Node(i, None)
        p_new.link = t
        p_new = t

    p_new.link = add
    return head


def Isloop(head):
    if head == None:
        raise Exception("The Linked  list is empty")
    ptr1, ptr2 = head, head
    while ptr1 != None:
        # print(ptr1)
        ptr1 = ptr1.link
        if ptr1 is not None:
            ptr1 = ptr1.link
        ptr2 = ptr2.link
        if ptr1 == ptr2:
            return True

    return False


def isloop_address(head):
    add = []
    ptr = head
    while ptr != None:
        if id(ptr) in add:
            return True
        add.append(id(ptr))
        ptr = ptr.link

    return False


def print_loop(head):
    ptr = head
    if isloop_address(head):
        add = []
        while True:
            if id(ptr) in add:
                print(f"the loop on  {ptr.data} from the Last number")
                break
            print(ptr.data)
            add.append(id(ptr))
            ptr = ptr.link
    else:
        while ptr != None:
            print(ptr.data)
            ptr = ptr.link
        print("there is No loop in the Linkedlist")


if __name__ == "__main__":
    head = CreateLoop()
    print(Isloop(head))
    print_loop(head)
