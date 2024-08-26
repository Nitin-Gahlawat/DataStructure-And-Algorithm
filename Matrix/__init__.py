from Matrix.DigonalMatrix import DigonalMatrix
from Matrix.LowerTriangular import Lower_Triangular
from Matrix.MatrixOpration import Matrix_Opration
from Matrix.SymmetricMatrix import Symmetric_Matrix
from Matrix.ToeplitzMatrix import Toeplitz_matrix
from Matrix.TridiagonalMatrix import Tridiagonal_matrix
from Matrix.UpperTriangular import Upper_Triangular


def introduction():
    print("\nMatrix")
    print("-" * 120)
    print("This Module Contains all the algorithm related to the Matrix datastructure")
    print("example of Matrix algorithm")
    print(
        "\nStoring the Multidimensional Diagonal matrix into a single dimensional array"
    )
    mat = [[2, 0, 0], [0, 3, 0], [0, 5, 0]]
    print(f"\nthe multi  matrix is {mat}")
    x = DigonalMatrix(3)
    x.Set_From_Matrix(mat)
    print("\nThe final matrix is ")
    x.display()

    print(
        "There are various type of matrix implementations eg. DigonalMatrix,Lower_Triangular,Upper_Triangular,Symmetric_Matrix,Toeplitz_matrix,Tridiagonal_matrix"
    )
