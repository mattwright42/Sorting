# helper function


def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
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


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0:int(len(arr) / 2)])
        right = merge_sort(arr[int(len(arr) / 2):])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort(arr, low, high):
    if low < high:
        split = partition(arr, low, high)
        quick_sort(arr, low, split - 1)
        quick_sort(arr, split + 1, high)
    return arr


def partition(arr, low, high):

    pivot = arr[low]
    leftmark = low + 1
    rightmark = high
    done = False

    while not done:
        print(arr)
        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark = leftmark + 1
        while arr[rightmark] >= pivot and rightmark >= leftmark:
            rightmark = rightmark - 1
        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
    temp = arr[low]
    arr[low] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(arr, 0, len(arr) - 1)
print(arr)

# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
