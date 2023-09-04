
def solution(number):
    return abs(number - int(str(number)[::-1])) 

print(solution(120))
print(solution(23))

