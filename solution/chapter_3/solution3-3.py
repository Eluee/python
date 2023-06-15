
def solution(scorse):
    return (sum(scorse) - min(scorse) - max(scorse)) // (len(scorse) - 2)

print(solution([35, 28, 98, 34, 20, 50, 85, 74, 71, 7]))