
import math

N = int(input())
map = [(i, j) for i in range(N) for j in range(N)]

imposs_position = {}
result = []

def locate_queen(point, imposs_position):
    """ 
    퀸이 point 좌표에 있을때 퀸을 배치하지 못하는 좌표를 포함
    Args:
        point (_tuple_): _퀸이 위치한 x, y 좌표를 담고 있는 tuple
        map (_set_): _지도에 존재하는 좌표_
    """
    # 직선 경로
    global N
    i, j = point
    for x in range(N): 
        imposs_position.add((x, j))
        imposs_position.add((i, x))
        
    # 대각선 경로
    d = i - j
    if d <= 0:
        for x in range(N + d): imposs_position.add((x, x - d))
    else:
        for x in range(0 + d, N): imposs_position.add((x, x - d))
        
    # 반대 대각선 경로
    temp =  j + i
    if temp < N:
        for x in range(temp + 1): imposs_position.add((x, temp - x))
    else:
        for x in range(temp + 1 - N, N ): imposs_position.add((x, temp - x))

def solution(queens ,imposs_position):
    global N, result, map
    
    if len(queens) == N:
        result.append(queens)
        return
  
    for coord in map:
        if coord not in imposs_position:
            queens_cp = queens.copy()
            imposs_position_cp = imposs_position.copy()
            queens_cp.append(coord)
            locate_queen(coord, imposs_position_cp )
            solution(queens_cp, imposs_position_cp )



solution([],set())
print(len(result))