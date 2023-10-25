import sys
# 백준 
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
#2 초	128 MB	38321	13973	10255	37.430%
# 문제
# 세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 
# 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.

# 배열 A와 B의 인덱스는 1부터 시작한다.

# 입력
# 첫째 줄에 배열의 크기 N이 주어진다. N은 10^5보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. 
# k는 min(10^9, N^2)보다 작거나 같은 자연수이다.

# 출력
# B[k]를 출력한다.

N = int(sys.stdin.readline())
k = int(sys.stdin.readline())

index = 0

# 인댁스가 1부터 시작
for target in range(1, N + 1):
    # target값이 나올 수 있는 i, j의 경우의수를 이분탐색기법으로 완전 탐색 해서 갯수를 기록 
    count = 0
    left = 1
    right = target
    while(left <= right):
        
    





