
def solution(korean, english):
    # 수학 점수를 구하는 공식
    math = (70 * 3) - korean - english
    return math if math <= 100 else -1

print(solution(70, 60))