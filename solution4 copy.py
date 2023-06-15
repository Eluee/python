def solution(arr):
    freq_list = [arr.count(item) for item in list(set(arr))]
    return max(freq_list) // min(freq_list)
    
print(solution([1,2,3,3,1,3,3,2,3,2]))
