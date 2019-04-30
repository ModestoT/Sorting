# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    a = b = i = 0
    
    while a < len(arrA) and b < len(arrB):
      if arrA[a] <= arrB[b]:
        merged_arr[i] = arrA[a]
        a += 1
      else:
        merged_arr[i] = arrB[b]
        b += 1
      i += 1

    while a < len(arrA):
      merged_arr[i] = arrA[a]
      a+=1
      i+=1
    while b < len(arrB):
      merged_arr[i] = arrB[b]
      b+=1
      i+=1
      
    print(merged_arr)
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) > 1:
      middle = int(len(arr)/ 2)
      arr1 = merge_sort(arr[:middle])
      arr2 = merge_sort(arr[middle:])

      merge(arr1, arr2)
    
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

merge_sort(arr1)