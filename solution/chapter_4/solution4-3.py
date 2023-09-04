
def solution(people):
    sizes = [120, 105, 100, 95]
    result = [0, 0, 0, 0]
    for item in people:
        for index, value in enumerate(sizes):
            if item < value:
                flag = index
        result[flag] += 1
    return result[::-1]

print(solution([97, 102, 93, 100, 107]))
                
                