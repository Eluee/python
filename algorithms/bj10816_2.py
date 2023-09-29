N = int(input())
list_N = list(map(int,input().split()))

M = int(input())
list_M = list(map(int,input().split()))

def binery_search(target):
    global N, list_N
    copied_list_N = list_N.copy()
    counter = start = 0
    end = N - 1
    while start <= end:
        mid = (start + end) // 2
        if copied_list_N[mid] == target:
            counter += 1
            copied_list_N.pop(mid)
            # 같은 숫자가 또 있을 수 있으므로 start, end 인덱스 초기화
            start = 0
            end = N - counter - 1      
        elif copied_list_N[mid] < target:
                start = mid + 1
        else:
                end = mid - 1   
    return counter

list_N.sort()
print( *[binery_search(num) for num in list_M] )
        
                
            
            
    

