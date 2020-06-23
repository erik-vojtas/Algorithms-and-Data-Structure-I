# Merge Sort Algorithm
# https://www.programiz.com/dsa/merge-sort
# split an array into two halves and then again until we get lists which consist one item, merge and sort then two lists together, then again until we get full list which is ordered

# https://www.studytonight.com/data-structures/merge-sort
# Worst Case Time Complexity [Big-O]: O(n*log n)
# Best Case Time Complexity [Big-omega]: O(n*log n)
# Average Time Complexity [Big-theta]: O(n*log n)

# Video:
# https://www.youtube.com/watch?v=M5kMzPswo20


comparisons = 0
recursions = 0

# decorator to count recursion
def countRecursion(fn):
    def wrappedFunction(*args):
        global recursions
        if fn(*args):
            recursions += 1
    return wrappedFunction

@countRecursion
def mergeSort(list):
    global comparisons
    global recursions
    if len(list) > 1:
        mid = len(list) // 2
        left_list = list[:mid]
        right_list = list[mid:]
        print("left list:", left_list)
        print("right list:", right_list)
        mergeSort(left_list)    # recursion
        mergeSort(right_list)   # recursion
        i = j = k = 0


        while i < len(left_list) and j < len(right_list):
            comparisons += 1
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i += 1
            else:
                list[k] = right_list[j]
                j += 1
            k += 1
            print("merge lists:", "left:", left_list, "right:", right_list)

        while i < len(left_list):
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            list[k] = right_list[j]
            j += 1
            k += 1

    return True


array = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print(f"Unsorted array: {array}.")
mergeSort(array)
print(f"Sorted array: {array}, comparisons: {comparisons}, recursions: {recursions}.")