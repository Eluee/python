import sys
import queue

N = int(sys.stdin.readline())
A, B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

relative_dict = { key:[] for key in range(1, N+1)} 

for _ in range(M):
    key, value = list(map(int, sys.stdin.readline().split()))
    relative_dict[key].append(value)
    relative_dict[value].append(key)
    

visit_que = queue.Queue()
visited = set()
count = 0
result = -1

if A == B:
    result = 0
else:
    visit_que.put(A)
    visited.add(A)
while visit_que.qsize() > 0:
    current_node = visit_que.get()
  
    count += 1
    for node in relative_dict[current_node]:
        if node == B:
            result = count
            visit_que = queue.Queue()
            break
        if node not in visited:
            # visit 체크는 que에서 뺄때하는게 아니라 갈 수 있는 노드를 체크할때 Visit 체크를 한다.
            visited.add(node)
            visit_que.put(node)
    
    
print(result)
 