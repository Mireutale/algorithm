def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # 현재 자리수에 해당하는 숫자의 개수를 세어 count 배열에 저장합니다.
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # count 배열을 누적 합으로 수정합니다.
    for i in range(1, 10):
        count[i] += count[i - 1]

    # output 배열에 정렬된 숫자를 저장합니다.
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # output 배열을 arr 배열로 복사합니다.
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Radix 정렬을 테스트하기 위해 배열을 정의합니다.
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("정렬 전 배열:", arr)

# Radix 정렬을 실행합니다.
radix_sort(arr)

print("정렬 후 배열:", arr)
