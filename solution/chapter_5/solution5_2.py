
def solution(time_table):
    time_table_cp = time_table.copy()
    time_table_cp.reverse()
    return time_table[:len(time_table) - time_table_cp.index(1)].count(0)
    


print(solution([0, 1, 0, 0, 1, 0, 1, 0, 0, 0]))