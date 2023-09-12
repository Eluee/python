def distribute_papers(papers, papers_len, K):
    # 초기화
    recipients = 0
    remaining_papers = 0

    # 줘야하는 종이의 갯수를 한명한명 비교하면서 
    # 각 사람에게 종이를 나눠주면서 확인
    for i in range(papers_len):
        # 남은 종이 수와 현재 사람이 필요한 종이 수를 합산
        total_papers = remaining_papers + papers[i]

        # 현재 사람에게 줄 수 있는 종이 수 계산
        distributed_papers = min(total_papers, K)

        # 남은 종이 수 업데이트
        remaining_papers = total_papers - distributed_papers
        print(remaining_papers)
        # 종이를 받은 사람 수 증가
        print("dis : ", distributed_papers)
        if remaining_papers > 0:
            
            recipients += 1

    # 마지막 사람까지 확인 후 남은 종이를 받을 수 있다면 마지막 사람에게 주기
    while remaining_papers > 0:
        distributed_papers = min(remaining_papers, K)
        remaining_papers -= distributed_papers
        recipients += 1

    return recipients
 
# 예제 사용
papers = [2, 4, 3, 4, 8, 9] #[2, 3, 1, 1, 4, 2]  # 각 사람이 필요로 하는 종이 수 예시
papers_len = len(papers)  # 리스트의 길이
K = 5  # 처음 앞사람에게 전달한 종이 수
result = distribute_papers(papers, papers_len, K)
print(f"{result} 명이 종이를 필요한 만큼 받았습니다.")

