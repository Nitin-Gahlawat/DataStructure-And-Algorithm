from Stack.stack import Stack


# Balanced  Paranthisis matching 
def Matching(x: str) -> bool:
    stk = Stack(len(x))

    # Using this to Find out the type of  the paranthisis
    type_open = {
        "[": 1,
        "(": 2,
        "{": 3,
    }
    type_close = {
        "]": 1,
        ")": 2,
        "}": 3,
    }
    for i in x:
        if (i == "[") or (i == "(") or (i == "{"):
            stk.push(type_open[i])
        elif (i == "]") or (i == ")") or (i == "}"):
            if type_close[i] - stk.peek() == 0:
                stk.pop()
            else:
                return False
    if stk.isempty():
        return True
    else:
        return False


def balanced(x: str) -> bool:
    stk = Stack(len(x))
    for i in x:
        if x == "(":
            stk.push("x")
        elif x == ")":
            if stk.isempty():
                return False
            stk.pop()
    if stk.isempty():
        return True
    else:
        return False


if __name__ == "__main__":
    x = "[({({([][)})}])]"
    print(Matching(x))

    x = "[({({([][])})})]"
    print(Matching(x))

    x = "(((A+B)*(c-d))"
    print(balanced(x))
