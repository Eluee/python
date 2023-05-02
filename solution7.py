

def solution(score):
    total = 0
    for item in score: 
        if 650 <= item and item < 800: 
            total += 1
            print(item)
    
    return total


print(solution([650, 722, 914, 558, 714, 803, 650, 679, 669, 800]))