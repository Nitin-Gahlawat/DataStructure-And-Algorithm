# stack using array
class Stack:
    # Time Complexity O(1)
    def __init__(self, number_of_ele: int):
        self.top: int = -1  # Number of elements
        self.size: int = number_of_ele
        self.stack: list[int] = self._create_stack(number_of_ele)

    # Time Complexity O(1)
    def _create_stack(self, number_of_ele: int) -> list[int]:
        stack = [0 for _ in range(0, number_of_ele)]
        return stack

    # Time Complexity O(1)
    def isempty(self) -> bool:
        return self.top == -1

    # Time Complexity O(1)
    def isfull(self) -> bool:
        return self.top == self.size - 1  # beacuse static initial value fo top is -1

    # Time Complexity O(1)
    def top(self) -> int:
        return self.top

    # Time Complexity O(1)
    def push(self, a: int) -> None:
        if self.isfull():
            raise Exception("The Stack is Full")
        self.top += 1
        self.stack[self.top] = a

    # Time Complexity O(1)
    def pop(self) -> int:
        if self.isempty():
            raise Exception("The Stack is empty")
        x: int = self.stack[self.top]
        self.stack[self.top] = 0
        self.top = self.top - 1
        return x

    # Time Complexity O(1)
    def size(self) -> int:
        return self.size

    # Time Complexity O(1)
    def peek(self) -> int:
        if self.isempty():
            raise Exception("The Stack is empty")

        return self.stack[self.top]

    # Time Complexity O(1)
    def peek_index(self, index) -> int:
        if self.isempty():
            raise Exception("The Stack is empty")

        if (self.top - index + 1) < 0:
            raise Exception("invalid postition")

        return self.stack[self.top - index + 1]

    # Time Complexity O(n)
    def __str__(self) -> str:
        temp = "["
        for i in range(0, self.top + 1, 1):
            if i != self.top:
                temp += str(self.stack[i]) + ","
            else:
                temp += str(self.stack[i]) + "]"
        return temp


if __name__ == "__main__":
    x = Stack(4)
    x.push(20)
    x.push(30)
    x.push(50)
    x.push(90)
    print(x)
