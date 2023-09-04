
def solution(money ,chairs, desks):
    # chairs와 desks의 모든 조합의 합을 리스트로 만드는데 살 수 있는 가장 큰 값을 골라야 하므로 합이 돈보다 같거나 적은 수만 리스트에 포함
    result = [chair + desk for chair in chairs for desk in desks if chair + desk <= money]
    # result의 길이가 0 인경우 살 수 있는 것이 없으므로 0을 반환하고 아닌경우 가장 큰 값을 반환
    return  max(result) if len(result) > 0 else 0 

print(solution(7,[2, 5],[4, 3, 5]))
print(solution(7,[3],[5]))