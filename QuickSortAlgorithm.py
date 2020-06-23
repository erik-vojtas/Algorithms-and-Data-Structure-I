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
#
# https://www.studytonight.com/data-structures/quick-sort
# Worst Case Time Complexity [Big-O]: O(n**2)
# Best Case Time Complexity [Big-omega]: O(n*log n)
# Average Time Complexity [Big-theta]: O(n*log n)

# Video:
#https://www.youtube.com/watch?v=h_9kAXFKJwY&t=143s

import random

comparisons = 0
iteration = 0
swaps = 0
print("Quick Sort Algorithm:")
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

swap = 0
recursion_level = 0
def partitionRQS(array, left, right):
    global swap
    ## random select pivot
    pIndex = random.randint(left, right)
    tmp = array[right]
    array[right] = array[pIndex]
    array[pIndex] = tmp
    ##
    i = left
    j = right - 1
    pivot = array[right]
    # loop - do smthg as long as i not overlaps j
    while i < j:
        # loop searchuing element from left which ist greater or equal than pivot
        while i < right and array[i] < pivot:
            i = i + 1
        # loop searching from right element which is smaller than the pivot
        while j > left and array[j] >= pivot:
            j = j - 1

        # if i < j
        # swap array[i] array [j]
        if i < j:
            swap += 1
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp

    # if array[i] > pivot
    # swap array[i] array[right]
    if array[i] > pivot:
        swap += 1
        tmp = array[i]
        array[i] = array[right]
        array[right] = tmp
    return i


def r_quick_sort(array, left, right):
    global recursion_level
    if left >= right:
        return

    p = partitionRQS(array, left, right)
    # print(recursion_level)
    # print(left)
    # print(right)
    print(array)
    recursion_level += 1
    r_quick_sort(array, left, p - 1)
    recursion_level += 1
    r_quick_sort(array, p + 1, right)
    return




array = [2, 7, 4, 1, 5, 3]
print(f"Unsorted array: {array}")
print(QuickSort(array, 0, len(array)-1))
print("---------------------------------------------------------------")

array2 = [2, 7, 4, 1, 5, 3]
r_quick_sort(array2, 0, len(array)-1)
print("Swaps:", swaps, "Recursion level:", recursion_level)