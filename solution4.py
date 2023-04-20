def solution(arr):
    max_freq = 0
    min_freq = arr.count(arr[0])
    for item in list(set(arr)):
        freq = arr.count(item)
        if max_freq < freq:
            max_freq = freq
        if min_freq > freq:
            min_freq = freq
        
    return int(max_freq / min_freq)
    
print(solution([1,2,3,3,1,3,3,2,3,2]))