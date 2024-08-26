import math
class Matrix_Opration:
    @staticmethod
    def transpose(a:list[list[int]])-> list[list[int]]:
        # Initialize c with correct dimensions
        c = [[0]*len(a) for _ in range(len(a[0]))]
        for i in range(len(a)):
            for j in range(len(a[i])):
                c[j][i]=a[i][j]
        return c
    
    @staticmethod
    def smallest_in_each_col(a:list[list[int]])->list[int]:
        # find smallest elemtn of each col
        smallest_ele_col_wise=[]
        for j in range(len(a)):
            temp=a[0][j]
            for i in range(len(a[j])):
                if(temp>a[i][j]):
                    temp=a[i][j]
            smallest_ele_col_wise.append(temp)
        return smallest_ele_col_wise
    
    @staticmethod
    def smallest_in_each_row(a:list[list[int]])->list[int]:
        # find smallest elemtn of each row
        smallest_ele_row_wise=[]
        for i in range(len(a)):
            temp=a[i][0]
            for j in range(len(a[i])):
                if(temp>a[i][j]):
                    temp=a[i][j]
            smallest_ele_row_wise.append(temp)
        return smallest_ele_row_wise
                

    @staticmethod
    def matrix_addtion(a:list[list[int]],b:list[list[int]]):
        if(len(a)!=len(b)  and len(a[0])!=len(b[0])):
            return -1
        c=[]
        for i in range(len(a)):
            temp_lst=[]
            for j in range(len(b[0])):
                temp=0
                for k in range(len(a)):
                    temp+=a[i][k]*b[k][j]
                temp_lst.append(temp)
            c.append(temp_lst)
        return c
    
    @staticmethod
    def matrix_multiplication(a:list[list[int]],b:list[list[int]]):
        if(len(a[0])!=len(b)):
            return -1
        c=[]
        for i in range(len(a)):
            temp_lst=[]
            for j in range(len(b[0])):
                temp=0
                for k in range(len(a)):
                    temp+=a[i][k]*b[k][j]
                temp_lst.append(temp)
            c.append(temp_lst)
        return c
    
    @staticmethod
    def saddle_point(a:list[list[int]]):
        #Find the saddle point of the matrix m(a*b)
        res=float('-inf')
        for i in range(len(a)):
            temp=a[i][0]
            for j in range(len(a[i])):
                if(a[i][j]<temp):
                    temp=a[i][j]
            if(res<temp):
                res=temp
        return res

    def reverse_saddle_point(a:list[list[int]]):
        #Find the saddle point of the matrix m(a*b) [reverse of saddle point]
        res=float('inf')
        for i in range(len(a)):
            temp=a[i][0]
            for j in range(len(a[i])):
                if(a[i][j]>temp):
                    temp=a[i][j]
            if(res>temp):
                res=temp
        return res
    
    def sum_of_reciprocal_of_each_ele(a:list[list[int]]):
        # print sum of square of  reciprocal of each element in a matrix (1/m[i][j])^2
        sum=0
        for i in range(len(a)):
            for j in range(len(a[i])):
                sum+=math.pow((1/a[i][j]),2)
        return sum
    
    def sum_of_upper_half(mat:list[list[int]]):
        #find sum of the upper half of the matrix
        sum=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if(i<=j):
                    sum=sum+mat[i][j]
        return sum
    
    def sum_of_lower_half(mat:list[list[int]]):
        #find sum of the lower half of the matrix
        sum=0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if(i>=j):
                    sum=sum+mat[i][j]
        return sum

    @staticmethod
    def display_matrix(a:list[list[int]])->None:
        for i in a:
            print(i)


if __name__=="__main__":
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    matrix_b = [
        [1,1,1],
        [1,1,1],
        [1,1,1]
    ]            
    # p=Matrix_Opration.transpose([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    # Matrix_Opration.display_matrix(p)

    # p=Matrix_Opration.smallest_in_each_row([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    # Matrix_Opration.display_matrix(p)

    # p=Matrix_Opration.smallest_in_each_col([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    # Matrix_Opration.display_matrix(p)


    p=Matrix_Opration.matrix_addtion(matrix_a,matrix_b)
    Matrix_Opration.display_matrix(p)
    

    # m=Matrix_Opration.matrix_multiplication(matrix_b,matrix_a)
    # Matrix_Opration.display_matrix(m)

    # p=Matrix_Opration.saddle_point([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    # print(p)

    # p=Matrix_Opration.reverse_saddle_point([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    # print(p)

    # sum=Matrix_Opration.sum_of_reciprocal_of_each_ele(matrix_a)
    # print(sum)

    # sum=Matrix_Opration.sum_of_upper_half(matrix_b)
    # print(sum)
    
    # sum=Matrix_Opration.sum_of_lower_half(matrix_b)
    # print(sum)

