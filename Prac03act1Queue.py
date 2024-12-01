import numpy as np
class DSAQueue():
    default_capacity = 100
    def __init__(self, maxCapacity = default_capacity):
        self.count = 0
        self.queue = np.empty(maxCapacity, dtype = object)
        self.maxCapacity = maxCapacity

    def getCount(self):
        return self.count
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == len(self.queue)
    
    def enqueue(self, value):
        if self.isFull():
            print("The queue is full!")
        else:
            self.queue[self.count] = value
            self.count += 1
            # print(self.queue)
    
    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty!")
        else:
            # print(self.queue)
            frontVal = self.queue[0]
            for i in range(len(self.queue)-1):
                self.queue[i] = self.queue[i+1]
                self.queue[i+1] = None 
            self.count -= 1
            return frontVal
        
    def peek(self):
        if self.isEmpty():
            print("The queue is empty!")
        else:
            frontVal = self.queue[0]
            # print("The current front Value is", frontVal)
            return frontVal
        
    
        
# a = DSAQueue()
# a.enqueue(9)
# a.enqueue(10)
# a.enqueue(7)
# print(a.dequeue())
# print(a.dequeue())
# print(a.dequeue())
# print(a.dequeue())
# print(a.queue)


    
