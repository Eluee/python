
number = int(input())
number_list = list(map(int, input().split()))
com = list(map(int, input().split()))

total_com = sum(com)

max_min_list = []

def max_min(com_list):
    global max_min_list, number_list
    temp = number_list[0]
    for i in range(len(com_list)):
        if com_list[i] == 0: temp += number_list[i+1]
        elif com_list[i] == 1:temp -= number_list[i+1]
        elif com_list[i] == 2: temp *= number_list[i+1]
        else: temp = int(temp / number_list[i+1])
    max_min_list.append(temp)

def solution(com_list, com, depth):
    global total_com
    if depth == total_com:
        max_min(com_list)
        return
    
    for i in range(4): 
        com_cp = com.copy()
        com_list_cp = com_list.copy()
        if com_cp[i] > 0:
            com_cp[i] -= 1
            com_list_cp.append(i)
            solution(com_list_cp, com_cp, depth+1)


solution([],com,0)
print(max(max_min_list))
print(min(max_min_list))
