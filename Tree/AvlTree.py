from __future__ import annotations


class node_avl:
    def __init__(self, data: int, height: int, lchild: node_avl, rchild: node_avl):
        self.data = data
        self.height = height
        self.lchild = lchild
        self.rchild = rchild


class avl_tree:

    def __init__(self):
        self.root = None

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

    ############################################################
    # Insertion in AVL Trees
    ############################################################

    def Nodeheight(self, root: node_avl):
        if root is None:
            return 0
        hl = root.lchild.height if root.lchild is not None else 0
        hr = root.rchild.height if root.rchild is not None else 0
        return max(hl, hr) + 1

    def blancefactor(self, root: node_avl):
        if root == None:
            return 0
        hl = root.lchild.height if root.lchild != None else 0
        hr = root.rchild.height if root.rchild != None else 0
        return hl - hr

    def ll_rotation(self, a: node_avl):
        b = a.lchild
        a.lchild = b.rchild
        b.rchild = a
        a.height = self.Nodeheight(a)
        b.height = self.Nodeheight(b)
        if self.root == a:
            self.root = b

        return b

    def rr_rotation(self, a: node_avl):
        b = a.rchild
        a.rchild = b.lchild

        b.lchild = a
        a.height = self.Nodeheight(a)
        b.height = self.Nodeheight(b)

        if self.root == a:
            self.root = b

        return b

    def lr_rotation(self, a: node_avl):
        b = a.lchild
        c = b.rchild

        b.rchild = c.lchild
        a.lchild = c.rchild

        c.lchild = b
        c.rchild = a

        b.height = self.Nodeheight(b)
        a.height = self.Nodeheight(a)
        c.height = self.Nodeheight(c)
        if self.root == a:
            self.root = c

        return c

    def rl_rotation(self, a: node_avl):
        b = a.rchild
        c = b.lchild

        a.rchild = c.lchild
        b.lchild = c.rchild

        c.rchild = b
        c.lchild = a

        b.height = self.Nodeheight(b)
        a.height = self.Nodeheight(a)
        c.height = self.Nodeheight(c)

        if self.root == a:
            self.root = c

        return c

    def Rinsert(self, root: node_avl, ele: int):
        if root == None:
            return node_avl(ele, 1, None, None)
        if root.data > ele:
            root.lchild = self.Rinsert(root.lchild, ele)
        elif root.data < ele:
            root.rchild = self.Rinsert(root.rchild, ele)

        root.height = self.Nodeheight(root)

        if self.blancefactor(root) == 2 and self.blancefactor(root.lchild) == 1:
            root = self.ll_rotation(root)
        elif self.blancefactor(root) == 2 and self.blancefactor(root.lchild) == -1:
            root = self.lr_rotation(root)
        elif self.blancefactor(root) == -2 and self.blancefactor(root.rchild) == -1:
            root = self.rr_rotation(root)
        elif self.blancefactor(root) == -2 and self.blancefactor(root.rchild) == 1:
            root = self.rl_rotation(root)
        return root

    ############################################################
    # Traversal of AVL Trees
    ############################################################

    def inorder(self, root: node_avl):
        if root:
            self.inorder(root.lchild)
            print(root.data, end=" ")
            self.inorder(root.rchild)

    def preorder(self, root: avl_tree):
        if root:
            print(root.data, end=" ")
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    def postorder(self, root: node_avl):
        if root:
            self.postorder(root.lchild)
            self.postorder(root.rchild)
            print(root.data, end=" ")


if __name__ == "__main__":
    root = None
    tree = avl_tree()

    root = tree.Rinsert(root, 30)
    tree.root = root

    x = [20, 40, 10, 25, 5, 15, 28, 4]
    for i in x:
        tree.Rinsert(tree.root, i)

    print("preorder")
    tree.preorder(tree.root)

    print("\ninorder")
    tree.inorder(tree.root)

    print("\npostorder")
    tree.postorder(tree.root)
