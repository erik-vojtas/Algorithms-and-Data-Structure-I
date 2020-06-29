# Linear Search Algorithm
# https://www.programiz.com/dsa/linear-search
# One of the easiest search algorithm, goes through each item in list.

def linearSearch(num, list_of_nums):
  for i,n in enumerate(list_of_nums): # if
      if n == num:
          print(f'Item: {n} has been found in position: {i+1}.')
          return True


list_of_nums = [2,11,7,6,1,5,7,3,1]
linearSearch(7, list_of_nums)