import sys

N, M, L = list(map(int, sys.stdin.readline().split()))
reststop_list = sorted(list(map(int, sys.stdin.readline().split())))
reststop_list = [0] + reststop_list + [L]
reststop_list.sort()

left = 1
right = L - 1
result = 0

# 모든 빈 구간에서 일정한 거리로 나눈 몫의 합이 M과 같은 거리중 가장 작은거리
# 휴개소가 없는 구간만 구해야 하기 때문에 25번줄에서 -1을 해준다. (300의 거리에 100단위로 
# 휴개소를 지으면 딱 나뉘어 떨어지기 때문에 몫이 3이 나오는데 이는 거리가 300인 곳에도 휴개소를 지었다는 말 이므로)
# 이전 휴개소와 다음 휴개소의 거리가 300이라면 일정한 거리로 나눌때는 299에 나누어준다.

# 결국 3 1 1000
# 200 701 800 가 주어졌을때 거리가 251보다 작아지면 M개 보다 더 지어버린다.
# 그러므로 M개를 지을 수 있는 가장 작은 거리값이 251 이라는 결논


while left <= right:
    # count는 휴개소의 갯수
    count = 0
    # mid는 최대거리 
    mid = (left + right) // 2
    print(f"mid = {mid}, left = {left}, right = {right}")
    for i in range(1, len(reststop_list)):
        if reststop_list[i] - reststop_list[i - 1] > mid:
            count += (reststop_list[i] - reststop_list[i - 1] - 1)// mid
            
    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        result = mid
    
print(result)
    
        