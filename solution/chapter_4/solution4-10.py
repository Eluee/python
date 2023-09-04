
def solution( weight, boxes):
    dev = weight * 0.1
    print(dev)
    return [item for item in boxes if weight - dev > item or item > weight + dev]

print(solution(600 ,[653, 670, 533, 540, 660]))