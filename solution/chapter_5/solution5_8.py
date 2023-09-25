
def solution(usage):
    rule = [(430, 20) ,(570, 10), (840, 1)]
    price = 0
    for i in range(len(rule)):
        price += (usage // rule[i][1]) * rule[i][0]
        usage %= rule[i][1]
        if usage == 0:
            break
    
    return price

print(solution(35))
            
    
        