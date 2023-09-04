

def solution(temperature, A, B):
    #temperature리스트를 사용해서 A와 B사이의 리스트에서 가장 높은 값만 리스트 컴프리헨션
    return len([x for x in temperature[A:B] if temperature[A] < x and temperature[B] < x])

print(solution([3, 2, 1, 5, 4, 3, 3, 2],1, 6))