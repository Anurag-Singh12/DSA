def Divide(arr, l, r):
    if (l < r):
        m = (l + r) // 2
        Divide(arr, l, m)
        Divide(arr, m + 1, r)
        merge(arr, l, m, r)


def merge(arr, l, m, r):
    s1 = m - l + 1
    s2 = r - m

    Left = [0] * s1
    Right = [0] * s2

#copying into another array
    for i in range(s1):
        Left[i] = arr[l + i]
    
    for j in range(s2):
        Right[j] = arr[m + 1 + j]

# initiaizing index
    i = j = 0
    k = l

    while (i < s1 and j < s2):
        if (Left[i] < Right[j]):
            arr[k] = Left[i]
            i = i + 1
            k = k + 1
        else:
            arr[k] = Right[j]
            j = j + 1
            k = k + 1

#for remaining elements
    while (i < s1):
        arr[k] = Left[i]
        i = i + 1
        k = k + 1

    while (j < s2):
        arr[k] = Right[j]
        j = j + 1
        k = k + 1

arr = [21, 45, 24, 89, 7, 5, 10]
Divide(arr, 0, len(arr) - 1)
print(arr)