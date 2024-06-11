import sys

A, B = list(map(int, sys.stdin.readline().split()))
result = -1

def DFS(num, depth):
    global B, result
    if B < num:
        return
    if B == num:
        result = depth
        return
    DFS(num * 2, depth + 1)
    DFS((num * 10) + 1, depth + 1)

DFS(A, 1)
print(result)



