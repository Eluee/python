def solution(start_month, start_day, end_month, end_day):
   return func_a(end_month, end_day) - func_a(start_month, start_day)

def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for index in range(month - 1):
        total += month_list[index]
    total += day - 1
    return total

print(solution(1, 2, 2, 2))