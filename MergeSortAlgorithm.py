# Merge Sort Algorithm
# https://www.programiz.com/dsa/merge-sort
# split an array into two halves, sort these two halves and then merge them together in an order

comparisons = 0
iteration = 0
swaps = 0
def MergeSort(array, start, end):
    global iteration
    global swaps
    global comparisons
    if start < end:
        pIndex = Partition(array, start, end)
        MergeSort(array, start, pIndex - 1)
        MergeSort(array, pIndex + 1, end)
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


#array = [2, 7, 4, 1, 5, 3]
array = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print(f"Unsorted array: {array}")
print(MergeSort(array, 0, len(array)-1))