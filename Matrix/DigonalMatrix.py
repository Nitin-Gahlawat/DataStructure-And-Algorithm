# ## Diagonal Matrix


#The given matrix should follow 1 based indexing

########################################
# example of Digonal Matrix
########################################
# [3, 0, 0]
# [0, -2, 0]
# [0, 0, 4]

class DigonalMatrix:
    def __init__(self,n:int):
        self._n=n
        self._A=[0]*n
        
    @staticmethod
    def check(n :list[list[int]]) ->bool:
        for i in range(len(n)):
            for j in range(len(n[i])):
                if(i!=j and n[i][j]!=0):
                    return False
        return True
    def set(self,i:int,j:int,x)->None:
        if(i==j):
            self._A[i-1]=x
    def get(self,i: int,j:int)->int:
        if(i==j):
            return self._A[i-1]
        else:
            return -1
    def Set_From_Matrix(self,n :list[list[int]]) ->None:
          for i in range(0,self._n):
            for j in range(0,self._n):
                    self.set(i+1,j+1,n[i][j])

    def display(self):
        for i in range(1,self._n+1):
            for j in range(1,self._n+1):
                if(i==j):
                    print(self.get(i,j),end=" ")
                else:
                    print(0,end=" ")
            print("\n",end="")
            
if __name__=="__main__":
    x=DigonalMatrix(3)
    x.set(1,1,4)
    x.set(2,2,5)
    x.set(3,3,6)
    # x.Set_From_Matrix([[5,0,0],[0,2,0],[0,0,9]])
    # print(DigonalMatrix.check([[5,0,0],[0,2,0],[0,0,9]]))
    x.display()

