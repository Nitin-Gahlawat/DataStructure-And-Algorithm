from Stack import Stack


def queue_using_stack(*z: list[int]) -> list[int]:
    stk1 = Stack(len(z))
    stk2 = Stack(len(z))

    # pushing all the elements in the stack 1
    for i in z:
        stk1.push(i)

    # pushing all the elements in the stack 2 from stack 2
    while not stk1.isempty():
        stk2.push(stk1.pop())

    # constructing the final res list
    res = []
    while not stk2.isempty():
        res.append(stk2.pop())
    return res


if __name__ == "__main__":
    print(queue_using_stack(1, 2, 3, 4, 5, 6, 8))
