
# ## Basic Opration on a string


class BasicOprations:
    @staticmethod
    def Insert(x :str,y:int,z: str):
        x=list(x)
        x.append("")
        for i in range(len(x)-1,y,-1):
            x[i]=x[i-1]
        x[i]=z
        return "".join(x)
    
    @staticmethod
    def Delete(x :str,start:int,end:int):
        if(0<=start<=len(x) and 0<=end<=len(x) and start<end):
            x=list(x)
            y=[]
            for i in range(0,start):
                y.append(x[i])

            for j in range(end+1,len(x)):
                y.append(x[j])

            return "".join(y)
        else:
            raise IndexError(f"The index {start} and {end} is out of range.")
    @staticmethod
    def Substring(x :str,start:int,end:int):
        if(0<=start<=len(x) and 0<=end<=len(x) and start<end):
            x=list(x)
            y=[]
            for i in range(start,end):
                y.append(x[i])
            return "".join(y)
        else:
            raise IndexError(f"The index {start} and {end} is out of range.")

    @staticmethod
    def CountVowals(x :str):
        vowals=['a','e','i','o','u']
        vct=0
        ct=0
        x=x.lower()
        for i in x:
            if(i==" "):
                continue
            for j in vowals:
                if(i==j):
                    vct=vct+1
                    break
            else:
                ct=ct+1  
                
        return vct,ct
    
    @staticmethod
    def countwords(x :str):
        ct=0
        for i in range(1,len(x)):
            if(x[i]==" " and not x[i-1]==" "):
                ct=ct+1
        return ct+1

    @staticmethod
    ## Code for Cheack the Valid string
    def isvalidStr(x :str):
        for i in x:
            if(not (i >='a' and i<='z') and not (i >='A' and i<='Z') and not (i >='0' and i<='9') and not (i==" ")):
                return False
        return True

    @staticmethod
    ## Code for Cheack the Comparing two strings
    def Compare(x :str, y:str) -> int:
        i,j=0,0
        x=x.lower()
        y=y.lower()
        while(len(x)!=i and len(y)!=j):
            if(x[i]!=y[j]):
                if(x[i]>y[j]):
                    return 1
                else:
                    return -1
            i,j=i+1,j+1
        if(len(x)!=i):
            return 1
        if(len(y)!=j):
            return -1
        return 0
    

if __name__=="__main__":
    print(BasicOprations.Insert("good moring you",10," to"))
    print(BasicOprations.Delete("hello world",2,4))
    print(BasicOprations.Substring("hello  world",5,12))
    print(BasicOprations.CountVowals("How Are you"))
    print(BasicOprations.countwords("How Areyou ?"))
    print(BasicOprations.isvalidStr("ello #world"))
    print(BasicOprations.Compare("hell52","hello"))


