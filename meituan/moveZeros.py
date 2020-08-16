def moveZeros(arr, n):
    zeros = 0
    i = 0
    for i in range(n):
        if arr[i] != 0:
            arr[i-zeros] = arr[i]
        else:
            zeros += 1
    i = n - zeros
    while i < n:
        arr[i] = 0
        i += 1
    return arr
#arr = [1, 7, 0, 2, 3, 0, 4, 8]
#print(moveZeros(arr, 8))

def moveZeros2(arr, n):
    j = 0
    i = 0
    for i in range(n):
        if arr[i] != 0:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            j += 1
    return arr

#print(moveZeros2(arr, 8))
arr = [3, 1, 2, 4, 5, 8]

def partition(arr, L, R):
    pivot = arr[R]
    i = 0
    j = L
    for i in range(L,R):
        if arr[i] < pivot:
            temp = arr[j]
            arr[j] = arr[i]
            arr[i] = temp
            j += 1
    temp = arr[j]
    arr[j] = arr[R]
    arr[R] = temp
    return j
def quicksort(arr, L, R):
    if L < R:
        M = partition(arr, L, R)
        quicksort(arr, L,  M-1)
        quicksort(arr, M+1, R)
    return arr
print(quicksort(arr, 0, 5))