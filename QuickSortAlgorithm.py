# Quick Sort Algorithm
# https://www.programiz.com/dsa/quick-sort
# 1. A pivot element is chosen from the array. You can choose any element from the array as the pivot element. Here, we have taken the rightmost (ie. the last element) of the array as the pivot element
# 2. The elements smaller than the pivot element are put on the left and the elements greater than the pivot element are put on the right.
# The above arrangement is achieved by the following steps.
# a) A pointer is fixed at the pivot element. The pivot element is compared with the elements beginning from the first index. If the element greater than the pivot element is reached, a second pointer is set for that element.
# b) Now, the pivot element is compared with the other elements (a third pointer). If an element smaller than the pivot element is reached, the smaller element is swapped with the greater element found earlier.
# c) The process goes on until the second last element is reached. Finally, the pivot element is swapped with the second pointer.
# 3. Pivot elements are again chosen for the left and the right sub-parts separately. Within these sub-parts, the pivot elements are placed at their right position. Then, step 2 is repeated.
# 4. The sub-parts are again divided into smaller sub-parts until each subpart is formed of a single element.
# 5. At this point, the array is already sorted.


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
    for i in range(start, end):
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