# Heap Sort Algorithm
# https://www.programiz.com/dsa/heap-sort


def heapify(array, length_of_array, i):
    highest_value = i   # find highest_value among root and children
    left = 2 * i + 1
    right = 2 * i + 2
    if left < length_of_array and array[i] < array[left]:
        highest_value = left
    if right < length_of_array and array[highest_value] < array[right]:
        highest_value = right
    if highest_value != i: # if root is not equal to highest_value
        array[i], array[highest_value] = array[highest_value], array[i] # then swap them
        heapify(array, length_of_array, highest_value) # call function heapify again


def heapSort(array):
    length_of_array = len(array)
    for i in range(length_of_array // 2, -1, -1): # build max heap
        heapify(array, length_of_array, i) # call function heapify
    for i in range(length_of_array - 1, 0, -1):
        array[i], array[0] = array[0], array[i] # swap values
        heapify(array, i, 0) # heapify root element
        print(array)

array = [1, 12, 9, 5, 6, 10]

print(f"Unsorted array is: {array}.")
heapSort(array)
print(f"Sorted array is: {array}.")