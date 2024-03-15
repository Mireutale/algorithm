def insertion_sort(arr):
    for i in range(1, n):
            global comparison
            for j in range(i, 0, -1):
                if arr[j] < arr[j-1]: 
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    comparison += 1
                else:
                    comparison += 1
                    break
            if(arr[i] == arr[k]):
                print(comparison)
    return arr

def selection_sort(arr: list, key):
    for i in range(n):
        min_i = i
        for j in range(i+1, n):
            if arr[min_i] > arr[j]:
                min_i = j 
        arr[min_i], arr[i] = arr[i], arr[min_i]
        if i == key:
            for t in range(n):
                print(arr[t])
    return arr

def heapify(arr, n, i):
    min = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[min]:
        min = l

    if r < n and arr[r] < arr[min]:
        min = r

    if min != i:
        arr[i], arr[min] = arr[min], arr[i]
        heapify(arr, n, min)

def heap_sort(arr, k):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        if k == n - i:
            for a in range(i):
                print(arr[a])

def quick_sort(arr, s, e):
    global quick_pass
    if s > e:
        return
    pivot_data = s
    l = s + 1
    r = e
    quick_pass += 1
    while l <= r:
        while l <= e and arr[l] <= arr[pivot_data]:
            l += 1
        while r > s and arr[r] >= arr[pivot_data]:
            r -= 1
        if l > r:
            arr[r], arr[pivot_data] = arr[pivot_data], arr[r]
        else:
            arr[l], arr[r] = arr[r], arr[l]
    if quick_pass == k:
        for t in range(n):
            print(arr[t])
    quick_sort(arr, s, r - 1)
    quick_sort(arr, r + 1, e)
        
    
select, k = map(int, input().split())
n = int(input())
arr = []
for a in range(n):
    comparison = 0
    arr.append(int(input()))
if select == 1:
    insertion_sort(arr)
elif select == 2:
    key = k - 1
    selection_sort(arr, key)
elif select == 3:
    heap_sort(arr, k)
else:
    quick_pass = 0
    quick_sort(arr, 0, n-1)