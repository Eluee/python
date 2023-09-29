N = int(input())
list_N = list(map(int,input().split()))

M = int(input())
list_M = list(map(int,input().split()))


# 리스트의 같은 숫자의 반복이 시작되는 위치를 이진탐색으로 찾는 함수
def binery_search(target):
    global N, list_N
    end = N - 1
    start = 0
    while start < end:

        mid = (start + end) // 2
        if list_N[mid] < target:
            start = mid + 1
        elif list_N[mid] > target:
            end = mid - 1
        else:
            # 반복 시작 위치를 찾기 위해 end를 끌어옴
            end = mid
    return end

#해당 인댁스부터 target이 몇번 반복되는지 확인 후 횟수 반환
def repeat_count(target, index):
    global N, list_N
    counter = 0
    for i in range(index, N):
        if list_N[i] != target:
            return counter
        else:
            counter += 1
    return counter

list_N.sort()
print( *[repeat_count(num ,binery_search(num)) for num in list_M] )
        
                
            
            
    

