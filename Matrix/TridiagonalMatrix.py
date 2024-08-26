
# ## Tridiagonal Matrix


#The given matrix should follow 1 based indexing
########################################
# example of Tridiagonal  matrix
########################################
# [[2,3,0,0,0],
# [7,2,3,0,0],
# [0,7,2,3,0],
# [0,0,7,2,3],
# [0,0,0,7,2]]

class Tridiagonal_matrix:
    
    def __init__(self,n:int):
        #matrix width
        self._n=n
        self._A=[0]*(3*n-2)      # Creating a list of size (3*n-2)
        
    def set(self,i:int,j:int,x)->None:
        if(i-j==1):
            self._A[j-1]=x
        elif(i==j):
            self._A[(self._n-1)+(i-1)]=x
        elif(j-i==1):
            self._A[(2*self._n-1)+(i-1)]=x
            
    def get(self,i: int,j:int)->int:
        if(i-j==1):
            return self._A[j-1]
        elif(i==j):
            return self._A[(self._n-1)+(i-1)]
        elif(j-i==1):
            return self._A[(2*self._n-1)+(i-1)]
        else:
            return 0
            
    def Set_From_Matrix(self,n :list[list[int]]) ->None:
          for i in range(0,self._n):
            for j in range(0,self._n):
                if(i==j or i-j==1 or j-i==1):
                    #given +1 because internal set method follow 1 based indexing 
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
                if(i==j or i-j==1 or j-i==1):
                    if(n[i+1][j+1]!=n[i][j]):
                        return False
        return True
if __name__=="__main__":        
    x=Tridiagonal_matrix(5)
    x.Set_From_Matrix([[2,3,0,0,0],
                    [7,2,3,0,0],
                    [0,7,2,3,0],
                    [0,0,7,2,3],
                    [0,0,0,7,2]])
    x.display()
