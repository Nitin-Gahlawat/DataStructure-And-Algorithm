from __future__ import annotations

from SparseMartrix.Element import Element


class Spares:

    def __init__(self: Spares, sparse_matrix: list[list[int]]) -> None:
        self.row: int = len(sparse_matrix)
        self.col: int = len(sparse_matrix[0])
        self.e: list[Element] = self._fill_values(sparse_matrix)
        self.num = len(self.e)

    def _fill_values(self: Spares, n: list[list[int]]) -> list[Element]:
        e: list[Element] = []
        for i in range(len(n)):
            for j in range(len(n[i])):
                if n[i][j] != 0:
                    e.append(Element(i, j, n[i][j]))
        return e

    def __str__(self: Spares) -> str:
        string = " "
        k = 0
        for i in range(self.row):
            for j in range(self.col):
                if k < self.num:
                    if self.e[k].i == i and self.e[k].j == j:
                        string += f" {self.e[k].k} "
                        k += 1
                    else:
                        string += " 0 "
                else:
                    string += " 0 "
            string += " \n "
        return f"row={self.row} col={self.col} num of elements={self.num} \n\nelements= \n{string}"

    def display_coordinate_List(self: Spares) -> None:
        print("*" * 15)
        print(f"* r={self.row} c={self.col} k={self.num} *")
        print("*" * 15)
        for i in range(self.num):
            print("* " + str(self.e[i]) + " *")
        print("*" * 15)
        print("\n", end="")

    def display_compresed_sparse_row(self):
        # Occurence of  elements in ith row of the matrix
        mapele = {}
        for i in range(0, self.num):
            if self.e[i].i not in mapele:
                mapele[self.e[i].i] = 1
            else:
                mapele[self.e[i].i] = mapele[self.e[i].i] + 1

        sum = 0
        print("*" * 30)
        print(f"* element * sum * column_num *")
        print("*" * 30)
        for i in range(self.num):
            if self.e[i].i != self.e[i - 1].i:
                sum = sum + mapele[self.e[i].i]
            print(f"*   {self.e[i].k}    *   {sum}   *      {self.e[i].j}    *")
        print("*" * 30)
        print("\n", end="")

    def coordinate_to_matrix(
        self: Spares, row: int, col: int, c: list[Element]
    ) -> list[list[int]]:
        res = [[0] * col for _ in range(row)]
        k = 0
        for i in range(row):
            for j in range(col):
                if k < len(c):
                    if c[k].i == i and c[k].j == j:
                        # print(f"i=={i} and j=={j}")
                        res[i][j] = c[k].k
                        k += 1
        return res

    def Addition_of_sparse(self: Spares, sparse_matrix: Spares) -> Spares:
        if self.row != sparse_matrix.row or self.col != sparse_matrix.col:
            return None

        elements: list[Element] = []
        x, y = 0, 0

        while self.num > x and sparse_matrix.num > y:
            if self.e[x].i < sparse_matrix.e[y].i:
                elements.append(self.e[x])
                x += 1
            elif self.e[x].i > sparse_matrix.e[y].i:
                elements.append(sparse_matrix.e[y])
                y += 1
            else:
                if self.e[x].j > sparse_matrix.e[y].j:
                    elements.append(sparse_matrix.e[y])
                    y += 1
                elif self.e[x].j < sparse_matrix.e[y].j:
                    elements.append(self.e[x])
                    x += 1
                else:
                    elements.append(
                        Element(
                            self.e[x].i, self.e[x].j, self.e[x].k + sparse_matrix.e[y].k
                        )
                    )
                    x, y = x + 1, y + 1

        while self.num > x:
            elements.append(self.e[x])
            x += 1

        while sparse_matrix.num > y:
            elements.append(sparse_matrix.e[y])
            y += 1

        return Spares(self.coordinate_to_matrix(self.row, self.col, elements))

    def Subtraction_of_sparse(self: Spares, sparse_matrix: Spares) -> Spares:
        if self.row != sparse_matrix.row or self.col != sparse_matrix.col:
            return None

        elements: list[Element] = []
        x, y = 0, 0

        while self.num > x and sparse_matrix.num > y:
            if self.e[x].i < sparse_matrix.e[y].i:
                elements.append(self.e[x])
                x += 1
            elif self.e[x].i > sparse_matrix.e[y].i:
                elements.append(
                    Element(
                        sparse_matrix.e[y].i,
                        sparse_matrix.e[y].j,
                        -1 * sparse_matrix.e[y].k,
                    )
                )
                y += 1
            else:
                if self.e[x].j > sparse_matrix.e[y].j:
                    elements.append(
                        Element(
                            sparse_matrix.e[y].i,
                            sparse_matrix.e[y].j,
                            -1 * sparse_matrix.e[y].k,
                        )
                    )
                    y += 1
                elif self.e[x].j < sparse_matrix.e[y].j:
                    elements.append(self.e[x])
                    x += 1
                else:
                    elements.append(
                        Element(
                            self.e[x].i, self.e[x].j, self.e[x].k - sparse_matrix.e[y].k
                        )
                    )
                    x, y = x + 1, y + 1

        while self.num > x:
            elements.append(self.e[x])
            x += 1

        while sparse_matrix.num > y:
            elements.append(
                Element(
                    sparse_matrix.e[y].i,
                    sparse_matrix.e[y].j,
                    -1 * sparse_matrix.e[y].k,
                )
            )
            y += 1

        return Spares(self.coordinate_to_matrix(self.row, self.col, elements))

