def distribute_papers(papers, papers_len, K):
    # 초기화
    recipients = 0
    remaining_papers = K

    # 각 사람에게 종이를 나눠주면서 확인
    for i in range(papers_len):

        # 현재 사람에게 줄 수 있는 종이 수 계산
        distributed_papers = papers[i]

        # 남은 종이 수 업데이트
        remaining_papers -= distributed_papers

        # 종이를 받은 사람 수 증가
        if remaining_papers >= 0:
            recipients += 1

    return recipients

# 예제 사용
papers = [1, 1, 1, 1, 1]  # 각 사람이 필요로 하는 종이 수 예시
papers_len = len(papers)  # 리스트의 길이
K = 5  # 처음 앞사람에게 전달한 종이 수
result = distribute_papers(papers, papers_len, K)
print(f"{result} 명이 종이를 필요한 만큼 받았습니다.")

