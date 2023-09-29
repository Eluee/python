N = int(input())
list_N = list(map(int,input().split()))

M = int(input())
list_M = list(map(int,input().split()))


# 이진 탐색을 통해 리스트의 같은 숫자의 반복이 시작되는 위치를 찾고 마지막위치를 찾아서 반복횟수를 반환
def binery_search(target):
    global N, list_N
    end = N - 1
    start = 0
    # 반복시작 위치 찾기 end가 곧 시작위치
    while start < end:
        mid = (start + end) // 2
        if list_N[mid] < target:
            start = mid + 1
        elif list_N[mid] > target:
            end = mid - 1
        else:
            # 반복 시작 위치를 찾기 위해 end를 끌어옴
            end = mid

    
    if list_N[end] != target:
        # 해당 target이 리스트에 없을경우
        return 0
    else:
        if end == N - 1:
            # 해당 target이 리스트에 있으나 끝에 있는 경우
            return 1
        elif list_N[end + 1] != target:
            # 해당 target이 반복되지 않는 경우
            return 1
        else:
            # target이 반복이 되는 경우
            start_repeat = end
            start = end
            end = N - 1
            # 끝 위치 찾기
            while start < end:
                mid = (start + end) // 2 + 1
                if list_N[mid] < target:
                    start = mid + 1
                elif list_N[mid] > target:
                    end = mid - 1
                else:
                    # 반복  끝위치를 찾기 위해 end를 끌어옴
                    start = mid
            end_repeat = start
            return end_repeat - start_repeat + 1
    
list_N.sort()
print( *[binery_search(num) for num in list_M] )
   
                
            
            
    

