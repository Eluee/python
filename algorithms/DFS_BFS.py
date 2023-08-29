
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
            if ( - 1) > 0 : prop.append((i, j))
            dict[(n,m)]

print()
