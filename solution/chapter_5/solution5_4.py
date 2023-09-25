
def solution(taekwondo, running, shoting):
    total_score = 0
    
    #태권도 점수
    total_score +=  250 if taekwondo >= 25 else taekwondo * 8
    # 달리기 점수
    total_score += 250 + ((60 - running) * 5)
    # 사격 점수
    total_score +=  sum(shoting) + (100 if shoting.count(10) >= 7 else 0)
    return total_score

print( solution(27, 63, [9, 10, 8, 10, 10, 10, 7, 10, 10, 10]))
    
    