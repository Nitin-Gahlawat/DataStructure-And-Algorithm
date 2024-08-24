from __future__ import annotations
from .ArrayClass import Array


# ## Searching in a array



class Searching:

    @staticmethod
    def linearSearch(x:Array,key:int):
        if (x.isDuplicate()):
            raise Exception("The array contains the duplicate element")
        for i in range(0,len(x)):
            if (x.arr[i] == key):
                return i
        return -1

    @staticmethod
    def TranspositionLinearSearch(x:Array,key:int):
        if (x.isDuplicate()):
            raise Exception("The array contains the duplicate element")
        
        for i in range(0,len(x)):
            if (x.arr[i] == key):
                #  Swap logic
                element = x.arr[i]
                x.arr[i]= x.arr[i - 1]
                x.arr[i - 1]=element
                return i - 1
        return -1
        
    @staticmethod
    def moveToHeadLinearSearch(x:Array,key:int):
        if (x.isDuplicate()):
            raise Exception("The array contains the duplicate element")
        
        for i in range(0,len(x)):
            if (x.arr[i] == key):
                #  Swap logic
                element = x.arr[i]
                x.arr[i]= x.arr[0]
                x.arr[0]= element
                return 0
        return -1

    @staticmethod
    def binarySearch(x:Array,key, l, h):  #requires a sorted array for working
        if not x.is_sorted():
            raise Exception("The array is not sorted")
            return -1
        else:
            while (l <= h):
                mid =int((l + h) / 2)
                if (x.arr[mid] == key):
                    return mid
                elif (key > x.arr[mid]):
                    l = mid + 1
                else:
                    h = mid - 1
            return -1

    @staticmethod
    def binarySearchRecursive(x:Array,key, low, high):  #requires a sorted array for working
        if (low <= high):
            mid =int((low + high) / 2)
            if (x.arr[mid] == key):
                return mid
            elif (x.arr[mid] > key):
                return Searching.binarySearchRecursive(x,key, low, mid - 1)
            else:
                return Searching.binarySearchRecursive(x,key, mid + 1, high)
        return -1



if __name__=="__main__":
    a=Array(8,6,3,2,-8,5)
    print(f"linearSearch {Searching.linearSearch(a,45)}")
    print(f"TranspositionLinearSearch {Searching.TranspositionLinearSearch(a,45)}")
    print(f"moveToHeadLinearSearch {Searching.moveToHeadLinearSearch(a,45)}")
    b=Array(1,2,3,4,5,6,7,8,9,10,11,12,13)
    print(f"binarySearch {Searching.binarySearch(b,9,0,len(b))}")
    print(f"binarySearchRecursive {Searching.binarySearchRecursive(b,8,0,len(b))}")

