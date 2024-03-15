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
        #for t in range(n):
          print(arr)
    quick_sort(arr, s, r - 1)
    quick_sort(arr, r + 1, e)

select, k = map(int, input().split())
n = int(input())
arr = []
for a in range(n):
    arr.append(int(input()))

2
quick_pass = 0
quick_sort(arr, 0, n-1)