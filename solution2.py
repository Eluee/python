def solution(price, grade):
    level = {"S":0.95, "G":0.9, "V":0.85}
    return int(level[grade] * price)

print(solution(2500, "V"))