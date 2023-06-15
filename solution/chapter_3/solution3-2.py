
def solution(current_grade, last_grade):
    dict_1 = { id: current_grade[id] for id in range(current_grade) if current_grade[id] >= 80}
    return {}