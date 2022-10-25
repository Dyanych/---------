from functools import reduce
import random
import time

# All type of sorting algorithms

def selectSort(arr: list) -> list:
    # 1. Selection sort
    for i in range(len(arr) - 1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
            arr[i], arr[min] = arr[min], arr[i]
    return arr

def incertSort(arr: list) -> list:
    # 2. Insertion sort
    if len(arr) > 1: 
        for i in range(1, len(arr)):
            for j in range(i):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
    return arr

def bubbleSort(arr: list) -> list:
    # 3. Bubble sort
    for i in range(len(arr) - 1):
        flag = True
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
                flag = False
        if flag:
            break
    return arr

def mergeSort(arr: list) -> list:
    # 4. Merge sort
    n = len(arr)
    # Split recusively
    if n <= 1:
        return arr
    else:
        arr1 = mergeSort(arr[:n//2])
        arr2 = mergeSort(arr[n//2:])

        arr.clear()
    
    # Merge the chunks
        while arr1 and arr2:
            if arr1[0] <= arr2[0]:
                arr.append(arr1[0])
                arr1.pop(0)
            else:
                arr.append(arr2[0])
                arr2.pop(0)
        arr.extend(arr1 + arr2)
    return arr

def heapSort(arr: list) -> list:
    # 5. Heap sort
    pass

def msdSort(arr: list) -> list:
    # 6. MSD sort
    pass

def lsdSort(arr: list) -> list:
    # 7. LSD Sort
    i = 0
    runNext = True

    while runNext:
        digiDict = {i:[] for i in (0,1,2,3,4,5,6,7,8,9)}
        runNext = False
        for x in arr:
            digi = x%(10**(i+1))//(10**i)
            runNext |= digi
            digiDict[digi].append(x)
        arr.clear()
        # print('*****', arr)
        arr = reduce(lambda x, y: x + y, [digiDict[i] for i in (0,1,2,3,4,5,6,7,8,9)])
        # print(i, '-->', arr)
        i += 1
    return arr

# Generate not sorted list
# m = random.randint(1, 1000)
m = 10000
inList = random.sample(range(m+1),m)
# inList = [2,1]
print(inList)

start = time.time()
lsdSort(inList)
print(inList)
end = time.time()
print(end - start)

# print(myIncert([7,8,9], 5))