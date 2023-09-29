K, N = map(int, input().split())
cable_list = [int(input()) for _ in range(K)]
    


def valid_cable(cut_length):
    global cable_list
    return sum([cable // cut_length for cable in cable_list])

left = 1
# 안자르는 케이블이 존재할 수 있기 때문에 가장 큰 값으로 시작
right = max(cable_list)

while left < right :
    mid = (left + right) // 2 + 1
    cut_cables = valid_cable(mid)
    if N <= cut_cables:
        left = mid
    else:
        right = mid - 1

print(left)

