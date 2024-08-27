from SparseMartrix.SparseMatrix import Spares
from SparseMartrix.Element import Element

def introduction():
    print("\nSparseMartrix")
    print("-" * 120)
    print("This Module contains all the algorithm related to the SparseMartrix datastructure")
    print("example of SparseMartrix algorithm")
    sparse_a: list[list[int]] = [
        [0, 0, 0, 6, 0, 0],
        [0, 7, 0, 0, 0, 0],
        [0, 2, 0, 5, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [4, 0, 0, 0, 0, 0],
    ]
    sparse_b: list[list[int]] = [
          
        [0, 0, 0, 0, 0, 0],
        [0, 3, 0, 0, 5, 0],
        [0, 0, 2, 0, 0, 7],
        [0, 0, 0, 9, 0, 0],
        [8, 0, 0, 0, 0, 0],
    ]
    print("\nPrinting the coordinate List of the Matrix a ")
    x = Spares(sparse_matrix=sparse_a)
    x.display_coordinate_List()

    print("Printing the compresed sparse row of the Matrix b ")
    y = Spares(sparse_matrix=sparse_b)
    y.display_compresed_sparse_row()

    print("Printing the matrix after the subtraction of a and b")
    z = x.Subtraction_of_sparse(y)
    print(z)