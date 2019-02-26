# Complete the selection_sort() function below in class with your instructor
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        minimum = i
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        for j in range(minimum, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        # TO-DO: swap
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
  for i in range(1, len(arr)):
    j = i - 1
    while arr[j] > arr[j + 1] and j >= 0:
      arr[j], arr[j + 1] = arr[j + 1], arr[j]
      j-=1
    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):

    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr