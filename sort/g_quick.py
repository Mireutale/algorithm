def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]  # 피벗을 첫 번째 요소로 선택합니다.
        left = [x for x in arr[1:] if x <= pivot]  # 피벗보다 작거나 같은 요소들을 모읍니다.
        right = [x for x in arr[1:] if x > pivot]  # 피벗보다 큰 요소들을 모읍니다.
        # 왼쪽 부분 배열, 피벗, 오른쪽 부분 배열을 재귀적으로 정렬하여 결합합니다.
        return quick_sort(left) + [pivot] + quick_sort(right)

# 퀵 정렬을 테스트하기 위해 배열을 정의합니다.
arr = [10, 7, 8, 9, 1, 5]
print("정렬 전 배열:", arr)

# 퀵 정렬을 실행합니다.
arr = quick_sort(arr)

print("정렬 후 배열:", arr)
