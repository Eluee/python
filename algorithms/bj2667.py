import sys

N = int(sys.stdin.readline())

map = [list(map(int,list(sys.stdin.readline().strip()))) for _ in range(N)]
result = list()
count = 0

def counter(i, j):
    global map, count
    map[i][j] = 0
    count += 1
    if i + 1 < N:
        if map[i + 1][j] == 1: counter(i + 1, j)
    if j + 1 < N:
        if map[i][j + 1] == 1: counter(i, j + 1)
    if 0 <= i - 1:
        if map[i - 1][j] == 1: counter(i - 1, j)
    if 0 <= j - 1:
        if map[i][j - 1] == 1: counter(i, j - 1)

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            count = 0
            counter(i, j)
            result.append(count)
            
result.sort()
print(len(result))
for i in result:
    print(i)