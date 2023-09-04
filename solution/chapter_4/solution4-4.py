
def solution(cards):
    colors = [ cards[index][0] for index in range(3)]
    max = 0
    for index in range(len(cards)):
        temp = colors.count(colors[index])
        if max < temp: max = temp
    if max == 1:
        return sum(map(int,[ cards[index][1] for index in range(3)]))
    elif max == 2:
        return sum(map(int,[ cards[index][1] for index in range(3)])) * 2
    else:
        return sum(map(int,[ cards[index][1] for index in range(3)])) * 3


print(solution([["blue", "2"], ["red", "5"], ["black", "3"]]))
print(solution([["blue", "2"], ["blue", "5"], ["black", "3"]]))