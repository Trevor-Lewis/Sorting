# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_index]:
                cur_index = j
            if cur_index != i:
                arr[i], arr[cur_index] = arr[cur_index], arr[i]



        # TO-DO: swap




    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    for i in range(1, len(arr)):
        current_element = arr[1]
        j = i -1
        while j >= 0 and current_element < arr[j]
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    is_sorted = False
    while not is_sorted:
        is_sorted: True
        for i in range(len(arr) - 1)
            if arr[i] > arr[i + 1]
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                is_sorted = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr