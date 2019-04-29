# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
             



        # TO-DO: swap




    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    swapped = False
    j = 0
    while j < len(arr):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                temp1 = arr[i]
                temp2 = arr[i-1]

                arr[i] = temp2
                arr[i-1] = temp1
                
                swapped = True
                j+=1
            elif swapped == True and arr[i] > arr[i-1] and j > len(arr):
                j = 0
            elif arr[i] > arr[i-1]:
                j+=1
                if j > len(arr):
                    j = 0
                    swapped = False
                elif arr[i] > arr[i-1] and swapped == False and j == len(arr):
                    break
    
            
    return arr 


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr


arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(bubble_sort(arr1))