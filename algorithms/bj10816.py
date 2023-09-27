N = int(input())
list_N = list(map(int,input().split()))

M = int(input())

list_M = list(map(int,input().split()))
dict_M = dict.fromkeys(list_M, 0)

for number in list_N: 
    try:
        dict_M[number] += 1
    except:
        continue
    
print(*[dict_M[key] for key in list_M])
