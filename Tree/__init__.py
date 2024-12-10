from Tree.AvlTree import avl_tree
from Tree.BinarySearchTree import BinarySearch
from Tree.general_binarytree import Tree
from Tree.Heap import (
    create_heap_max,
    create_heap_min,
    delete_maxheap,
    delete_minheap,
    heapsort,
    heapsort_minele,
    insert_maxheap,
    insert_minheap,
)


def introduction():
    print("\nTree")
    print("-" * 120)
    print("This Module contains all the algorithm related to the Tree datastructure")
    print("Example of Tree algorithm")

    root = None
    tree = avl_tree()

    x = [20, 40, 10, 25, 5, 15, 28, 4]
    tree.root = tree.Rinsert(root, 30)
    for i in x:
        tree.Rinsert(tree.root, i)

    print("preorder")
    tree.preorder(tree.root)

    print("\ninorder")
    tree.inorder(tree.root)

    print("\npostorder")
    tree.postorder(tree.root)
