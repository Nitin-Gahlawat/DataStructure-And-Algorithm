
# ### Set oprations on the Array elements
# ### [union,Intersction,Diffrence]


class SetOpration:

    ## finding the union of the Two unsorted array
    @staticmethod
    def union_unsorted(a: list[int],b: list[int]) -> list[int]:
        c=[]
        for i in a:
            c.append(i)
        for j in b:
            temp=True
            for m in a:
                if(j==m):
                    temp=False
                    break
            if temp:
                c.append(j)
        return c
    
    ## finding the union of the Two sorted array
    @staticmethod
    def union_sorted(a: list[int],b: list[int]) -> list[int]:
        c=[]
        i,j=0,0
        while(i < len(a) and j < len(b)):
            if(a[i]==b[j]):
                c.append(b[j])
                i,j=i+1,j+1
            elif(a[i]<b[j]):
                c.append(a[i])
                i=i+1
            else:
                c.append(b[j])
                j=j+1
        while(i < len(a)):
            c.append(a[i])
            i=i+1
        while(j < len(b)):
            c.append(b[j])
            j=j+1
        return c
    
    ## finding the Intersection of the Two unsorted array
    @staticmethod
    def Intersection_unsorted(a: list[int],b: list[int]) -> list[int]:
        c=[]
        for j in a:
            temp=False
            for m in b:
                if(j==m):
                    temp=True
                    break
            if temp:
                c.append(j)
        return c
    
    ## finding the Intersection of the Two sorted array
    @staticmethod
    def Intersection_sorted(a: list[int],b: list[int]) -> None:
        c=[]
        i,j=0,0
        while(i < len(a) and j < len(b)):
            if(a[i]==b[j]):
                c.append(b[j])
                i,j=i+1,j+1
            elif(a[i]<b[j]):
                i=i+1
            else:
                j=j+1
        return c
    
    ## finding the Diffence of the Two unsorted array
    @staticmethod
    def Diffrence_unsorted(a: list[int],b: list[int]) -> list[int]:
        c=[]
        for j in a:
            temp=True
            for m in b:
                if(j==m):
                    temp=False
                    break
            if temp:
                c.append(j)
        return c
    
    ## finding the Diffence of the Two sorted array
    @staticmethod
    def Diffrence_sorted(a: list[int],b: list[int]) -> list[int]:
        c=[]
        i,j=0,0
        while(i < len(a) and j < len(b)):
            if(a[i]==b[j]):
                i,j=i+1,j+1
            elif(a[i]<b[j]):
                c.append(a[i])
                i=i+1
            else:
                j=j+1
        while(i < len(a)):
            c.append(a[i])
            i=i+1
        return c
    
if __name__=="__main__":
    print(SetOpration.union_unsorted([1,2,3,4,5,6],[4,5,6,7,8,9]))
    print(SetOpration.union_sorted([1,2,3,4,5,6],[4,5,6,7,8,9]))
    print(SetOpration.Intersection_unsorted([1,2,3,4,5,6],[4,5,6,7,8,9]))
    print(SetOpration.Intersection_sorted([1,2,3,4,5,6],[4,5,6,7,8,9]))
    print(SetOpration.Diffrence_unsorted([1,2,3,4,5,6],[4,5,6,7,8,9]))
    print(SetOpration.Diffrence_sorted([4,5,6,7,8,9],[1,2,3,4,5,6]))

