
# # Sum of pair such that i+j=k (say k=10 )

## Meth1 pair of elements with sum k unsorted array (say k==10)
## O(N*N)=O(N^2)
def sum_pair(a :list[int],k) -> list[list[int]]:
    sum_ele=[]
    for i in range(len(a)):
        left=k-a[i]
        for j in range(i+1,len(a)):
            if(left==a[j]):
                sum_ele.append([a[i],left])
    return sum_ele  

## Meth2 pair of elements with sum k in unsorted array (say k==10) using hashtable
# O(N^2)=O(N**2)
def sum_pair_hash(a :list[int],k :int)->list[list[int]]:
    hash_table=[]
    pair=[]
    for i in range(max(a)+1):
        hash_table.append(0)
    for i in a:
        hash_table[i]=hash_table[i]+1
        if(hash_table[k-i]>0 and i!=(k-i)):
            pair.append([i,k-i])
            hash_table[i],hash_table[k-i]=hash_table[i]-1,hash_table[k-i]-1
    return pair

## Meth2 pair of elements with sum k in sorted array (say k==10)
def sum_pair_sorted(a:list[int],k)->list[list[int]]:
    pair=[]
    i,j=0,len(a)-1
    while(i<j):
        if(a[i]+a[j]>k):
            j=j-1
        elif(a[i]+a[j]<k):
            i=i+1
        else:
            pair.append([a[i],a[j]])
            i,j=i+1,j+1
    return pair

if __name__=="__main__":
    print(sum_pair([6,3,8,10,4,16,7,5,2,9,14],10))
    print(sum_pair_hash([6,3,8,10,4,16,7,5,2,9,14],10) )        
    print(sum_pair_sorted([2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16],10))

