
# ## Toeplitz  matrix   


#The given matrix should follow 1 based indexing
########################################
# example of Toeplitz  Matrix
########################################
# [2,3,4,5,6]
# [7,2,3,4,5]
# [8,7,2,3,4]
# [9,8,7,2,3]
# [1,9,8,7,2]

class Toeplitz_matrix:
    def __init__(self,n:int):
        self._n=n
        self._A=[0]*int(2*n-1)      # Creating a list of size i+j-1
        
    def set(self,i:int,j:int,x)->None:
        if(i<j):
            self._A[j-1]=x
        elif(i==j):
            self._A[i-j]=x
        elif(i>j):
            self._A[(self._n-1)+(i-1)]=x
            
    def get(self,i: int,j:int)->int:
        if(i<j):
            return self._A[j-i]
        elif(i==j):
            return self._A[i-j]
        elif(i>j):
            return self._A[(self._n-1)+(i-j)]
            
            
    def Set_From_Matrix(self,n :list[list[int]]) ->None:
          for i in range(0,self._n):
            for j in range(0,self._n):
                if(i==0 or j==0):
                    self.set(i+1,j+1,n[i][j])
                
    def display(self):
        for i in range(1,self._n+1):
            for j in range(1,self._n+1):
                print(self.get(i,j),end=" ")
            print("\n",end="")
            
    @staticmethod
    def Check(n :list[list[int]]) ->bool:
        for i in range(0,len(n)-1):
            for j in range(0,len(n[i])-1):
                if(n[i][j]!=n[i+1][j+1]):
                    return False
        return True
if __name__=="__main__":
    x=Toeplitz_matrix(5)
    x.Set_From_Matrix([[2,3,4,5,6],
                    [7,2,3,4,5],
                    [8,7,2,3,4],
                    [9,8,70,2,3],
                    [1,9,8,7,2]])
    x.display()

