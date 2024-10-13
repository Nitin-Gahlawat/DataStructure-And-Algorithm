from __future__ import annotations


class Sparse_Matrix_Node:
    def __init__(self, col, val, link=None) -> None:
        self.col: int = col
        self.val: int = val
        self.link: Sparse_Matrix_Node = link


# Sparse matrix
class Sparse_Matrix:
    def __init__(self, matrix_row, matrix_col) -> None:
        self.matrix_row = matrix_row
        self.matrix_col = matrix_col
        self.x: Sparse_Matrix_Node = [None] * self.matrix_row

    # Time Complexity O(n)
    def insert_ele(self, row: int, col: int, val: int):
        if row >= self.matrix_row or col >= self.matrix_col:
            raise Exception("The row or col is out of range")

        if self.x[row] is None:
            self.x[row] = Sparse_Matrix_Node(col, val, None)
            return

        current = self.x[row]
        new_node = Sparse_Matrix_Node(col, val, None)

        if col < current.col:
            new_node.link = current.link
            self.x[row] = new_node  # Update the head of the list
            return

        while current.link is not None and col >= current.link.col:
            current = current.link

        if current.link is None:
            current.link = new_node
        else:
            new_node.link = current.link
            current.link = new_node

    # Time Complexity O(n)
    def __str__(self) -> str:
        res = ""
        for i in range(0, self.matrix_row):
            temp = self.x[i]
            # print(i, temp)
            for j in range(0, self.matrix_col):
                if temp != None and temp.col == j:
                    res += f" {temp.val} \t"
                    temp = temp.link
                else:
                    res += f" {0} \t"
            res += "\n"
        return res

    # Time Complexity O(n^2)
    def Add(self, matrix2: Sparse_Matrix):
        if (self.matrix_row != matrix2.matrix_row) or (
            self.matrix_col != matrix2.matrix_col
        ):
            raise Exception(
                "the row and columns of the first matrix does not match the second matrix"
            )

        final_mat: Sparse_Matrix_Node = [None] * self.matrix_row
        for i in range(self.matrix_row):
            x = self.x[i]
            y = matrix2.x[i]
            head = None
            ptr = None
            while (x is not None) and (y is not None):
                if x.col == y.col:
                    new_node = Sparse_Matrix_Node(x.col, x.val + y.val, None)
                    x = x.link
                    y = y.link
                elif x.col < y.col:
                    new_node = Sparse_Matrix_Node(x.col, x.val, None)
                    x = x.link
                elif x.col > y.col:
                    new_node = Sparse_Matrix_Node(y.col, y.val, None)
                    y = y.link

                if ptr == None:
                    ptr = new_node
                    head = ptr
                    continue
                ptr.link = new_node
                ptr = new_node

            while x is not None:
                new_node = Sparse_Matrix_Node(x.col, x.val, None)
                if ptr is None:
                    head = new_node
                    ptr = head
                else:
                    ptr.link = new_node
                    ptr = new_node
                x = x.link

            while y is not None:
                new_node = Sparse_Matrix_Node(y.col, y.val, None)
                if ptr is None:
                    head = new_node
                    ptr = head
                else:
                    ptr.link = new_node
                    ptr = new_node
                y = y.link

            final_mat[i] = head

        m = Sparse_Matrix(self.matrix_row, self.matrix_col)
        m.x = final_mat
        return m

    # Time Complexity O(n^2)
    def Sub(self, matrix2: Sparse_Matrix):
        if (self.matrix_row != matrix2.matrix_row) or (
            self.matrix_col != matrix2.matrix_col
        ):
            raise Exception(
                "the row and columns of the first matrix does not match the second matrix"
            )

        final_mat: Sparse_Matrix_Node = [None] * self.matrix_row
        for i in range(self.matrix_row):
            x = self.x[i]
            y = matrix2.x[i]
            head = None
            ptr = None
            while (x is not None) and (y is not None):
                if x.col == y.col:
                    new_node = Sparse_Matrix_Node(x.col, x.val - y.val, None)
                    x = x.link
                    y = y.link
                elif x.col < y.col:
                    new_node = Sparse_Matrix_Node(x.col, x.val, None)
                    x = x.link
                elif x.col > y.col:
                    new_node = Sparse_Matrix_Node(y.col, -y.val, None)
                    y = y.link

                if ptr == None:
                    ptr = new_node
                    head = ptr
                    continue
                ptr.link = new_node
                ptr = new_node

            while x is not None:
                new_node = Sparse_Matrix_Node(x.col, x.val, None)
                if ptr is None:
                    head = new_node
                    ptr = head
                else:
                    ptr.link = new_node
                    ptr = new_node
                x = x.link

            while y is not None:
                new_node = Sparse_Matrix_Node(y.col, -y.val, None)
                if ptr is None:
                    head = new_node
                    ptr = head
                else:
                    ptr.link = new_node
                    ptr = new_node
                y = y.link

            final_mat[i] = head

        m = Sparse_Matrix(self.matrix_row, self.matrix_col)
        m.x = final_mat
        return m


if __name__ == "__main__":
    matrix = Sparse_Matrix(3, 3)
    matrix.insert_ele(0, 0, 800)
    matrix.insert_ele(2, 0, 5)
    matrix.insert_ele(2, 1, 166)
    print("x matrix is ")
    print(matrix)
    print("*" * 15)

    y = Sparse_Matrix(3, 3)
    y.insert_ele(0, 0, 10)
    y.insert_ele(0, 1, 32)
    y.insert_ele(0, 2, 300)
    print("y matrix is ")
    print(y)
    print("*" * 15)

    print("result matrix is ")
    m = y.Add(matrix)
    print(m)
