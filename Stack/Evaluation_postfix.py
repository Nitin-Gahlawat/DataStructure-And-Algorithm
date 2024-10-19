from Stack.stack import Stack


def isOprand(x) -> bool:
    # print("x val", x)
    if x == "+" or x == "*" or x == "/" or x == "-" or x == "^":
        return False
    else:
        return True


def prec(c) -> int:
    # if c == "A" or c == "B" or c == "C":
    #     return 4
    if c == "^":
        return 3
    elif c == "/" or c == "*":
        return 2
    elif c == "+" or c == "-":
        return 1
    else:
        return -1


def associativity(c):
    if c == "^":
        return "R"
    return "L"


def infix_postfix(infix) -> str:
    # initlize a stack and postfix result
    stk = Stack(len(infix))
    postfix = ""

    i = 0
    # run the loop while the i is less len(infix)
    while i < len(infix):
        if isOprand(infix[i]):
            postfix += infix[i]
            i = i + 1
        else:
            # If the oprater is higher precidence than the stack top precidence
            while not stk.isempty() and prec(infix[i]) <= prec(stk.peek()):
                postfix += stk.pop()

            stk.push(infix[i])
            i = i + 1

    while not stk.isempty():
        postfix += stk.pop()

    return postfix


def eval(postfix):
    stk = Stack(len(postfix))  # str stack
    for i in postfix:
        if isOprand(i):
            stk.push(i)
        else:
            a = float(stk.pop())
            b = float(stk.pop())
            if i == "+":
                c = a + b
            elif i == "*":
                c = a * b
            elif i == "-":
                c = b - a
            elif i == "/":
                c = b / a
            stk.push(str(c))

    return stk.pop()


if __name__ == "__main__":
    infix = "2*3*5+6/6"
    x: str = infix_postfix(infix)
    print("infix", x)
    print("result", eval(x))
