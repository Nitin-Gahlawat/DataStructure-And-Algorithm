# ## Cheacking if a String is palindrome


class Plindrome:
    @staticmethod
    def Plindrome_using_half_list(x :str) -> bool:
        x=list(x.lower()) #converting to lower and list
        for i in range(0,int(len(x)/2)):
            if(x[i] != x[len(x)-i-1]):
                return False
        return True
    
    @staticmethod
    def Plindrome_using_reverseCopy(x :str)-> bool:
        x=list(x.lower())
        y=[0]*(len(x))
        for i in range(len(x)-1,-1,-1):
            y[len(x)-1-i]=x[i]
        for j in range(len(x)):
            if(x[j]!=y[j]):
                return False
        return True
    
    
if __name__=="__main__":
    print(Plindrome.Plindrome_using_half_list("Madam"))
    print(Plindrome.Plindrome_using_reverseCopy("Madam"))

