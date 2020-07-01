# Shell Sort Algorithm
# https://www.programiz.com/dsa/shell-sort


def shellSort(array):
    print(f"Unsorted array: {array}.")
    len_of_array = len(array)
    gap = int(len_of_array/2) # Start with a big gap, then reduce the gap
    while gap > 0: # loop over until gap is grater than 0
        for i in range(gap, len_of_array):
            temp_value = array[i] # save a[i] in temp_value and make a hole at position i
            temp_index = i # save i in temp_index
            while temp_index >= gap and array[temp_index - gap] > temp_value: # shift earlier gap-sorted elements up until the correct
                array[temp_index] = array[temp_index - gap]
                temp_index -= gap
            array[temp_index] = temp_value  # put temp_value (the original a[i]) in its correct location
            # print(array)
        gap = int(gap/2) # smaller the gap
    print(f"Sorted array: {array}.")

array = [1, 12, 9, 5, 6, 10, 7, 3]
shellSort(array)
