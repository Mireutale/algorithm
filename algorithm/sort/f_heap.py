"""
힙 정렬 : 합병 정렬에서는 추가적인 저장공간이 필요하지만, 힙 정렬에서는 일정한 양의 저장 공간만 추가로 필요하다.
max 완전 이진 트리구조를 계속해서 만들어서 root노드에 존재하는 max값들을 모아 정렬하는 방법.

            0
    1               2
3       4       5       6
...

위와 같은 형태가 트리 구조이고, 이 구조에서 왼쪽 자식은 부모의 배열 인덱스1에서 *2 + 1을 한것과 같고, 오른쪽 자식은 부모의 배열 인덱스에서 *2 + 2를 한것과 같다.
이유는 배열의 시작이 1이 아닌 0이기 때문이다.

또한 힙 구조를 만들때, n//2, -1, -1, -1을 사용한다.
부모가 될수 있는 가장 작은 값이 n이 힙 사이즈 일때, n//2 - 1이기 때문이고 여기서부터 0까지 -1씩 줄여나가는 것을 의미한다.
"""

def heapify(arr, n, i):
    """
    힙 구조 생성 == 최대 완전 이진 트리 구조
    n은 heap의 크기와 동일하고, 왼쪽 또는 오른쪽 자식 중에서 부모(largest)보다 크면 largest의 값을 자식의 인덱스로 변경하고
    largest가 기존의 부모가 아니라면(!= i) 부모와 위치를 바꿔준다.
    이 함수를 호출하면 가장 큰 값이 root노드에 오게된다.
    """
    largest = i  # 가장 큰 값의 인덱스를 i로 설정합니다.
    left = 2 * i + 1  # 왼쪽 자식 노드의 인덱스를 계산합니다.
    right = 2 * i + 2  # 오른쪽 자식 노드의 인덱스를 계산합니다.

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
    return arr

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1): #i를 n-1에서부터 1까지 반복하면서 가장 큰 값을 하나씩 arr배열의 가장 마지막으로 보낸다.
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0) #root노드에 다시 가장 큰 값을 옮기는 작업
    return arr