
def solution(stuffs):
    #리스트 안에서 3이하인 리스트와 3초과인 리스트를 나눈뒤 각 리스트를 합하여 둘중 큰수를 반환 
    return max(sum([value for value in stuffs if value > 3]),sum([value for value in stuffs if value <= 3]))

print(solution([5, 3, 4, 2, 3, 2]))