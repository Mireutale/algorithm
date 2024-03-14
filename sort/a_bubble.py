"""
버블 정렬 : 리스트의 모든 값을 비교해서 크기가 다르면 두 값을 swap해서 정렬하는 방법
특징 : 쉽지만 굉장히 느린 정렬 속도를 가진다.
"""
#increasing order

def incresing_order_bubble_Sort(arr : list):
    n = len(arr) #list의 개수
    for i in range(n): #0번부터 마지막 번호까지 i이동
        for j in range(0, n-i-1): #
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap
    return arr

#decreasing order
                
def decresing_order_bubble_Sort(arr : list):
    n = len(arr) #list의 개수
    for i in range(n): #0번부터 마지막 번호까지 i이동
        for j in range(n-1, i, -1): #j는 i + 1 =번부터 마지막 번호까지 이동
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j] #swap
    return arr
