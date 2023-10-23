import sys

N, M, L = list(map(int, sys.stdin.readline().split()))
reststop_list = sorted(list(map(int, sys.stdin.readline().split())))
reststop_list = [0] + reststop_list + [L]

dist_list = sorted([reststop_list[i+1] - reststop_list[i] for i in range(len(reststop_list) - 1)],reverse=True)

for i in range(M):
    if dist_list[i] % 2 == 0:
        dist = [dist_list[i] // 2, dist_list[i] // 2 ]
    else:
        dist = [dist_list[i] // 2, dist_list[i] // 2 + 1]
        
    left = i + 1
    right = len(dist_list) - 1
    
    while(left < right):
        mid = (left + right) // 2
        if  dist_list[mid] < dist[0] :
            right = mid - 1
        else:
            left = mid + 1
    
    print(dist_list, dist[0])
    dist_list.insert(left , dist[0])
    dist_list.insert(left, dist[1])

print(dist_list)
print(dist_list[M])

            
            
            
# 찾으려고 하는 숫자는 dist_list[i] 보다 큰 숫자가 시작하는 곳
        