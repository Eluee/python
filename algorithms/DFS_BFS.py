
def create_graph():
    """
    예제 graph 생성
    """
    graph = dict()
    graph['A'] = ['B', 'C']
    graph['B'] = ['A', 'D']
    graph['C'] = ['A', 'G', 'H', 'I']
    graph['D'] = ['B', 'E', 'F']
    graph['E'] = ['D']
    graph['F'] = ['D']
    graph['G'] = ['C']
    graph['H'] = ['C']
    graph['I'] = ['C', 'J']
    graph['J'] = ['I']
    return graph


def coord_to_graph(n, m):
    """
    n * m 크기의 2차원 지도의 좌표를 graph로 만들어주는 함수
    
    """
    graph = dict()
    for i in range(n):
        for j in range(m):
            prop = list()
            if (i - 1) > 0 : prop.append((i, j))
            dict[(n,m)]

def diagonal_1(i, j, N):
    """
    bj9663_2 문제를 위한 실험 코드 퀸을 N * N 크기의 맵의 (i, j)에 배치 했을때 
    이동 가능한 경로를 모두 '#'으로 바꿔서 출력

    Args:
        i (int): x좌표 
        j (int): y좌표
        N (int): 맵의 크기
    """
    map = [['0' for _ in range(N)]for _ in range(N)]
    #직선
    for x in range(N): map[x][j] = '#'
    for x in range(N): map[i][x] = '#'
    #대각선
    d = i - j
    if d <= 0:
        for x in range(N + d): map[x][x - d] = '#'
    else:
        for x in range(0 + d, N): map[x][x - d] = '#'
    #대각선 반대
    temp =  j + i
    if temp < N:
        for x in range(temp + 1): map[x][temp - x] = '#'
    else:
        for x in range(temp + 1 - N, N ): map[x][temp - x] = '#'
        
    for item in map:
        print(item)

def diagonal_2(i, j, N):
    """
    bj9663_2 문제를 위한 실험 코드 퀸을 N * N 크기의 맵의 (i, j)에 배치 했을때 
    이동 가능한 대각선 경로를 모두 '#'으로 바꿔서 출력

    Args:
        i (int): x좌표 
        j (int): y좌표
        N (int): 맵의 크기
    """
    map = [['0' for _ in range(N)] for _ in range(N)]

    temp =  j + i
    if temp < N:
        for x in range(temp + 1): map[x][temp - x] = '#'
    else:
        for x in range(temp + 1 - N, N ): map[x][temp - x] = '#'
    
    for item in map:
        print(item)
        

diagonal_1(3, 2, 5)
