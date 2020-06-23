# Selection Sort Algorithm
# https://www.programiz.com/dsa/selection-sort
# Compare 2 items next to each other from left to right hand side and look for a min_value. Then min_value is swaped with the first value from left hand side. Then second value and so on...until we get to the last value in array.

# https://www.studytonight.com/data-structures/selection-sorting
# Worst Case Time Complexity [ Big-O ]: O(n**2)
# Best Case Time Complexity [Big-omega]: O(n**2)
# Average Time Complexity [Big-theta]: O(n**2)

print("Selection Sort Algorithm:")
def SelectionSort(array):
    print(f"Unsorted array: {array}")
    comparisons = 0
    swaps = 0
    for i in range(len(array)):
        min_value = array[i]
        min_position = i
        for j in range(i, len(array)):
            comparisons += 1
            if array[j] < min_value:
                min_value = array[j]
                min_position = j
        if array[i] != array[min_position]:
            array[i], array[min_position] = array[min_position], array[i]
            swaps += 1
        print(f"Iteration {i + 1}: {array}")
    print(f"Sorted array: {array}, comparisons: {comparisons}, swaps: {swaps}.")

array = [2,7,4,1,5,3]

SelectionSort(array)
