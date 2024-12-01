import numpy as np
class DSAStack:
    default_capacity = 100
    def __init__(self, maxCapacity = default_capacity):
        self.count = 0
        self.stack = np.empty(maxCapacity, dtype = object)
        self.maxCapacity = maxCapacity
               
    def getCount(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):       
        return self.count == len(self.stack)
    
    def push(self,value):
        if self.isFull():
            print("Stack is already full!")
        else:
            self.stack[self.count] = value
            self.count += 1
            # print("The stack has",self.count,"disks")

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            topVal = self.top()
            self.count = self.count - 1
            self.stack[self.count] = None
            return topVal
        
    def top(self):
        if self.isEmpty():
            print("The stack is currently empty!")
        else:
            topVal = self.stack[self.count - 1]
            # print("The top disk value is the",topVal,"th disk")
            return topVal

        
# a = DSAStack()
# a.push(5)
# a.push(6)
# a.push(7)
# a.push(8)
# print(a.pop())
# print(a.top())
# print(a)






    


            
    

        
    
        

        
    
