
import math

N = int(input())
map = {(i, j) for i in range(N) for j in range(N)}

result = []

def locate_queen(point, map):
    """ 
    퀸이 point 좌표에 있을때의 공격 가능한 좌표를 제거
    Args:
        point (_tuple_): _퀸이 위치한 x, y 좌표를 담고 있는 tuple
        map (_set_): _지도에 존재하는 좌표_
    """
    # 직선 경로
    global N
    i, j = point
    for x in range(N): 
        map.discard((x, j))
        map.discard((i, x))
        
    # 대각선 경로
    d = i - j
    if d <= 0:
        for x in range(N + d): map.discard((x, x - d))
    else:
        for x in range(0 + d, N): map.discard((x, x - d))
        
    # 반대 대각선 경로
    temp =  j + i
    if temp < N:
        for x in range(temp + 1): map.discard((x, temp - x))
    else:
        for x in range(temp + 1 - N, N ): map.discard((x, temp - x))

def solution(queens ,map):
    global N, result
    
    if len(queens) == N:
        result.append(queens)
        return
  
    for coord in map:
        queens_cp = queens.copy()
        map_cp = map.copy()
        queens_cp.append(coord)
        locate_queen(coord, map_cp )
        solution(queens_cp, map_cp)



solution([],map)
print(len(result))