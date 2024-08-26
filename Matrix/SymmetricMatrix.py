
# ## Symmetric matrix


#The given matrix should follow 1 based indexing
########################################
# example of Symmetric Matrix

########################################
# [2,3,4,5,6]
# [7,2,3,4,5]
# [8,7,2,3,4]
# [9,8,7,2,3]
# [1,9,8,7,2]

class Symmetric_Matrix:
    
    def __init__(self,n:int):
        self._n=n
        self._A=[0]*int(n*(n+1)/2)        # Creating a list of size int(i*(i+1)/2) 

        
    def set(self,i:int,j:int,x)->None:
        if(i>=j):
            self._A[int(i*(i-1)/2)+j-1]=x

    def Set_From_Matrix(self,n :list[list[int]]) ->None:
        for i in range(0,self._n):
            for j in range(0,self._n):
                    self.set(i+1,j+1,n[i][j])   

    def get(self,i: int,j:int)->int:
        if(i>=j):
            return self._A[int(i*(i-1)/2)+j-1]
        else:
            return -1
    
    def display(self):
        for i in range(1,self._n+1):
            for j in range(1,self._n+1):
                if(i>=j):
                    print(self.get(i,j),end=" ")
                else:
                    print(self.get(j,i),end=" ")
            print("\n",end="")

    @staticmethod
    def Check(n :list[list[int]]) ->bool:
        for i in range(0,len(n)-1):
            for j in range(0,len(n[i])-1):
                if(n[i][j]!=n[j][i]):
                    return False
        return True

if __name__=="__main__":
    x=Symmetric_Matrix(5)
    x.Set_From_Matrix([ [2,3,4,5,6],
    [7,2,3,4,5],
    [8,7,2,3,4],
    [9,8,7,2,3],
    [1,9,8,7,2]])
    x.display()
