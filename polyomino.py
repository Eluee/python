
# 5를 포함하고 있는 4길이의 연속된 수열을 모두 출력

arr = []
result = []

def find(index, a):
    d = a.copy()
    d.append(index)
    global result
    
    right = left = index
    while right in d:
        right += 1
        
    while left in d:
        left -= 1

    if len(d) >= 4:
        d.sort()
        print(d in result)
        if d in result:
            return
        else:
            result.append(d)
            
    else:
        find(right, d)
        find(left, d)


arr.append(5)
find(5 + 1, arr)
find(5 - 1, arr)
for i in result:
    print(i)