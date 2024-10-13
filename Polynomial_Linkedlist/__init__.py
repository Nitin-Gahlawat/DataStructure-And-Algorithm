from Polynomial_Linkedlist.polynomial import Polynomial, Node_Polynomial


def introduction():
    print("\nPolynomial using Linkedlist")
    print("-" * 120)
    print(
        "This Module contains all the algorithm related to the Polynomial using LinkedList datastructure"
    )
    print("example")
    p = Polynomial([4, 3], [9, 2], [6, 1], [7, 0])
    q = Polynomial([5, 4], [7, 3], [9, 1])
    print(f"Conside two polnomial {p} and {q}")
    x = q.addition(p)
    print(f"Sum of Two Polynomial is {x}")
