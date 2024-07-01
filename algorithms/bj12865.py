
import sys
N, K = list(map(int, sys.stdin.readline().split()))
max_value = 0

# 
# 리스트 컴프리헨션에서 변수를 재사용하여 조건 확인
items = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]
itemsLen = len(items)
def recursion (current_weight, current_value, index ):
    global K, itemsLen, items, max_value
    for i in range(index, itemsLen):
        
        next_weight = items[i][0] + current_weight
        if next_weight > K : continue
        
        next_value = items[i][1] + current_value
        if max_value < next_value: max_value = next_value
    
        recursion(next_weight, next_value, i+1)
        
recursion(0, 0, 0)
print(max_value)

