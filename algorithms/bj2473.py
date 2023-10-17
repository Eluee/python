N = int(input())
list_N = sorted(list(map(int, input().split())))
list_N_len = len(list_N)

best_sum = sum(list_N[-3:])
best_number = list_N[-3:]

def solution(list_N):
    # 가장 최대로 나올 수 있는 합은 list_N의 끝에서부터 3개이므로 탐색할 필요가 없다 그러므로 -3
    global list_N_len, best_sum, best_number
    for i in range(list_N_len - 3):
        target = -list_N[i]
        left = i + 1
        right = list_N_len - 1
        
        while left < right:
            total = list_N[left] + list_N[right]
            if  abs(target - total) < best_sum:
                best_sum = abs(target - total)
                best_number[0] = list_N[i]
                best_number[1] = list_N[left]
                best_number[2] = list_N[right]
            
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                best_number[0] = list_N[i]
                best_number[1] = list_N[left]
                best_number[2] = list_N[right]
                break
    
    
solution(list_N)
print(*best_number)
        
        
        