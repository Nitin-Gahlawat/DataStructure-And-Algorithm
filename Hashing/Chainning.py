from __future__ import annotations
from Linked_list.Nodes import Node


class chaining:

    def __init__(self):
        self.hashfun = lambda a: a % 10

    def print_hash_table(self, x: list[Node]):
        for i in range(0, len(x)):
            print(f"{i}-------- ", end="")
            temp = x[i]
            while temp != None:
                print(temp.data, end=" ")
                temp = temp.link
            print()

    def searching(self, hashtable: list[Node], ele: int) -> bool:
        if hashtable[self.hashfun(ele)] == None:
            return False
        else:
            temp = hashtable[self.hashfun(ele)]
            while temp != None and temp.data < ele:
                temp = temp.link
            if temp is None:
                return False
            elif temp.data == ele:
                return True
            else:
                return False

    def insert(self, x: list[int]):
        hashtable: list[Node] = [None for _ in range(0, 10)]
        for i in x:
            if hashtable[self.hashfun(i)] == None:
                hashtable[self.hashfun(i)] = Node(i, None)
            else:
                temp = hashtable[self.hashfun(i)]
                pretemp = temp
                while temp != None and temp.data < i:
                    pretemp = temp
                    temp = temp.link
                # The node is first Node
                if temp == pretemp:
                    hashtable[self.hashfun(i)] = Node(i, hashtable[self.hashfun(i)])
                elif temp is None:
                    pretemp.link = Node(i, None)
                else:
                    pretemp.link = Node(i, pretemp.link)
        return hashtable


if __name__ == "__main__":
    x = chaining()
    res = x.insert([16, 12, 122, 68, 5, 25, 299, 121, 199])
    x.print_hash_table(res)
    print(x.searching(res, 121))
