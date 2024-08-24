

# # Duplicate elements count


## Meth1 of counting sorted element in array
#O(n)
def duplicate_sorted(a :list[int])->dict[int,int]:
    mapele={}
    ct=1
    for i in range(len(a)-1):
        if(a[i]==a[i+1]):
            ct=ct+1
            mapele[a[i]]=ct
        else:
            ct=1
    return mapele

## Meth2 of counting sorted element in array
##O(n)
def duplicate_sorted_meth2(a :list[int])->dict[int,int]:
    mapele={}
    i=0
    while(i<len(a)-1):
        if(a[i]==a[i+1]):
            j=i
            while(a[i]==a[j]):
                j=j+1
            mapele[a[i]]=j-i
            i=j
        i=i+1
    return mapele

## Meth3 of counting sorted element in array using Hashing
## O(n)
def duplicate_sorted_meth3(a :list[int])->dict[int,int]:
    hash_table=[]
    duplicate_times={}
    for i in range(max(a)+1):
        hash_table.append(0)
    for i in a:
        hash_table[i]=hash_table[i]+1
    for i in range(min(a),max(a)+1):
        if(hash_table[i]>1):
            duplicate_times[i]=hash_table[i]
    return duplicate_times


## Meth1 of counting unsorted element in array
def duplicate_unsorted(a :list[int])->dict[int,int]:
    mapele={}
    for i in range(len(a)):
        count=1
        if(a[i]!= -1):                     ##does not including -1 in count array
            for j in range(i+1,len(a)):
                if(a[i]==a[j]):
                    a[j]=-1                  ##replacing it with -1 because the element may be counted  multiple times
                    count=count+1
            mapele[a[i]]=count
    return mapele

## Meth2 of unsorted element in array using Hash table
def count_elements_unsorted(a :list[int]) -> dict[int,int]:
    hash_table=[]
    missing={}
    for i in range(max(a)+1):
        hash_table.append(0)
    for i in a:
        hash_table[i]=hash_table[i]+1
    for i in range(min(a),max(a)+1):
        if(hash_table[i]>0):
            missing[i]=hash_table[i]
    return missing

if __name__=="__main__":
    print(duplicate_sorted([3,6,8,8,10,12,15,15,15,20]))
    print(duplicate_sorted_meth2([8,8,10,11,12,13,14,15,15,15,15,20,200]))
    print(duplicate_sorted_meth3([8,8,10,11,12,13,14,15,15,15,15,20,200]))
    print(duplicate_unsorted([8,3,6,4,6,5,6,8,2,7]))
    print(count_elements_unsorted([12,12,3,5,4,10]))

