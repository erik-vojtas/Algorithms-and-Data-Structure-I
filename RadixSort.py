# Radix Sort Algorithm
# It is only used to sort numbers
# https://www.programiz.com/dsa/radix-sort

def radixSort(lis_of_nums):
    current_length = 1 # current current_length
    max_len = len(str(max(lis_of_nums))) # maximum current_length of number in list
    while current_length <= max_len: # loop over until current current_length is not greater than maximum current_length
        index = - + current_length # index = negative value of current current_length
        for x in range(len(list_of_nums)): # loop over all numbers in list
            str_num = str(list_of_nums[x])
            if len(str_num) < current_length: # if length of num is smaller than current_length
                list_of_nums[x] = str(0) + str_num # then add 0 in front of the first left digit
        for i in range(len(list_of_nums)): # compare each value (Bubble sort algorithm)
            for j in range(0, len(lis_of_nums)-i-1):
                if str(list_of_nums[j])[index] > str(list_of_nums[j+1])[index]: # if value on the left side is greate than value on the right side
                    list_of_nums[j], list_of_nums[j+1] = list_of_nums[j+1], list_of_nums[j] # then swap values
        print(f"Sorted list according to index: {index}: {[int(x) for x in list_of_nums]}")
        current_length += 1


list_of_nums = [170,45,75,90,802,24,2,66]
radixSort(list_of_nums)