from collections import deque


class Tree_Node:
    def __init__(self, data, lchild=None, rchild=None):
        self.lchild = lchild
        self.data = data
        self.rchild = rchild


class Tree:
    ############################################################
    # Construction of  tree for various methods
    ############################################################
    def __init__(self, *args):
        if len(args) == 1:
            self.root = args[0]
        else:
            self._Create_with_keybaord()

    def _Create_with_keybaord(self) -> None:
        queue = deque()
        x = input("enter root value ")
        root = Tree_Node(x)
        queue.append(root)

        while len(queue) != 0:
            p = queue.popleft()
            left: str = input(f"enter the left child of {p.data} ")
            if left != "":
                t = Tree_Node(int(left))
                p.lchild = t
                queue.append(t)
            else:
                p.lchild = None

            right: str = input(f"enter the right child {p.data} ")
            if right != "":
                t = Tree_Node(int(right))
                p.rchild = t
                queue.append(t)
            else:
                p.rchild = None

        self.root = root

    ############################################################
    # Printing of the Tree in postorder,preorder,inorder
    ############################################################
    # Time Complexity O(n)
    def preorder(self, root) -> None:
        if root is not None:
            print(root.data, end=",")
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    # Time Complexity O(n)
    def inorder(self, root) -> None:
        if root is not None:
            self.inorder(root.lchild)
            print(root.data, end=",")
            self.inorder(root.rchild)

    # Time Complexity O(n)
    def postorder(self, root) -> None:
        if root is not None:
            self.postorder(root.lchild)
            self.postorder(root.rchild)
            print(root.data, end=",")

    # Time Complexity O(n)
    def preorder_itrative(self) -> None:
        stack: Tree_Node = deque()
        t = self.root
        while t != None or (len(stack) != 0):
            if t != None:
                print(t.data, end=",")
                stack.append(t)
                t = t.lchild
            else:
                t = stack.pop()
                t = t.rchild
        print()

    # Time Complexity O(n)
    def Inorder_itrative(self) -> None:
        stack: Tree_Node = deque()
        t = self.root
        while t != None or (len(stack) != 0):
            if t != None:
                stack.append(t)
                t = t.lchild
            else:
                t = stack.pop()
                print(t.data, end=",")
                t = t.rchild
        print()

    # Time Complexity O(n)
    def postorder_itrative(self) -> None:
        class items:
            def __init__(self, ispoped: bool, Node: Tree_Node):
                self.ispoped = ispoped
                self.Node = Node

        stack: deque[items] = deque()
        t = items(False, self.root)
        while t.Node != None or (len(stack) != 0):
            if t.Node != None:
                stack.append(items(False, t.Node))
                t = items(False, t.Node.lchild)
            else:
                t = stack.pop()
                if t.ispoped == False:
                    stack.append(items(True, t.Node))
                    t = items(False, t.Node.rchild)
                else:
                    print(t.Node.data, end=",")
                    t.Node = None
        print()

    def level_order(self):
        queue = deque()
        t = self.root
        queue.append(t)
        while len(queue) != 0:
            p = queue.popleft()
            print(p.data, end=",")
            if p.lchild != None:
                queue.append(p.lchild)
            if p.rchild != None:
                queue.append(p.rchild)
        print()

    ################################################################################
    # Counting of nodes(total nodes,count leaf,height,count_internal_nodes)
    ################################################################################

    def total_count(self, root):
        if root != None:
            x = self.total_count(root.lchild)
            y = self.total_count(root.rchild)
            return x + y + 1
        else:
            return 0

    def count_leaf(self, root):
        if root != None:
            x = self.count_leaf(root.lchild)
            y = self.count_leaf(root.rchild)
            if root.lchild == None and root.rchild == None:
                return x + y + 1
            else:
                return x + y
        else:
            return 0

    def height(self, root):
        if root != None:
            x = self.height(root.lchild)
            y = self.height(root.rchild)
            if x > y:
                return x + 1
            else:
                return y + 1
        else:
            return 0

    def count_internal_nodes(self, root):
        if root != None:
            x = self.count_internal_nodes(root.lchild)
            y = self.count_internal_nodes(root.rchild)
            if root.lchild != None or root.rchild != None:
                return x + y + 1
            else:
                return x + y
        else:
            return 0


if __name__ == "__main__":
    #           1
    #         /   \
    #       2       3
    #      / \     / \
    #     4   5   6   7
    tree = Tree(
        Tree_Node(
            1,
            Tree_Node(2, Tree_Node(4), Tree_Node(5)),
            Tree_Node(3, Tree_Node(6), Tree_Node(7)),
        )
    )
    print("**" * 30)
    print("preorder")
    tree.preorder_itrative()
    tree.preorder(tree.root)
    print("\ninorder")
    tree.Inorder_itrative()
    tree.inorder(tree.root)
    print("\npostorder")
    tree.postorder_itrative()
    tree.postorder(tree.root)
    print("\nlevel order")
    tree.level_order()
    print(
        f"Total nodes {tree.total_count(tree.root)} internal nodes {tree.count_internal_nodes(tree.root)} leaf nodes {tree.count_leaf(tree.root)}"
    )

    print(f"height of the Tree is {tree.height(tree.root)}")
