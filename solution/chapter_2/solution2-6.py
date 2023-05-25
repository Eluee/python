

def solution(floors):
    return sum( [ abs(floors[index + 1] - floors[index]) for index in range(len(floors) - 1) ])

print(solution([1, 2, 5, 4, 2]))

