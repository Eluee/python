
def solution(speed, cars):
    rule = [ int(speed * i) for i in [1.3, 1.2, 1.1]]
    panalty_dict = [7, 5, 3]
    total_panalty = 0
    for car in cars:
        if car >= rule[0]:
            total_panalty += panalty_dict[0]
            continue
        if car >= rule[1]:
            total_panalty += panalty_dict[1]
            continue
        if car >= rule[2]:
            total_panalty += panalty_dict[2]
            continue
    return total_panalty
    
print(solution(100, [110, 98, 125, 148, 120, 112, 89]))