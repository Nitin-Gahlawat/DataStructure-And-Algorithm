
# ## Triangular Matrix


#The given matrix should follow 1 based indexing
########################################
# example of Lower Triangular Matrix
########################################
# [[1, 0, 0, 0, 0]
# [2, 3, 0, 0, 0]
# [4, 5, 6, 0, 0]
# [7, 8, 9, 10, 0]
# [11, 12, 13, 14, 15]]
class Lower_Triangular():
    
    def __init__(self,n:int):
        self._n=n
        self._A=[0]*int(n*(n+1)/2)        # Creating a list of size int(i*(i+1)/2) 

    @staticmethod
    def Check(n :list[list[int]]) ->bool:
        for i in range(len(n)):
            for j in range(len(n[i])):
                if(i<j and n[i][j]!=0):
                    return False
        return True
    
    def Set_From_Matrix_row_major(self,n :list[list[int]]) ->None:
        for i in range(0,self._n):
            for j in range(0,self._n):
                    if(i>=j):
                        self.set_row_major(i+1,j+1,n[i][j]) 

    def set_row_major(self,i:int,j:int,x)->None:
        if(i>=j):
            self._A[int(i*(i-1)/2)+j-1]=x
            
    def get_row_major(self,i: int,j:int)->int:
        if(i>=j):
            return self._A[int(i*(i-1)/2)+j-1]
        else:
            return -1
    
    def display_row_major(self):
        for i in range(1,self._n+1):
            for j in range(1,self._n+1):
                if(i>=j):
                    print(self.get_row_major(i,j),end=" ")
                else:
                    print(0,end=" ")
            print("\n",end="")

    def set_col_major(self,i:int,j:int,x)->None:
        if(i>=j):
            self._A[int((j-1)*(2*self._n-j+2)/2)+(i-j)]=x

    def Set_From_Matrix_col_major(self,n :list[list[int]]) ->None:
        for i in range(0,self._n):
            for j in range(0,self._n):
                    self.set_col_major(i+1,j+1,n[i][j]) 
            
    def get_col_major(self,i: int,j:int)->int:
        if(i>=j):
            return self._A[int((j-1)*(2*self._n-j+2)/2)+(i-j)]
        else:
            return -1
        
    def display_col_major(self):
        for i in range(1,self._n+1):
            for j in range(1,self._n+1):
                if(i>=j):
                    print(self.get_col_major(i,j),end=" ")
                else:
                    print(0,end=" ")
            print("\n",end="")

if __name__=="__main__":         
    x=Lower_Triangular(3)
    x.Set_From_Matrix_row_major([[2, 0, 0],
                                [5, 1, 0],
                                [7, 3, 4]])
    x.display_col_major()

    print(Lower_Triangular.Check([[2, 0, 0],
                                [5, 1, 9],
                                [7, 3, 4]]))

    y=Lower_Triangular(5)
    y.Set_From_Matrix_col_major([[1, 0, 0, 0, 0],
                                [2, 3, 0, 0, 0],
                                [4, 5, 6, 0, 0],
                                [7, 8, 9, 10, 0],
                                [11, 12, 13, 14, 15]])
    y.display_col_major()

