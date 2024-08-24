
# # Missing element


## single missing element in a sorted array
def missing_element_sorted_meth1(a: list[int]) -> int:
    natural_sum=a[-1]*((a[-1]+1)/2) ## sum of n natural number n*((n+1)/2)
    array_sum=0
    for i in a:
        array_sum+=i
    return natural_sum-array_sum

##This algorithm finds the missing element or a range of missing element
def missing_element_sorted_meth2(a :list[int]) -> list[int]:
    c=[]
    l,h,n=a[0],a[-1],len(a)
    diff=a[0]
    for i in range(0,n):
        if((a[i]-i)!=diff):
            new_diff=a[i]-i
            for j in range(diff,new_diff):
                c.append(j+i)
            diff=new_diff
    return c
    
## using hash table(or bitset) fing the missing element in a unsorted array
def missing_element_unsorted(a :list[int]) -> list[int]:
    hash_table=[]
    missing=[]
    for i in range(max(a)+1):
        hash_table.append(0)
    for i in a:
        hash_table[i]=hash_table[i]+1
    for i in range(min(a),max(a)+1):
        if(hash_table[i]==0):
            missing.append(i)
    return missing

if __name__=="__main__":
    print(missing_element_sorted_meth1([1,2,3,4,5,6,7,9,10]))
    print(missing_element_sorted_meth2([6,7,8,9,10,20,26,27]))
    print(missing_element_unsorted([12,3,5,4,10]))
