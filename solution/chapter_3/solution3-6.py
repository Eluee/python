
# 길이를 6으로 나누었을때 나머지가 0, 3, 5, 이면 가능한 리스트

def solution(length):
  tile = ['R', 'R', 'R', 'G', 'G', 'B']
  return [ tile[i%6] for i in range(length)] if length % 6 in [0, 3, 5] else -1

print(solution(16))
