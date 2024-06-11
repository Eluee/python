import sys

N = int(sys.stdin.readline())
A, B = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

relative_dict = { key:[] for key in range(1, N+1)}
result = -1 

for _ in range(M):
    key, value = list(map(int, sys.stdin.readline().split()))
    relative_dict[key].append(value)
    relative_dict[value].append(key)

def DFS(current_node, visited, depth):
    global relative_dict, result
    if current_node == B:
        result = depth
        return
    
    visited_copy = visited.copy()
    visited_copy.add(current_node)
    for node in relative_dict[current_node]:
        if node not in visited_copy:
            DFS(node, visited_copy,  depth + 1)
    
DFS(A,set(),0)
print(result)

            
