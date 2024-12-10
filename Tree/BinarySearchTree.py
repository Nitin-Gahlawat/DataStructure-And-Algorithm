from collections import deque


class Tree_Node:
    def __init__(self, data, lchild=None, rchild=None):
        self.lchild = lchild
        self.data = data
        self.rchild = rchild


class BinarySearch:
    def __init__(self):
        self.root = None

    ############################################################
    # Insertion in BST
    ############################################################
    def insert(self, *args):
        for i in args:
            if self.root is None:
                self.root = Tree_Node(i, None, None)
                continue

            main = self.root
            temp: Tree_Node = None
            while main != None:
                temp = main
                if main.data > i:
                    main = main.lchild
                else:
                    main = main.rchild
            if temp.data > i:
                temp.lchild = Tree_Node(i, None, None)
            else:
                temp.rchild = Tree_Node(i, None, None)

    def Rinsert(self, root: Tree_Node, ele: int):
        if root == None:
            return Tree_Node(ele, None, None)
        if root.data > ele:
            root.lchild = self.Rinsert(root.lchild, ele)
        elif root.data < ele:
            root.rchild = self.Rinsert(root.rchild, ele)
        return root

    ############################################################
    # Print of the BST
    ############################################################
    def inorder(self, root: Tree_Node):
        if root:
            self.inorder(root.lchild)
            print(root.data, end=" ")
            self.inorder(root.rchild)

    def preorder(self, root: Tree_Node):
        if root:
            print(root.data, end=" ")
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    ############################################################
    # Searching in BST
    ############################################################

    def RSearch(self, root: Tree_Node, key: int) -> Tree_Node:
        if root == None:
            return None
        if root.data == key:
            return root
        elif root.data > key:
            return self.RSearch(root.lchild, key)
        else:
            return self.RSearch(root.rchild, key)

    def Search(self, root: Tree_Node, key: int) -> Tree_Node:
        while root != None:
            if root.data == key:
                return root
            elif root.data > key:
                root = root.lchild
            else:
                root = root.rchild
        return None

    ############################################################
    # Deletion in BST
    ############################################################
    def _height(self, root):
        if root != None:
            x = self.height(root.lchild)
            y = self.height(root.rchild)
            if x > y:
                return x + 1
            else:
                return y + 1
        else:
            return 0

    def delete(self, root: Tree_Node, key: int) -> Tree_Node:
        if root == None:
            return None
        if key < root.data:
            root.lchild = self.delete(root.lchild, key)
        elif key > root.data:
            root.rchild = self.delete(root.rchild, key)
        else:
            if root.lchild == None and root.rchild == None:
                return None
            elif self._height(root.lchild) > self._height(root.rchild):
                q = self.Inpre(root.lchild)
                root.data = q.data
                root.lchild = self.delete(root.lchild, q.data)
            else:
                q = self.Insucess(root.rchild)
                root.data = q.data
                root.rchild = self.delete(root.rchild, q.data)
        return root

    def Inpre(self, root: Tree_Node) -> Tree_Node:
        while root.rchild != None:
            root = root.rchild
        return root

    def Insucess(self, root: Tree_Node) -> Tree_Node:
        while root.lchild != None:
            root = root.lchild
        return root

    def generate_tree_preorder(self, pre: list[int]) -> Tree_Node:
        stk: deque[Tree_Node] = deque()
        i = 0
        root = Tree_Node(pre[i], None, None)
        i = i + 1
        p = root
        while i < len(pre):
            if p.data > pre[i]:
                t = Tree_Node(pre[i], None, None)
                i = i + 1
                p.lchild = t
                stk.append(p)
                p = t
            else:
                # in this section because p.data < pre[i]
                if not stk or pre[i] < stk[-1].data:
                    t = Tree_Node(pre[i], None, None)
                    i = i + 1
                    p.rchild = t
                    p = t
                else:
                    p = stk.pop()
        return root


if __name__ == "__main__":

    x = BinarySearch()
    preorderlist = [9, 5, 3, 8, 6, 15, 12, 20, 16]
    x.root = x.generate_tree_preorder(preorderlist)
    #      9
    #   /     \
    #   5      15
    #  / \    /  \
    # 3   8   12  20
    #    /        /
    #    6       16

    x.insert(100, 40)
    x.Rinsert(x.root, 1)
    #          9
    #       /    \
    #     5      15
    #    / \    /  \
    #   3   8   12  20
    #  /   /       /  \
    # 1   6       16   100
    #                  /
    #                 40
    print("Is 40 present in list", False if x.RSearch(x.root, 40) == None else True)
    x.delete(x.root, 40)
    #          9
    #       /    \
    #     5      15
    #    / \    /  \
    #   3   8   12  20
    #  /   /       /  \
    # 1   6       16   100
    print("Inorder")
    x.inorder(x.root)
    print("\npreorder")
    x.preorder(x.root)
