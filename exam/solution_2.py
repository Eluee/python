def solution(day, numbers):
    return len([number for number in numbers if day%2 == number%2])

print(solution(17,[3285, 1724, 4438, 2988, 3131, 2998]))