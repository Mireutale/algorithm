def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # 배열을 중간으로 나눕니다.
        left_half = arr[:mid]  # 왼쪽 부분 배열
        right_half = arr[mid:]  # 오른쪽 부분 배열

        # 왼쪽과 오른쪽 부분 배열에 대해 재귀적으로 합병 정렬을 호출합니다.
        merge_sort(left_half)
        merge_sort(right_half)

        # 두 개의 부분 배열을 합병합니다.
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 남은 요소들을 복사합니다.
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 합병 정렬을 테스트하기 위해 배열을 정의합니다.
arr = [12, 11, 13, 5, 6, 7]
print("정렬 전 배열:", arr)

# 합병 정렬을 실행합니다.
merge_sort(arr)

print("정렬 후 배열:", arr)
