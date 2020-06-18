# Bubble Sort Algorithm
# https://www.programiz.com/dsa/bubble-sort
# Compare 2 items next to each other from left to right hand side and sort them if it is needed. Firstly highest numbers are sorted from right to left hand side.

def BubbleSort(array):
    print(f"Unsorted array: {array}")
    comparisons = 0
    swaps = 0
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            comparisons += 1
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swaps += 1
        print(f"Iteration {i+1}: {array}")
    print(f"Sorted array: {array}, comparisons: {comparisons}, swaps: {swaps}.")

array = [2,7,4,1,5,3]

BubbleSort(array)