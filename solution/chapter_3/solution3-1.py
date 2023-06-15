
def solution(scores, n):
    cp_scores = scores
    cp_scores.sort(reverse = True)
    return cp_scores.index(scores[n])

print(solution([20, 60, 98, 59], 3))