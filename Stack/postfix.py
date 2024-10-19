from Stack.stack import Stack


def isOprand(x) -> bool:
    # print("x val", x)
    if x == "+" or x == "*" or x == "/" or x == "-" or x == "^" or x == ")" or x == "(":
        return False
    else:
        return True


def inprec(x):
    if x == "+" or x == "-":
        return 2
    elif x == "*" or x == "/":
        return 4
    elif x == "^":
        return 5
    elif x == "(":
        return 0
    elif x == ")":
        return 7


def outprec(x):
    if x == "+" or x == "-":
        return 1
    elif x == "*" or x == "/":
        return 3
    elif x == "^":
        return 6
    elif x == "(":
        return 7
    elif x == ")":
        return 0


def infix_postfix(infix) -> str:
    # initlize a stack and postfix result
    stk = Stack(len(infix))
    postfix = ""

    i = 0
    # run the loop while the i is less length of string infix
    while i < len(infix):
        # If it is oprand than push it in the string
        if isOprand(infix[i]):
            postfix += infix[i]
            i = i + 1
        else:
            # if it si Closing bracket
            if infix[i] == ")":
                while not stk.isempty() and stk.peek() != "(":
                    postfix += stk.pop()
                if stk.isempty():
                    raise Exception("The string is not valid")
                else:
                    stk.pop()
            else:
                # If the oprater is higher precidence than the stack top precidence
                while not stk.isempty() and outprec(infix[i]) <= inprec(stk.peek()):
                    postfix += stk.pop()

                stk.push(infix[i])
            i = i + 1

    while not stk.isempty():
        if stk.peek() == "(":
            raise Exception("The string is not valid")
        else:
            postfix += stk.pop()

    return postfix


if __name__ == "__main__":
    infix = "(A+(B*C)-D*(E+F))"
    x: str = infix_postfix(infix)
    print(x)
