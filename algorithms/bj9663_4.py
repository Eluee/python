
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
    reach = {}
    for x in range(N): 
        reach.add((x, j))
        reach.add((i, x))
        
    # 대각선 경로
    d = i - j
    if d <= 0:
        for x in range(N + d): 
            reach.add((x, x - d))
    else:
        for x in range(0 + d, N):
            reach.add((x, x - d))
    # 반대 대각선 경로
    temp =  j + i
    if temp < N:
        for x in range(temp + 1):
            reach.add((x, temp - x))
    else:
        for x in range(temp + 1 - N, N ):
            reach.add((x, temp - x))

def solution(queens ,map):
    global N, result
    
    if len(queens) == N:
        result.append(queens)
        view_table(queens)
        return
  
    for index in range(len(map)):
        queens_cp = queens.copy()
        map_cp = map[index + 1:]
        queens_cp.append(map[index])
        locate_queen(map[index], map_cp )
        solution(queens_cp, map_cp)

def view_table(queens):
    table = [['0' for _ in range(N)] for _ in range(N)]
    for coord in queens:
        table[coord[0]][coord[1]] = '#'
    
    print(queens)
    for row in table:
        print(* row)
    print()

N = int(input())
map = [(i, j) for i in range(N) for j in range(N)]
result = []


solution([],map)
print(len(result))