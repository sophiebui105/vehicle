import numpy as np
class DSAHashEntry():
    def __init__(self, inKey = " ", inValue = None):
        self.key = inKey
        self.value = inValue
        self.state = 0 if inKey == " " else 1

    def __repr__(self):
        return f"DSAHashEntry(key={self.key}, value={self.value}, state={self.state})"

import math
def findNextPrime(startVal: int):
    if startVal % 2 == 0:
        primeVal = startVal - 1 
    else:
        primeVal = startVal 
    isPrime = False
    while not isPrime:
        primeVal = primeVal + 2
        isPrime = True
        rootVal = math.sqrt(primeVal)
        ii = 3 
        while ii <= rootVal and isPrime:
            if primeVal % ii == 0:
                isPrime = False
            else:
                ii = ii + 2
    return primeVal


class DSAHashTable():
    def __init__(self, tableSize):
        self.actualSize = findNextPrime(tableSize)
        self.tableSize = tableSize
        self.hashArray = np.empty(self.actualSize, dtype = object)
        for i in range(self.actualSize):
            self.hashArray[i] = DSAHashEntry()
        self.count = 0
    
    def getSize(self):
        return self.actualSize
        
    def put(self, inKey, inValue):
        if self.getLoadFactor() > 0.7:
            self._resize(self.actualSize*2)

        # hashIdx = self._findEmpty(inKey)
        # self.hashArray[hashIdx] = DSAHashEntry(inKey, inValue)
        # self.count += 1

        hashIdx = self._hash(inKey)
        origIdx = hashIdx
        found = False
        give_up = False

        while not give_up:
            if self.hashArray[hashIdx].state == 0 or self.hashArray[hashIdx].state == -1:
                self.hashArray[hashIdx].value = inValue
                self.hashArray[hashIdx].state = 1
                self.hashArray[hashIdx].key = inKey
                self.count += 1
                give_up = True
            elif self.hashArray[hashIdx].state == 1 and self.hashArray[hashIdx].key == inKey:
                raise DuplicateError("Duplicate key error!")
            else:
                hashIdx = (hashIdx + self._stepHash(inKey)) % len(self.hashArray)
                if hashIdx == origIdx:
                    give_up = True

    def get(self, inKey):
        hashIdx = self._findKey(inKey)
        if hashIdx is not None and self.hashArray[hashIdx].state == 1:
            return self.hashArray[hashIdx].value
        else:
            raise KeyError(f"Cannot find {inKey}")
        
    def remove(self, inKey):
        hashIdx = self._findKey(inKey)
        if hashIdx is not None and self.hashArray[hashIdx].state == 1:
            self.hashArray[hashIdx].state = -1
            self.count -= 1
            self.hashArray[hashIdx].key = None
            self.hashArray[hashIdx].value = None 
        else:
            raise KeyError(f'Cannot find {inKey}')
        if self.getLoadFactor() < 0.3:
            self._resize(self.actualSize // 2)
    
    def getLoadFactor(self):
        return (self.count + 1)/self.actualSize
    
    import numpy as np

    def _resize(self, newSize):
        oldArray = self.hashArray
        self.actualSize = findNextPrime(newSize)
        self.hashArray = np.empty(self.actualSize, dtype = object)
        for i in range(self.actualSize):
            self.hashArray[i] = DSAHashEntry()
       
        oldCount = self.count
        self.count = 0

        for entry in oldArray:
            if entry.state == 1:
                self.put(entry.key, entry.value)
        self.count = oldCount
    
    def _hash(self, key):
        hashIdx = 0
        for ii in range(len(key)):
            hashIdx = hashIdx^((hashIdx << 5) + (hashIdx << 2) + ord(key[ii]))
        return hashIdx % len(self.hashArray)
    
    def _stepHash(self, inKey):
        # return 1 + (hash(inKey) % (self.actualSize -1))
        key = 0
        for i in range(len(inKey)):
            key += ord(inKey[i])                
        return 5 - (key % 5)
    
    def _findKey(self, inKey):
        hashIdx = self._hash(inKey)
        step = self._stepHash(inKey)
        origIdx = hashIdx

        while self.hashArray[hashIdx].state != 0:
            if self.hashArray[hashIdx].key == inKey and self.hashArray[hashIdx].state == 1:
                return hashIdx
            hashIdx = (hashIdx + step) % self.actualSize
            if hashIdx == origIdx:
                return None
        return None
    
    def _findEmpty(self, inKey):
        hashIdx = self._hash(inKey)
        step = self._stepHash(inKey)
        origIdx = hashIdx

        while self.hashArray[hashIdx].state == 1:
            hashIdx = (hashIdx + step) % self.actualSize
            if hashIdx == origIdx:
                raise Exception("HashTable is full")
        return hashIdx
    
    def export(self):
        return[a for a in self.hashArray if a.state == 1]
    
    def printTable(self):
        for i, entry in enumerate(self.hashArray):
            if entry is not None:
                # print(f"Index {i}: Key = {entry.key}, Value = {entry.value}")
                print(f"Index {i}: VehicleID = {entry.key}, Vehicle = {entry.value}")
class DuplicateError(Exception):
    pass

# import csv
# def loadcsv(filename):
#     with open('RandomNames7000.csv', newline='') as csvfile:
#         spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#         for row in spamreader:
#             print(', '.join(row))

import csv

def loadNamesFromCSV(filename):  
    hashTable = DSAHashTable(10)
    # with open(filename, mode='r', newline='', encoding='utf-8') as file:
        # reader = csv.reader(file)
    reader = open(filename, 'r')
    readlines = reader.readlines()
    for row in readlines:
        if row:  
            a = row.split(",")
            inKey = a[0].strip()
            inValue = a[1].strip()
            try:
                hashTable.put(inKey, inValue)
            except DuplicateError:
                print("Duplicate Error")
    return hashTable

def saveHashTableToCSV(hashTable, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for entry in hashTable.export():
            writer.writerow([entry.key, entry.value])  


# a = DSAHashTable(10)
# table = loadNamesFromCSV('RandomNames7000.csv')
# saveHashTableToCSV(table, 'HashTable.csv')

  # Load names from CSV
# saveHashTableToCSV(hashTable, 'HashTable.csv')

# saveHashTableToCSV(hashTable, 'HashTableOutput.csv')  # Save the hash table to CSV


# hashTable = DSAHashTable(5)
# hashTable.put('1', 100)
# hashTable.put('2', 200)
# hashTable.put('3', 200)
# hashTable.put('Phuong',500)
# hashTable.printTable()
# # print()
# # hashTable.put('4', 200)
# # hashTable.remove('4')
# hashTable.remove('2')
# hashTable.printTable()
# print(hashTable.getSize())






        