
def solution(socks):
    return sum([ socks.count(item) // 2 for item in list(set(socks)) ])

print(solution([1, 2, 1, 3, 2, 1]))
