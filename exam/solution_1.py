def solution(votes, N, K):
    return [votes.count(i) for i in range(1, N+1)].count(K)
     
print(solution([2, 5, 3, 4, 1, 5, 1, 5, 5, 3], 5, 2))


