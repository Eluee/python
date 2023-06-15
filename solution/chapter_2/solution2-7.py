def solution( value, unit):
    return int((value - 32) / 1.8 if unit == 'F' else (value * 1.8) + 32)

print(solution(527, "C"))