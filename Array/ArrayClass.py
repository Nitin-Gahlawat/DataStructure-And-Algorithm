from __future__ import annotations
import ctypes
from random import randint

class Array:
    def __init__(self:Array,*args:tuple[int])->None: 
        if(len(args)==0):     
            self._size=1
            self._length=0
            #create c type array with _size=self._size
            self.arr=self.__make_array(self._size)
            for i in range(0,self._size):
                self.arr[i]=None
        else:
            self._size=len(args)
            self._length=len(args)
            self.arr=self.__make_array(self._size)
            for i in range(0,self._size):
                self.arr[i]=args[i]

        
    def __make_array(self:Array,capacity):
        #create self.arr static and referential(store all types) with _size capacity
        x=(capacity*ctypes.py_object)()
        return x
        
    def __grow(self:Array)->None:
        self._size=self._size*2
        new_arr=self.__make_array(self._size)
        for i in range(0,self._size):
            if(self._length>i):
                new_arr[i]=self.arr[i]
            else:
                new_arr[i]=None
        self.arr=new_arr

    def copy(self:Array)->Array:
        x=Array()
        for i in range(len(self.arr)):
            x.append(self.arr[i])
        return x
            
    def __getitem__(self:Array, index:int)->int:
        return self.arr[index]

    def __setitem__(self:Array, index:int, value:int)->None:
        self.arr[index] = value
        
    def __str__(self:Array)->str:
        res="["
        for i in range(0,self._length):
            res+=(f"{self.arr[i]} , ")
        res=res[0:len(res)-2]+("]") #removing the last comma from the string
        return res
        
    def __len__(self:Array)->int:
        return self._length
    
    def GetIndex(self:Array,index)->int:
        return self.arr[index]
    
    
    def SetIndex(self:Array,index,element)->None:
        self.arr[index]=element


    def isDuplicate(self:Array)->bool:
        for i in range(0,self._length):
            for j in range(0,self._length):
                if (i != j):
                    if (self.arr[i]==self.arr[j]):
                        return True
        return False

    
    def is_sorted(self:Array) -> bool:
         for i in range(0,self._length-1):
             if self.arr[i]>self.arr[i+1]:
                 return False
         return True
    
    # /**
    #  * Inserts an element in the array.
    #  *
    #  */
    def insert(self:Array,*args:tuple[int])->None:
        for num in args:
            if(self._size==self._length):
                self.__grow()
            self.arr[self._length]=num
            self._length=self._length+1
            
    def append(self:Array,value:int)->None:
        if(self._size==self._length):
            self.__grow()
        self.arr[self._length]=value
        self._length=self._length+1
        
    def insertLast(self:Array,value:int)->None:
        self.append(value)
        
    def insertFirst(self:Array,value:int)->None:
        if(self._size==self._length):
            self.__grow()
        for i in range(self._length,-1,-1):
            self.arr[i]=self.arr[i-1]
        self.arr[0]=value
        self._length=self._length+1
        
    def insert_Positon(self:Array,pos:int,value:int)->None:
        if(self._size==self._length):
            self.__grow()
        for i in range(self._length,pos,-1):
            self.arr[i]=self.arr[i-1]
        self.arr[pos]=value
        self._length=self._length+1
        

    def insert_in_sorted_array(self:Array,element):
        if (self.is_sorted()):
            raise Exception("The array is not sorted ")
        
        if(self._size==self._length):
            self.__grow()
        for i in range(self._length,-1,-1):
            if self.arr[i-1] > element :
                self.arr[i]=self.arr[i-1]
            else:
                break
        self.arr[i]=element
        self._length=self._length+1 
        
    # /**
    #  * Deletes an element in the array.
    #  *
    #  */
    def deleteLast(self:Array)->int:       
         if (self._length == 0):
            raise Exception("The Array has no element")
         element = self.arr[self._length - 1]
         self.arr[self._length - 1]= None
         self._length=self._length-1
         return element
        
    def deleteFirst(self:Array)->int:
        if (self._length == 0):
            raise Exception("The Array has no element")
        element = self.arr[0]
        for i in range(1,self._length):
            self.arr[i-1]=self.arr[i]
        self.arr[self._length - 1]= None
        self._length=self._length-1
        return element
        
    def deletePosition(self:Array,position)->int:
        if (self._length == 0):
            raise Exception("The Array has no element")
        element = self.arr[position]
        for i in range(position,self._length):
            self.arr[i]= self.arr[i + 1]
        self.arr[self._length - 1]= None
        self._length=self._length-1
        return element
        
    def deleteElement(self:Array,element)->int:
        if (self._length == 0):
            raise Exception("The Array has no element")
            return 
        for i in range(0,self._length):
            if (self.arr[i]==element):
                return self.deletePosition(i)
    
    def negtive_on_left_side(self:Array)-> Array:
        x=self.copy()
        i,j=0,x._length-1
        while(i<j):
            if(x.arr[i]>0 and x.arr[j]<0):
                x.arr[i],x.arr[j]=x.arr[j],x.arr[i]
                i,j=i+1,j-1
            else:
                if(x.arr[i]<0):
                    i=i+1
                elif(x.arr[j]>0):
                    j=j-1
        return x
    


    def  Mearging_sorted(self:Array,a:Array)->Array:
        new_arr=[]
        i,j=0,0
        while(i < self._length and j<a._length):
            if(self.arr[i]<a[j]):
                new_arr.append(self.arr[i])
                i=i+1
            else:
                new_arr.append(a.arr[j])
                j=j+1
            
        while(i < self._length):
            new_arr.append(self.arr[i])
            i=i+1
        while(j<a._length):
            new_arr.append(a.arr[j])
            j=j+1

        return Array(*tuple(new_arr))
    

    def concat(self:Array,a:Array)->None:
        for i in range(len(a)):
            self.append(a[i])
