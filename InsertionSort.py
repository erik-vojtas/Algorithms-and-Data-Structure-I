# Insertion Sort Algorithm
# https://www.programiz.com/dsa/insertion-sort
# The first element in the array is assumed to be sorted. Take the second element and store it separately in key.
# Compare key with the first element. If the first element is greater than key, then key is placed in front of the first element.
# Now, the first two elements are sorted. Take the third element and compare it with the elements on the left of it.
# Placed it just behind the element smaller than it. If there is no element smaller than it, then place it at the beginning of the array.

# https://www.studytonight.com/data-structures/insertion-sorting
# Worst Case Time Complexity [ Big-O ]: O(n**2)
# Best Case Time Complexity [Big-omega]: O(n)
# Average Time Complexity [Big-theta]: O(n**2)

print("Insertion Sort Algorithm:")
def InsertionSort(array):
    print(f"Unsorted array: {array}")
    comparisons = 0
    swaps = 0
    for i in range(1, len(array)): # iteration starts at 1, ends at the last element of array
        key = array[i] # key element equals to an element in array with the current index
        position = i - 1 # position equals to current index minus one
        while position >= 0 and key < array[position]: # as long as we haven't reached the beginning and there is an element in our sorted array larger than the one we're trying to insert - move that element to the right
            comparisons += 1 # increase comparisons
            array[position+1] = array[position]
            position -= 1 # decrease position
        array[position+1] = key
        swaps += 1 # increase swaps
        print(f"Iteration {i}: {array}")
    print(f"Sorted array: {array}, comparisons: {comparisons}, swaps: {swaps}.")

#array = [2,7,4,1,5,3]
array = [38,5,1,47,15,36,26,27,2,46,4,19,50,48,9]
InsertionSort(array)