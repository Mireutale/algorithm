"""
선택 정렬 : 
"""
def selection_sort(arr):
    n = len(arr)
    # 배열 전체를 순회합니다.
    for i in range(n):
        # 최소값의 인덱스를 저장합니다.
        min_idx = i
        # 현재 인덱스(i)부터 배열 끝까지 최소값을 찾습니다.
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 최소값을 현재 위치(i)로 옮깁니다.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 선택 정렬을 테스트하기 위해 배열을 정의합니다.
arr = [64, 25, 12, 22, 11]
print("정렬 전 배열:", arr)

# 선택 정렬을 실행합니다.
selection_sort(arr)

print("정렬 후 배열:", arr)
