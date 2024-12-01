def QuickSort(array, leftIdx, rightIdx):
    if rightIdx > leftIdx:
        pivotIdx = (leftIdx + rightIdx)//2
        newPivotIdx = doPartitioning(array, leftIdx, rightIdx, pivotIdx)
        QuickSort(array, leftIdx, newPivotIdx-1)
        QuickSort(array, newPivotIdx+1, rightIdx)
    return array

def doPartitioning(array, leftIdx, rightIdx, pivIdx):
    pivotVal = array[pivIdx]
    array[pivIdx] = array[rightIdx]
    array[rightIdx] = pivotVal

    currIdx = leftIdx

    for ii in range(leftIdx, rightIdx):
        if array[ii].getBatteryLevel() > pivotVal.getBatteryLevel():
        # if array[ii] > pivotVal:
            temp = array[ii]
            array[ii] = array[currIdx]
            array[currIdx] = temp
            currIdx = currIdx + 1
            
    newPivIdx = currIdx
    array[rightIdx] = array[newPivIdx]
    array[newPivIdx] = pivotVal
    return newPivIdx

# array = [300,200,500,60,50,100,70]
# print(QuickSort(array, 0,len(array)-1))