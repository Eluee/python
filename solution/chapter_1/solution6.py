def solution(number):
    total = 0 
    list369 = ['3' ,'6' ,'9']
    for n in range(1,number + 1):
        for item in list369: total += str(n).count(item)
    return total


for i in range(100): print(solution(i),"=(", i,")", end="\n")