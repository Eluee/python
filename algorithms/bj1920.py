N = int(input())
list_N = list(map(int,input().split()))

M = int(input())
list_M = list(map(int,input().split()))

list_N.sort()

def binery_search(target):
    global list_N, N
    left = 0
    right = N - 1
    while(left <= right):
        mid = (left + right) // 2
        if list_N[mid] == target:
            return 1
        elif list_N[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return 0

for value in list_M: print(binery_search(value))
