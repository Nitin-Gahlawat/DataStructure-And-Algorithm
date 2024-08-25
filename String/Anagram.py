# ## Cheacking if the strings are Anagram or not

class Anagram:
    #O(n*n)==> O(n^2) Time
    @staticmethod
    def Anagram_meth1(x: str,y :str):

        ##converting to the List because i am considering the presence of Duplicate element in any string
        x=list(x.lower())
        y=list(y.lower())        

        if(len(x)!=len(y)):
            return False
        for i in range(len(x)):
            isChar=False
            for j in range(len(y)):
                if(x[i]==y[j]):
                    isChar=True
                    y[j]="0"            ##using this because there my be Duplicate element
                    break
            if(not isChar):
                return False
        return True
    
    @staticmethod
    def Anagram_meth2(x: str,y :str):
        hash_map=[]
        count_map={}
        x=list(x.lower())
        y=list(y.lower())
        
        for i in range(0,26):
            hash_map.append(0)
            
        for i in range(len(x)):
            hash_map[ord(x[i])-ord('a')]=hash_map[ord(x[i])-ord('a')]+1
        for j in range(len(y)):
            hash_map[ord(y[j])-ord('a')]=hash_map[ord(y[j])-ord('a')]-1

        for k in range(len(hash_map)):
            if(hash_map[k]<0):
                count_map[chr(k+ord('a'))]=hash_map[k]
            if(hash_map[k]>0):
                count_map[chr(k+ord('a'))]=hash_map[k]
        return count_map
    
    @staticmethod
    def Anagram_bits(x :str,y :str):
        if(len(x)!=len(y)):
            return False
        a,b=0,0
        for i in range(len(x)):
            a=(1<<ord(x[i])-ord('a')) | a
        for i in range(len(y)):
            b=(1<<ord(y[i])-ord('a')) | b
        if((a ^ b)>0):
            return False
        else:
            return True

if __name__=="__main__":
    p=Anagram.Anagram_meth1("decamal","medical")
    print(p)
    p=Anagram.Anagram_meth2("decamal","medical")
    print(p)
    p=Anagram.Anagram_bits("decimal","medical")
    print((p))
