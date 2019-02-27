### helper function
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range( 0, elements ):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


### recursive sorting function
def merge_sort( arr ):
    # Set the base 
    if len( arr ) > 1:
        # 
        left = merge_sort( arr[ 0 : len( arr ) / 2 ] )
        right = merge_sort( arr[ len( arr ) / 2 : ] )
        arr = merge( left, right )   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort( arr, low, high ):
        # base case
    if high-low <= 0:
        return arr

    pivot = low
    for i in range(low + 1, high + 1):
        # print("This is I", [i])
        # print(arr)
        if arr[i] < arr[pivot]:
            # move to LHS of pivot - 2 swaps
            temp = arr[i]
            arr[i] = arr[pivot + 1]
            arr[pivot + 1] = temp
            # print(arr)
            # print("This is I after move LHS of pivot 1 swap", [i])
            temp = arr[pivot]
            arr[pivot] = arr[pivot + 1]
            arr[pivot + 1] = temp
            pivot += 1
            print(arr)
            # print("This is I after move LHS of pivot 2 swaps", [i])

            #path to the base case?
            #Call quick_sort

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
