# Bucket Sort Algorithm
# https://www.programiz.com/dsa/bucket-sort

import math

def bucketSort(list_of_items):
    print(f"Unsorted list: {list_of_items}.")
    bucket_list = [] # defines bucket_list
    sorted_list = [] # defines sorted_list
    for x in range(10): # creates 10 empty bucket_list as empty lists
        bucket_list.append([])
    print(f"Empty bucket list: {bucket_list}.")
    # method math.floor() returns the floor of x - the largest integer less than or equal to x
    # method math.ceil() returns ceiling value of x - the smallest integer not less than x
    divider = math.ceil((max(list_of_items) + 1) / len(bucket_list)) # defines divider max_value + 1 / len(bucket_list)
    for i in range(len(list_of_items)): # loop over all items in list
        outcome = math.floor(list_of_items[i] / divider) # computation
        bucket_list[outcome].append(list_of_items[i]) # append each item into bucket
    print(f"Bucket list with all items: {bucket_list}.")
    for bucket in bucket_list: # loop over all bucket_list
        #sorted_list.extend(bucket)
        sorted_list += sorted(bucket) # sorts each bucket and combines them together
    print(f"Sorted list: {sorted_list}.")

list_of_nums = [22,45,12,8,10,6,72,81,33,18,50,14]
bucketSort(list_of_nums)