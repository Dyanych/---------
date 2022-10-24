import random
import time

# All type of sorting algorithms

def myIncert(arrSorted: list, new) -> list:
    try:
        j = 0
        while arrSorted[j] < new:
            j += 1
        return arrSorted[:j] + [new] + arrSorted[j:]
    except:
        return arrSorted + [new]

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

# 4. Merge sort
# 5. Heap sort

# Generate not sorted list
# m = random.randint(1, 1000)
m = 10
inList = random.sample(range(m+1),m)
# inList = [4,3,2,1]
print(inList)

start = time.time()
bubbleSort(inList)
print(inList)
end = time.time()
print(end - start)

# print(myIncert([7,8,9], 5))