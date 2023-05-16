
def solution(arr):
    answare = ''.join([x for x in arr if len(x) >= 5])
    return "ampty" if len(answare) < 1 else answare

print(solution(["my", "favo", "col", "is", "vio"]))

