# STRETCH: implement Linear Search				
def linear_search(arr, target):
  
  # TO-DO: add missing code
  for n in arr:
    if n == target:
      return arr.index(target)

  return -1   # not found


# STRETCH: write an iterative implementation of Binary Search 
def binary_search(arr, target):
  if len(arr) == 0:
    return -1 # array empty
    
  low = 0
  high = len(arr) - 1

  # TO-DO: add missing code
  middle = int(high - low / 2)
  if arr[middle] == target:
    return arr.index(target)

  elif arr[middle] < target:
    return binary_search(arr[middle:], target)

  else:
    return binary_search(arr[:middle], target)
    
  return -1 # not found


# STRETCH: write a recursive implementation of Binary Search 
def binary_search_recursive(arr, target, low, high):
  
  middle = (low+high)//2

  if len(arr) == 0:
    return -1 # array empty
  # TO-DO: add missing if/else statements, recursive calls


arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9] 

# print(binary_search(arr1, 6))
print(binary_search(arr1, -8))
print(binary_search(arr1, 0))