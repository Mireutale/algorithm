"""
선택 정렬 : 가장 작은 값 또는 가장 큰 값부터 찾아서 자리로 이동시킨다.
삽입 정렬보다 바꾸는 횟수가 적어 속도가 빠르다.
"""
#increasing order
def increasing_selection_sort(arr: list):
    n = len(arr)
    for i in range(n):
        min_i = i #배정할 자리
        for j in range(i+1, n):
            if arr[min_i] > arr[j]: #더 작은 값을 찾을때마다 변경, 부호를 바꾸면 decresing order
                min_i = j 
        arr[min_i], arr[i] = arr[i], arr[min_i] #끝까지 확인한 후 가장 작은 값 이동
    return arr

arr = [16, 2, 7, -10, 1]
increasing_selection_sort(arr)
print(arr)