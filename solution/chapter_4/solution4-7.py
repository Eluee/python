
def solution(money ,chairs, desks):
    result = [chair + desk for chair in chairs for desk in desks if chair + desk <= money]
    return  max(result) if len(result) > 0 else 0 

print(solution(7,[2, 5],[4, 3, 5]))
print(solution(7,[3],[5]))