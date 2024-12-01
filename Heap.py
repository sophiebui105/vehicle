import numpy as np
class DSAHeapEntry():
    def __init__(self, priority, value):
        self.priority = priority
        self.value = value
    def getPriority(self):
        return self.priority
    def setPriority(self, priority):
        self.priority = priority
    def getValue(self):
        return self.value
    def setValue(self, value):
        self.value = value

class DSAHeap():
    def __init__(self, maxSize):  
        self.heapArr = np.empty(maxSize, dtype= object)
        self.count = 0
    def add(self, priority, value):
        if self.count > len(self.heapArr):
            raise Exception("Heap is full!")
        else:
            newVal = DSAHeapEntry(priority, value)
            self.heapArr[self.count] = newVal
            self.trickleUp(self.count)
            self.count += 1
    def trickleUp(self, curIdx):
        parentIdx = (curIdx-1)//2
        while curIdx > 0 and self.heapArr[curIdx].getPriority() > self.heapArr[parentIdx].getPriority():
            temp = self.heapArr[parentIdx]
            self.heapArr[parentIdx] = self.heapArr[curIdx]
            self.heapArr[curIdx] = temp
            curIdx = parentIdx
            parentIdx = (curIdx-1)//2
        return self.heapArr
    def remove(self):
        if self.count == 0:
            raise Exception("Heap is empty!")
        else:
            self.heapArr[0] = self.heapArr[self.count-1]
            self.heapArr[self.count-1] = None
            self.trickleDown(0, self.count, self.heapArr)
            self.count -= 1
        return self.heapArr
    def trickleDown(self, curIdx, numItems, heapArr):
        if heapArr is None:
            heapArr = self.heapArr
        lChildIdx = curIdx*2 + 1
        rChildIdx = lChildIdx + 1
        keepGoing = True
        while keepGoing and lChildIdx < numItems:
            keepGoing = False
            self.largeIdx = lChildIdx
            if rChildIdx < numItems:
                if heapArr[lChildIdx].getPriority() < heapArr[rChildIdx].getPriority():
                    self.largeIdx = rChildIdx
            if heapArr[self.largeIdx] is not None and heapArr[curIdx] is not None and heapArr[self.largeIdx].getPriority() > heapArr[curIdx].getPriority(): 
                temp = heapArr[self.largeIdx]
                heapArr[self.largeIdx] = heapArr[curIdx]
                heapArr[curIdx] = temp
                keepGoing = True
            curIdx = self.largeIdx
            lChildIdx = curIdx * 2 + 1
            rChildIdx = lChildIdx + 1
    def heapify(self, heapArr, numItems):
        a = (numItems//2)-1
        for ii in range(a, -1, -1):
            self.trickleDown(ii, numItems, heapArr)
        return heapArr
    def heapSort(self, numItems):
        self.heapify(self.heapArr, numItems)
        b = numItems - 1
        for ii in range(b, 0, -1):
            temp = self.heapArr[0]
            self.heapArr[0] = self.heapArr[ii]
            self.heapArr[ii] = temp
            self.trickleDown(0, ii, self.heapArr)

# file_path = "D:\Curtin Master\Sem 2 2024\DSA\Week 9 - Hash tables\Prac07 - 21875768\RandomNames7000.csv"
# data = []
# value = []
# with open (file_path, 'r') as file:
#     for line in file:
#         data.append(int(line.split(",")[0]))
#         value.append(line.split(",")[1])
    
# numItems = len(data)
# heapEntry = np.empty(numItems, dtype = object)
# for i in range(numItems):
#     heapEntry[i] = DSAHeapEntry(data[i], value[i])

# heap = DSAHeap(numItems)
# for i in range(numItems):
#     heap.add(data[i], value[i])
# heap.remove()
# heap.heapSort(numItems)

# print("Sorted values after applying heapSort:")
# for entry in heap.heapArr:
#     if entry is not None:
#         print(f"Priority: {entry.getPriority()}, Value: {entry.getValue()}")

# import csv


# output_file_path = "D:/Curtin Master/Sem 2 2024/DSA/Week 10 - Heaps/Prac08 - 21875768/SortedRandomNames7000.csv"


# with open(output_file_path, mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["Priority", "Value"])
    
#     for entry in heap.heapArr:
#         if entry is not None:
#             writer.writerow([entry.getPriority(), entry.getValue()])

# print(f"Sorted heap data saved to {output_file_path}")


# heap = DSAHeap(5)

# heap.add(10, "A") 
# heap.add(15, "B")  
# heap.add(5, "C")   
# heap.add(20, "D")  

# for i in range(heap.count):
#     print(f"Index {i}: Priority = {heap.heapArr[i].getPriority()}, Value = {heap.heapArr[i].getValue()}")

# heap.remove()
# for i in range(heap.count):
#     print(f"Index {i}: Priority = {heap.heapArr[i].getPriority()}, Value = {heap.heapArr[i].getValue()}")

# heapArr = np.empty(9, dtype=object)
# heapArr[0] = DSAHeapEntry(5, "E")
# heapArr[1] = DSAHeapEntry(4, "A")
# heapArr[2] = DSAHeapEntry(1, "F")
# heapArr[3] = DSAHeapEntry(11, "G")
# heapArr[4] = DSAHeapEntry(10, "H")
# heapArr[5] = DSAHeapEntry(3, "I")
# heapArr[6] = DSAHeapEntry(2, "B")
# heapArr[7] = DSAHeapEntry(16, "B")
# heapArr[8] = DSAHeapEntry(12, "B")
# numItems = 9 

# heap = DSAHeap(numItems)

# heap.heapify(heapArr, numItems)

# print("Heap after heapify:")
# for i in range(numItems):
#     print(f"Index {i}: Priority = {heapArr[i].getPriority()}, Value = {heapArr[i].getValue()}")

# heap.heapSort(heapArr, len(heapArr))

# print("\nArray after heapSort:")
# for i in range(numItems):
#     print(f"Priority: {heapArr[i].getPriority()}, Value: {heapArr[i].getValue()}")






