
def solution(a, b):
    #소인수 분해 제귀함수
    def recursion(a, b):
        for i in range(min(a, b), 1, -1):
            if a%i == 0 and b%i == 0:
                resort.append(i)
                recursion(a//i, b//i)
                return
        resort.append(a)
        resort.append(b)
        return
    
    lcm = 1
    resort = []
    recursion(a, b)
    for i in resort: lcm *= i
    return lcm

print(solution(12, 14)) 