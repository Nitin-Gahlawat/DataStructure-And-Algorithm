# ## Finding A reverse of a string 


class Reverse:
    def reverseStr_meth1(x :str):
        final=""
        for i in range(len(x)-1,-1,-1):
            final+=x[i]
        return final
    def reverseStr_meth2(x :str):
        i,j=0,len(x)-1
        x=list(x) ##converting the string x in the list form so that we can edit it as 
        while(i<j):
            temp=x[i]
            x[i]=x[j]
            x[j]=temp
            i,j=i+1,j-1
        return "".join(x)
    
if __name__=="__main__":
    print(Reverse.reverseStr_meth1("Python"))
    print(Reverse.reverseStr_meth2("Python"))


