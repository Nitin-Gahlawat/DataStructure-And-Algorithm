from SparceMatrix_Linkedlist.sparse_matrix import (
    Sparse_Matrix,
    Sparse_Matrix_Node,
)


def introduction():
    print("\nSparceMatrix using Linkedlist")
    print("-" * 120)
    print(
        "This Module contains all the algorithm related to the Polynomial using LinkedList datastructure"
    )
    print("example")
    q = Sparse_Matrix(3, 3)
    q.insert_ele(0, 0, 800)
    q.insert_ele(2, 0, 5)
    q.insert_ele(2, 1, 166)

    p = Sparse_Matrix(3, 3)
    p.insert_ele(0, 0, 952)
    p.insert_ele(2, 1, 7)
    p.insert_ele(2, 2, 18)
    print()
    print(f"Conside two Sparse Matrix\n")
    print("*" * 15)
    print(p)
    print("*" * 15)
    print(q)
    x = q.Add(p)
    print(f"Sum of Two Sparse Matrix is \n{x}")
