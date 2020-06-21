# Quick Sort Algorithm
# https://www.programiz.com/dsa/quick-sort
# Set first item in an array as sorted

comparisons = 0
iteration = 0
swaps = 0

def QuickSort(array, start, end):
    global iteration
    global swaps
    global comparisons
    if start <= end:
        pIndex = Partition(array, start, end)
        QuickSort(array, start, pIndex - 1)
        QuickSort(array, pIndex + 1, end)
    return f"Sorted array: {array}, comparisons: {comparisons}, swaps {swaps}"


def Partition(array, start, end):
    global comparisons
    global iteration
    global swaps
    pivot = array[end]
    pIndex = start
    for i in range(start, end - 1):
        comparisons += 1
        if array[i] <= pivot:
            array[i], array[pIndex] = array[pIndex], array[i]
            swaps += 1
            pIndex += 1
    array[pIndex], array[end] = array[end], array[pIndex]
    swaps += 1
    comparisons += 1
    iteration += 1
    print(f"Iteration {iteration}: {array}")
    return pIndex


array = [2, 7, 4, 1, 5, 3]
print(f"Unsorted array: {array}")
print(QuickSort(array, 0, len(array)-1))