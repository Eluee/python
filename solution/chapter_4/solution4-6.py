
def solution(password):
    password = list(map(ord, password))
    if len([char for char in password if 65 <= char and char <= 90 ]) < 1:
        return False
    elif len([char for char in password if 97 <= char and char <= 122 ]) < 4:
        return False
    elif len([char for char in password if 48 <= char and char <= 57 ]) < 3:
        return False
    return True


print(solution("helloworld"))
print(solution("Hello123"))