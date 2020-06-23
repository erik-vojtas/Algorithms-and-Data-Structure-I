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
    for i in range(1, len(array)):
        key = array[i]
        position = i - 1
        while position >= 0 and key < array[position]:
            comparisons += 1
            array[position+1] = array[position]
            position -= 1
        array[position+1] = key
        swaps += 1
        print(f"Iteration {i}: {array}")
    print(f"Sorted array: {array}, comparisons: {comparisons}, swaps: {swaps}.")

array = [2,7,4,1,5,3]

InsertionSort(array)