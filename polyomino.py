map = [1, 3, 9, 1, 5, 10, 1, 1, 1]
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