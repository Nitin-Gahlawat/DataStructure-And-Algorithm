# ## Oprations on a array.
from __future__ import annotations
from .ArrayClass import Array

class ArrayOprtations:
    @staticmethod
    def Max(x:Array)->int:
        max = x.arr[0]
        for i in range(0,len(x)):
            if (max < x.arr[i]):
                max = x.arr[i]
        return max

    @staticmethod
    def Min(x:Array)->int:
        min = x.arr[0]
        for i in range(0,len(x)):
            if (min > x.arr[i]):
                min = x.arr[i]
        return min

    @staticmethod
    def Sum(x:Array)->int:
        sum = 0
        for i in range(0,len(x)):
            sum = sum + x.arr[i]
        return sum

    @staticmethod
    def Avg(x:Array)->float:
        avg = 0
        for i in range(0,len(x)):
            avg = avg + x.arr[i]
        return avg / len(x)
    
    @staticmethod
    def reverse_Array_meth1(y:Array) -> Array:
        x=y.copy()
        for i in range(0,int(len(x)/2)):
            x.arr[i],x.arr[len(x)-i-1]=x.arr[len(x)-i-1],x.arr[i]
        return x

    @staticmethod
    def reverse_Array_meth2(x:Array) ->Array:   
        temp_arr=x.copy()
        for i in range(0,len(x)):
            temp_arr[i]=x.arr[len(x)-i-1]
        return temp_arr

    @staticmethod
    def shift(y:Array,left : bool) -> Array:
        x=y.copy()
        if left:
            for i in range(1,len(x)):
                x.arr[i-1]=x.arr[i]
            x.arr[len(x)-1]=0
        else:
            for i in range(len(x)-1,0,-1):
                x.arr[i]=x.arr[i-1]
            x.arr[0]=0

        return x     

    @staticmethod
    def rotate(y:Array,left: bool) -> Array:
        x=y.copy()
        if left:
            temp=x.arr[0]
            for i in range(1,len(x)):
                x.arr[i-1]=x.arr[i]
            x.arr[len(x)-1]=temp
        else:
            temp=x.arr[len(x)-1]
            for i in range(len(x)-1,0,-1):
                x.arr[i]=x.arr[i-1]
            x.arr[0]=temp
        return x
    
if __name__=="__main__":
    a=Array(-8,5,6,2,5,45,3,20)
    print(f"Max {ArrayOprtations.Max(a)}")
    print(f"Min {ArrayOprtations.Min(a)}")
    print(f"Sum {ArrayOprtations.Sum(a)}")
    print(f"Avg {ArrayOprtations.Avg(a)}")
    print(ArrayOprtations.reverse_Array_meth1(a))
    print(ArrayOprtations.reverse_Array_meth2(a))
    print(ArrayOprtations.shift(a,False))
    print(ArrayOprtations.rotate(a,True))  

