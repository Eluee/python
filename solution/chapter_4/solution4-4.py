
def solution(cards):
    # color부분을 다루기 쉽게 2차원 리스트의 color부분만 따로 빼서 1차원 리스트로 만듦
    colors = [ cards[index][0] for index in range(3)]
    max = 0
    # colors 리스트의 가장 많은 중복을 횟수를 구함 
    for index in range(len(cards)):
        temp = colors.count(colors[index])
        if max < temp: max = temp
    #중복 횟수에 따라서 점수를 계산
    if max == 1:
        return sum(map(int,[ cards[index][1] for index in range(3)]))
    elif max == 2:
        return sum(map(int,[ cards[index][1] for index in range(3)])) * 2
    else:
        return sum(map(int,[ cards[index][1] for index in range(3)])) * 3


print(solution([["blue", "2"], ["red", "5"], ["black", "3"]]))
print(solution([["blue", "2"], ["blue", "5"], ["black", "3"]]))