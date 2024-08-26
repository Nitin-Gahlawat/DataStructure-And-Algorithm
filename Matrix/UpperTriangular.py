

#The given matrix should follow 1 based indexing
########################################
# example of Upper Triangular Matrix
########################################
# [1, 2, 3, 4, 5]
# [0, 6, 7, 8, 9]
# [0, 0, 10, 11, 12]
# [0, 0, 0, 13, 14]
# [0, 0, 0, 0, 15]

class Upper_Triangular():
    
    def __init__(self,n:int):
        self._n=n
        self._A=[0]*int(n*(n+1)/2)        # Creating a list of size int(i*(i+1)/2) 

    @staticmethod
    def Check(n :list[list[int]]) ->bool:
        for i in range(len(n)):
            for j in range(len(n[i])):
                if(i>j and n[i][j]!=0):
                    return False
        return True
    
    def set_From_Matrix_col_major(self,n :list[list[int]]) ->None:
        for i in range(0,self._n):
            for j in range(0,self._n):
                if(i<=j):
                    self.set_col_major(i+1,j+1,n[i][j]) 

    def set_col_major(self,i:int,j:int,x)->None:
        if(i<=j):
            self._A[int(j*(j-1)/2)+i-1]=x
            
    def get_col_major(self,i: int,j:int)->int:
        if(i<=j):
            return self._A[int(j*(j-1)/2)+i-1]
        else:
            return -1
    
    def display_col_major(self):
        for i in range(1,self._n+1):
            for j in range(1,self._n+1):
                if(i<=j):
                    print(self.get_col_major(i,j),end=" ")
                else:
                    print(0,end=" ")
            print("\n",end="")

    def set_row_major(self,i:int,j:int,x)->None:
        if(i<=j):
            self._A[int((i-1)*(2*self._n-i+2)/2)+(j-i)]=x

    def set_From_Matrix_row_major(self,n :list[list[int]]) ->None:
        for i in range(0,self._n):
            for j in range(0,self._n):
                    self.set_row_major(i+1,j+1,n[i][j]) 
            
    def get_row_major(self,i: int,j:int)->int:
        if(i<=j):
            return self._A[int((i-1)*(2*self._n-i+2)/2)+(j-i)]
        else:
            return -1
        
    def display_row_major(self):
        for i in range(1,self._n+1):
            for j in range(1,self._n+1):
                if(i<=j):
                    print(self.get_row_major(i,j),end=" ")
                else:
                    print(0,end=" ")
            print("\n",end="")    
              
if __name__=="__main__":  
    x=Upper_Triangular(3)
    mat=[[2, 5, 2],
        [0, 1, 9],
        [0, 0, 4]]
    x.set_From_Matrix_row_major(mat)
    x.display_row_major()
    matrix_m=[[1, 2, 3, 4, 5],
                                [0, 6, 7, 8, 9],
                                [0, 0, 10, 11, 12],
                                [0, 0, 0, 13, 14],
                                [0, 0, 0, 0, 15]]
    print(Upper_Triangular.Check(matrix_m))
    y=Upper_Triangular(5)
    y.set_From_Matrix_col_major(matrix_m)
    y.display_col_major()

