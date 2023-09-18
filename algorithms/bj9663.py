
N = int(input())
map = {(i, j) for i in range(N) for j in range(N)}

result = []

def remove(point, map):
    global N
    i , j = point
    for x in range(N): 
        map.discard((x, j))
        map.discard((i, x))

def solution(queens ,map):
    global N, result
    if len(queens) == N:
        result.append(queens)
        return
    for coord in list(map):
        queens_cp = queens.copy()
        map_cp = map.copy()
        queens_cp.append(coord)
        remove(coord, map_cp)
        solution(queens_cp, map_cp)



solution([],map)
print(len(result))