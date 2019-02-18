# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        temp = arr[smallest_index]
        arr[smallest_index] = arr[cur_index]
        arr[cur_index] = temp

    return arr


my_arr = [2, 5, 9, 7, 4, 1, 3, 8, 6]
print(my_arr)
arr = selection_sort(my_arr)
print(my_arr)


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        position = i
        while position > 0 and arr[position - 1] > temp:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = temp

    return arr


arr = insertion_sort(my_arr)
print(my_arr)


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    # loop through arr
    # check whether i is > i +1
    # if so, swap
    # if we go through the loop and there was at least 1 swap, we loop again
    # if there were no swaps, stop the loop
    for i in range(len(arr) - 1, 0, -1):
        for i in range(i):
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp

    return arr


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(arr)
print(arr)

# STRETCH: implement the Count Sort function below


def count_sort(arr, maximum=-1):

    return arr
