import sys
import queue

N, M, V = list(map(int, sys.stdin.readline().split()))

# 노드와 간선을 직관적으로 구분하기 위해 딕셔너리 사용
dict_N = {i:[] for i in range(1,N + 1)}

result = []

for _ in range(M):



    key, value = list(map(int, sys.stdin.readline().split()))
    # 간선이 양방향이므로 양쪽 모두 생성
    dict_N[key].append(value)
    dict_N[value].append(key)
    
for i in range(1,N+1):
    # 방문 순서가 가장 낮은 순으로 방문하기 위한 정렬
    dict_N[i].sort()
    

def DFS_search(start):
    global dict_N, result
    # 함수가 호출 되었다는 것은 새로운 노드 탐색을 했다는 의미이므로 기록
    result.append(start)
    # start와 이어진 간선을 모두 탐색
    for node in dict_N[start]:
        # 이어진 길이 탐색을 했던곳 인지 확인 후 탐색한 곳이 아니라면 해당노드를 탐색하기 위해 제귀호출
        if node not in result:
            DFS_search(node)

def BFS_search(start):
    global result, dict_N
    # 방문 해야할 노드를 기록할 Queue생성
    visit_que = queue.Queue()
    # 방문해야할 첫번째 노드가 start이므로 start를 첫번째 노드로 넣어둠
    visit_que.put(start)
    # 큐의 크기가 0보다 크다면 아직 방문해야할 노드가 남아있는 것 이므로 다시 반복
    while visit_que.qsize() > 0:
        # 노드 방문
        current_node = visit_que.get()
        # 방문한 노드를 result에 기록 만약 result에 존재한다면 기록하지 않음
        if current_node not in result:
            result.append(current_node)
        # 해당 노드와 이어져있는 노드를 순회
        for node in dict_N[current_node]:
            #이어져있는 노드가 result에 없다면 방문 해야할 노드이므로 queue에 넣기
            if node not in result:
                visit_que.put(node)
    
    
DFS_search(V)
print(*result)

result = []
BFS_search(V)
print(*result)