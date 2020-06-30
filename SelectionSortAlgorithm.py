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
    for i in range(len(array)): # loop over all item in list
        min_value = array[i] # define min_value
        min_position = i # define min_position
        for j in range(i, len(array)):  # loop over all item in list starting from i
            comparisons += 1 # increase comparisons
            if array[j] < min_value: # if current_value - array[j] is smaller than min_value
                min_value = array[j] # then min_value equals to current_value - array[j]
                min_position = j # min_position equals to current_value index
        if array[i] != array[min_position]: # if first item is not equal to min_value
            array[i], array[min_position] = array[min_position], array[i] # then swap these two values, the lowest value is now fixed
            swaps += 1 # increase swaps
        print(f"Iteration {i + 1}: {array}")
    print(f"Sorted array: {array}, comparisons: {comparisons}, swaps: {swaps}.")

array = [2,7,4,1,5,3]

SelectionSort(array)
