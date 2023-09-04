

def solution(papers, papers_len, K):
    # 리스트를 순차적으로 방문하면서 인댁스와 값을 가져옴
    for index, value in enumerate(papers):
        # 남은 종이가 0보다 작을 경우 마지막 사람에게 줄 종이가 부족했으므로 현제인댁스의 - 1 반환
        if K < 0: return index - 1
        # 남는 종이가 0일경우 마지막 사람에게 나눠준 종이가 딱 나뉘어 떨어졌기 때문에 인댁스 그대로 반환
        elif K == 0: return index
        # 종이가 남아 있는 경우 다음 사람이 필요한 종이의 수를 뺌 
        else: K -= value
    # 반복문을 탈출했다는건 종이가 모든 사람을 주고도 남았다는 의미 이므로 papers의 길이를 그대로 반환
    return papers_len
print(solution([2, 4, 3, 2, 1], 5, 10))
print(solution([2, 4, 3, 2, 1], 5, 14))