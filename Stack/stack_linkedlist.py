from Linked_list.Nodes import Node


class stack_ll:
    # Time Complexity O(1)
    def __init__(self):
        self.head: Node = None

    # Time Complexity O(1)
    def _create_node(self, data_val: int) -> Node:
        return Node(data_val, None)

    # Time Complexity O(1)
    def isempty(self) -> bool:
        return self.head == None

    # Time Complexity O(1)
    def push(self, a: int) -> None:
        new_node = self._create_node(a)
        new_node.link = self.head
        self.head = new_node

    # Time Complexity O(1)
    def pop(self) -> int:
        if self.isempty():
            raise Exception("The Stack is empty")

        data = self.head.data
        self.head = self.head.link
        return data

    # Time Complexity O(1)
    def peek(self) -> int:
        if self.isempty():
            raise Exception("The Stack is empty")
        data = self.head.data
        return data

    # Time Complexity O(n)
    def peek_pos(self, pos):
        if self.isempty():
            raise Exception("The Stack is empty")
        temp = self.head
        for i in range(pos):
            temp = temp.link
            if temp == None:
                raise Exception("the pos does Not exist")
        return temp.data

    # Time Complexity O(n)
    def __str__(self) -> str:
        if self.head == None:
            return str(None)

        string = "["
        temp: Node = self.head
        while temp.link != None:
            string += str(temp.data) + ","
            temp = temp.link

        string += f"{temp.data}]"
        return string


if __name__ == "__main__":
    x = stack_ll()
    x.push(20)
    x.push(30)
    x.push(500)
    print(x)
    print(x.pop())
    print(x.peek())
