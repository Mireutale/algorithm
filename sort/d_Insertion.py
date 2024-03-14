"""
삽입 정렬 : 정렬할 데이터를 기준으로 왼쪽에 있는 데이터는 정렬된 리스트, 오른쪽에 있는 데이터는 정렬되지 않은 리스트로 취급한다.
왼쪽의 정렬된 리스트에 있는 값과 비교하면서 들어갈 위치에 데이터를 삽입하는 방식이다.
특징 : 미리 정렬된 경우 굉장히 정렬 속도가 빠름.
"""
#increasing order
def insertion_sort(arr : list):
    n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1): #기준값보다 왼쪽에 있는 정렬된 값
            if arr[j] < arr[j-1]: #부호를 바꾸면 decreasing order
                arr[j], arr[j-1] = arr[j-1], arr[j] 
            else:
                #이전 값들과 비교하면서 increasing인 경우 자신보다 작은 값을 만나면 그자리에서 swap을 멈추고, decreasing인 경우 자신보다 큰 값을 만나면 그자리에서 swap을 멈춘다.
                break
    return arr