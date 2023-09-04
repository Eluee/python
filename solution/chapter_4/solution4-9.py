
def solution(socks):
    # 먼저 socks를set형으로 바꿔줘 중복을 제거하고 다시 list형으로 각 유형의 중복 횟수를 2로 나눈 몫을 담은 리스트를 만듦
    # 만든 리스트의 합이 곧 최대 양말 갯수
    return sum([ socks.count(item) // 2 for item in list(set(socks)) ])

print(solution([1, 2, 1, 3, 2, 1]))
