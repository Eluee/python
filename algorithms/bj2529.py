
k = int(input())
ineq_symbols = list(input().split())

result = []


# 수의 조합을 찾는 함수
def solution(number_list, depth):
    global k
    global ineq_symbols
    global result
    if k + 1 == depth:
        result.append(number_list)
        return
    for number in range(10):
        if number not in number_list:
            if len(number_list) == 0:
                number_list_cp = number_list.copy()
                number_list_cp.append(number)
                solution(number_list_cp, depth + 1)
            else:
                if ineq_symbols[len(number_list) - 1] == '<':
                    if number_list[len(number_list) - 1] < number:
                        number_list_cp = number_list.copy()
                        number_list_cp.append(number)
                        solution(number_list_cp, depth + 1)
                else:
                    if number_list[len(number_list) - 1] > number:
                        number_list_cp = number_list.copy()
                        number_list_cp.append(number)
                        solution(number_list_cp, depth + 1)
                
solution([], 0)
print("".join(map(str, result[len(result) - 1])))
print("".join(map(str, result[0])))
