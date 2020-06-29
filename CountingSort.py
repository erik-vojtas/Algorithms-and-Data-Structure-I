# Counting Sort Algorithm
# https://www.programiz.com/dsa/counting-sort

def countingSort(num, list_of_n):
    print(f"Unsorted list: {list_of_nums}.")
    count_list = []
    sorted_list = []
    for y in range(len(list_of_nums)): # creates a sorted_list with length of list_of_n, all values are equal to 0
        sorted_list.append(0)
    for x in range(0, max(list_of_n)+1): # creates a count_list with length of max value of list_of_n, all values are equal to 0
        count_list.append(0)
    # print(count_list)
    for i, n in enumerate(list_of_n): # count_list gets real values of occurrences of each digit in list_of_n
        count_list[n] = list_of_n.count(n)
    print(f"Count list: {count_list}.")
    for i,n in enumerate(count_list): # modifies count_list by adding the previous count
        if i < len(count_list)-1:
            count_list[i+1] = count_list[i] + count_list[i+1]
    print(f"Modified count list: {count_list}.")
    for i, n1 in enumerate(list_of_n): # loop over list_of_n
        for j, n2 in enumerate(count_list): # loop over count_list
            if n1 == j: # if value of list_of_n equals to index of count_list then
                sorted_list[n2-1] = n1 # sorted list gets a value - n1 at index n2-1
                count_list[n1] = n2-1 # after placing each element at its correct position, decrease its count by one
    print(f"Sorted list: {sorted_list}.")

searched_num = 7
list_of_nums = [2,11,7,6,1,5,7,12,3,1]

countingSort(searched_num, list_of_nums)