
total = 0

def solution(arr):
    am_arr = arr
    global total
    for i in am_arr:
        if type(i) != list:
            total += 1
        else:
           solution(i)
    return

solution([1, 2, 3,[1, 3, 5,[233, 3,4,3,1,2],[3,5], 2]])
print(total)