
def solution(numbers):
    return len([number for number in str(numbers) if number in ['2', '3', '5', '7']])

print(solution(29022531))