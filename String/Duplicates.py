
# ## Finding duplicates in a string


class Duplicates:
    @staticmethod
    def finding_duplicates_meth1(x :str):
        count_map={}
        x=list(x)
        for i in range(0,len(x)):
            ct=1
            if(x[i]=="0"):
                continue
            for j in range(i+1,len(x)):
                if(x[j]==x[i]):
                    x[j]="0"
                    ct=ct+1
            count_map[x[i]]=ct
        return count_map

    #using HashMap for Finding Duplicate element
    @staticmethod
    def finding_duplicates_meth2(x :str):
        hash_map=[]
        count_map={}
        x=x.lower()
        ##initlizing the array for the 26 lowercase english alphabet
        for i in range(0,26):
            hash_map.append(0)
        for j in range(0,len(x)):
            hash_map[ord(x[j])-ord('a')]=hash_map[ord(x[j])-ord('a')]+1
        for k in range(0,len(hash_map)):
            if(hash_map[k]!=0):
                count_map[chr(k+ord('a'))]=hash_map[k]
        return count_map
    
    #duplicate element using BitWise oprators
    @staticmethod
    def BitWise_finding_duplicates(x: str):
        h=0
        mapele={}
        for i in range(len(x)): 
            if(((1<<ord(x[i])-ord('a'))& h)>0):
                mapele[chr(ord(x[i]))]=mapele[chr(ord(x[i]))] +1
            else:
                h=(1<<(ord(x[i])-ord('a')) | h)
                mapele[chr(ord(x[i]))]=1
        return mapele
    
if __name__=="__main__":
    print(Duplicates.finding_duplicates_meth1("finding"))
    print(Duplicates.finding_duplicates_meth2("finding"))
    print(Duplicates.BitWise_finding_duplicates("finding"))


