
def reach_check(queens, current_queen):
    for point in queens:
        if point[1] == current_queen[1]:
            return False

        if point[0] - point[1] == current_queen[0] - current_queen[1]:
            return False
        if sum(point) == sum(current_queen):
            return False
    return True
    

def recursion(queens, depth):
    global N, result
    if depth == N:
        result += 1
        return
    for i in range(N):
        if reach_check(queens, (depth, i)):
            queens_cp = queens.copy()
            queens_cp.append((depth, i))
            recursion(queens_cp, depth+1)

        
result = 0
N = int(input())
recursion([],0)
print(result)