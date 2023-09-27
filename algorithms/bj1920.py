N = int(input())
list_N = set(map(int,input().split()))

M = int(input())
list_M = list(map(int,input().split()))

for i in list_M: print(1 if i in list_N else 0)
