
def solution( weight, boxes):
    # 편차를 구함
    dev = weight * 0.1
    # boxes를 순회 하면서 각원소가 편차 범위에 있는지 확인하고 범위에 없는 박스만 골라서(불량품) 새로운 리스트 생성후 리스트의 크기 반환
    return len([item for item in boxes if weight - dev > item or item > weight + dev])

print(solution(600 ,[653, 670, 533, 540, 660]))