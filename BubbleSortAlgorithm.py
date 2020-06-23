# Bubble Sort Algorithm
# https://www.programiz.com/dsa/bubble-sort
# Compare 2 items next to each other from left to right hand side and sort them if it is needed. Firstly highest numbers are sorted from right to left hand side.

# https://www.studytonight.com/data-structures/bubble-sort
# Worst Case Time Complexity [Big-O]: O(n**2)
# Best Case Time Complexity [Big-omega]: O(n)
# Average Time Complexity [Big-theta]: O(n**2)

# worst case - n^2 comparisons, n^2 swaps average case - best case - n^2 comparision, n swaps

print("Bubble Sort Algorithm:")
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