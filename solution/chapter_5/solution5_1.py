



def solution(ladders, win):
   for i in range(1, 7):
        temp = i
        for brige_index in range(len(ladders)):
            if ladders[brige_index][0] == temp:
                temp = ladders[brige_index][1]
                continue
            if ladders[brige_index][1] == temp:
                temp = ladders[brige_index][0]
                continue
        if temp == win:
            return i


   

print(solution([[1, 2], [3, 4], [2, 3], [4, 5], [5, 6]], 3))
print()