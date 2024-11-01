from Linked_list.Nodes import Node


class Linked_queue:
    def __init__(self):
        self.front = self.rare = None

    def enqueue(self, x):
        t = Node(x, None)
        if self.isempty():
            self.rare = t
            self.front = t
        else:
            self.rare.link = t
            self.rare = t

    def dequeue(self):
        if self.isempty():
            raise Exception("The Queue is Empty")
        data = self.front.data
        self.front = self.front.link
        return data

    def isempty(self):
        if self.front == None:
            return True
        else:
            return False

    def __str__(self):
        if self.isempty():
            return "[]"
        res = "["
        ptr = self.front
        while ptr != None:
            res = res + f"{ptr.data},"
            ptr = ptr.link

        return res[0 : len(res) - 1] + "]"


if __name__ == "__main__":
    x = Linked_queue()
    x.enqueue(0)
    x.enqueue(1)
    x.enqueue(2)
    print(x)
    print("dequeue", x.dequeue())
    print(x)
    x.enqueue(200)
    print(x)
