"""
퀵 정렬 : pivot은 어떤걸 선택해도 상관 없으나, 주어진 수열의 맨 앞에 오는 원소를 pivot으로 설정
평균적으로 가장 빠른 정렬, 이미 정렬이 거의 된 경우에는 최악의 경우
"""
#increasing order
def increasing_quick_sort(arr : list):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] #첫번째 원소를 pivot으로 설정
        left = [x for x in arr[1:] if x <= pivot]  #피벗보다 작은 값들을 모아서 리스트
        right = [x for x in arr[1:] if x > pivot]  #피벗보다 큰 값들을 모아서 리스트
        #재귀적으로 반복해서 결과 획득
        return increasing_quick_sort(left) + [pivot] + increasing_quick_sort(right)

#decreasing order
def decreasing_quick_sort(arr : list):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] #첫번째 원소를 pivot으로 설정
        left = [x for x in arr[1:] if x > pivot]  #피벗보다 큰 값들을 모아서 리스트
        right = [x for x in arr[1:] if x <= pivot]  #피벗보다 작은 값들을 모아서 리스트
        #재귀적으로 반복해서 결과 획득
        return decreasing_quick_sort(left) + [pivot] + decreasing_quick_sort(right)

def quick_sort(arr:list, low, high):
    if low >= high:
        return 0
    pivot_data = arr[low]
    left = low + 1
    right = high
    #left가 right보다 커지면 멈춤 -> 모든 값 다 확인
    while left < right:
        #왼쪽에서 올라가면서 피벗보다 작으면 left증가
        while arr[left] <= pivot_data and left < high:
            left += 1
        #오른쪽에서 내려오면서 피벗보다 크면 right감소
        while arr[right] >= pivot_data and right > low:
            right -= 1
        #left에서는 피벗보다 크고, right에서는 피벗보다 작은 값 발견
        if left < right: #찾은 두 값 swap 
            arr[left], arr[right] = arr[right], arr[left]
    #모든 값을 다 확인 하면 right가 있는 위치의 왼쪽은 전부 피벗보다 값이 작다.
    #right위치와 피벗 위치를 변환
    arr[low], arr[right] = arr[right], arr[low]
    #왼쪽에서 또 quick정렬 수행
    quick_sort(arr, low, right -1)
    #오른쪽도 마찬가지
    quick_sort(arr, right + 1, high)


arr = [16, 2, 7, -10, 1]
n=5
quick_sort(arr, 0, 4)
print(arr)