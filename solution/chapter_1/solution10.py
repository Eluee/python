
def solution(data):
    ave = sum(data)/len(data)
    return len([ x for x in data if x <= ave])

print(solution( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))