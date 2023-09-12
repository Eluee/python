# n = int(input())
# arr = list(map(int, input().split()))
com = list(map(int, input().split()))

glo_arr = []

four_arti = ['+','-','*','/']

com_sample = [ four_arti[i] for i in range(4) for _ in range(com[i]) ]

test = [[four_arti[index] for _ in range(value)]for index, value in enumerate(com)]

def combination(arr, com_number):
    global com_sample
    global glo_arr
    if len(arr) == com_number:
        glo_arr.append((com_sample[i] for i in arr))
        return
    for i in range(com_number):
        if i not in arr:
            cp_arr = arr.copy()
            cp_arr.append(i)
            combination(cp_arr, com_number)




#combination([], sum(com))

# for item in glo_arr:
#     print(item)

print(len(set(glo_arr)))
print(test)
    