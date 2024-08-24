
# # Finding min and max in one traversal


## finding min and max in one scan of the element of list
def find_min_max(a :list[int])->tuple[int,int]:
    min,max=a[0],a[0]
    for i in a:
        if(min>i):
            min=i
        elif(max<i):
            max=i
    return min,max
if __name__=="__main__":
    print(find_min_max([2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16]))
