def heapify(arr, n, i):
    largest = i  # 가장 큰 값의 인덱스를 i로 설정합니다.
    left = 2 * i + 1  # 왼쪽 자식 노드의 인덱스를 계산합니다.
    right = 2 * i + 2  # 오른쪽 자식 노드의 인덱스를 계산합니다.

    # 왼쪽 자식 노드가 존재하고 현재 노드보다 크다면 인덱스를 업데이트합니다.
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 오른쪽 자식 노드가 존재하고 현재 노드보다 크다면 인덱스를 업데이트합니다.
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 가장 큰 값이 현재 노드가 아니라면 노드를 교환합니다.
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 변경된 부분에 대해 다시 heapify를 수행합니다.
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # 힙을 구성합니다. (max heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 힙 정렬을 수행합니다.
    for i in range(n - 1, 0, -1):
        # 최대값을 뒤로 보냅니다.
        arr[0], arr[i] = arr[i], arr[0]
        # 힙을 다시 구성합니다.
        heapify(arr, i, 0)

# 힙 정렬을 테스트하기 위해 배열을 정의합니다.
arr = [12, 11, 13, 5, 6, 7]
print("정렬 전 배열:", arr)

# 힙 정렬을 실행합니다.
heap_sort(arr)

print("정렬 후 배열:", arr)
