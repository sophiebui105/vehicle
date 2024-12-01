class DSAListNode:
    def __init__(self, inValue):
        self.value = inValue
        self.next = None
    def getValue(self):
        return self.value 
    def setValue(self,inValue):
        self.value = inValue
    def getNext(self):
        return self.next
    def setNext(self,newNext):
        self.next = newNext
    def getPrev(self):
        return self.prev
    def setPrev(self, newPrev):
        self.prev = newPrev
    
class DSADEDLList:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head == None 
    def insertFirst(self, newValue):      
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd 
        else:
            newNd.setNext(self.head)
            self.head.setPrev(newNd)
            self.head = newNd
    def insertLast(self, newValue):
        newNd = DSAListNode(newValue)
        if self.isEmpty():
            self.head = newNd
            self.tail = newNd
        else:
            currNd = self.tail
            currNd.setNext(newNd)
            newNd.setPrev(self.tail)
            self.tail = newNd
    def peekFirst(self):
        if self.isEmpty():
            raise Emptyexception("It is empty!")
        else:
            nodeValue = self.head.getValue()
        
        return nodeValue
    def peekLast(self):
        if self.isEmpty():
            raise Emptyexception("It is empty!")
        else:
            nodeValue = self.tail.getValue()
        return nodeValue
    def removeFirst(self):
        if self.isEmpty():
            raise Emptyexception("It is empty!")
        else:
            nodeValue = self.head.getValue()
            self.head = self.head.getNext()
            if self.head == None:
                self.tail = None
        return nodeValue
    def removeLast(self):
        if self.isEmpty():
            raise Emptyexception("It is empty!")
        elif self.head.getNext() == None:
            nodeValue = self.head.getValue()
            self.head = None
            self.tail = None
        else:
            prevNd = self.tail.getPrev()
            prevNd.setNext(None)
            self.tail = prevNd   
            nodeValue = self.tail.getValue()
        return nodeValue
    
    def printList(self):
        currNd = self.head
        while currNd is not None:
            print(currNd.getValue(), end=" ")
            currNd = currNd.getNext()
        print()

    def printPathList(self):
        currNd = self.head
        while currNd is not None:
            print(currNd.getValue().getValue(), end=" ")
            currNd = currNd.getNext()
        print()
    
    def printVertexList(self):
        currNd = self.head
        while currNd is not None:
            print(currNd.getValue().getLabel(), end=" ")
            currNd = currNd.getNext()
        print()

    def copy(self):
        new_list = DSADEDLList()
        current = self.head
        while current:
            new_list.insertLast(current)
            current = current.next
        return new_list
    
    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode.getValue()
            curNode = curNode.getNext()

class Emptyexception(Exception):
    pass

# a = DSADEDLList()
# a.insertFirst(5)
# a.printList()
# a.insertFirst(6)
# try:
#     a.removeLast()
# except Exception as err:
#     print("It is empty!")

# try:
#     a.removeLast()
# except Exception as err:
#     print("It is empty!")

# a.printList()




        
    
     


    
