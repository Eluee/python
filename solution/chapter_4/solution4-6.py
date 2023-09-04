
def solution(password):
    #passsword를 판별하기 쉽게 ord 함수를 써서 아스키 코드 값으로 바꿔줌
    password = list(map(ord, password))
    # 아스키 코드 값의 범위를 통해서 대문자가 몇개인지 판단 후 1개 미만일 경우 False 반환
    if len([char for char in password if 65 <= char and char <= 90 ]) < 1:
        return False
    # 같은 방식으로 소문자의 범위 내에서 4개 미만 일 경우 False 반환
    elif len([char for char in password if 97 <= char and char <= 122 ]) < 4:
        return False
    # 아스키 코드 숫자 범위 내에서 3개 미만일경우 False 반환
    elif len([char for char in password if 48 <= char and char <= 57 ]) < 3:
        return False
    # 위에서 반환 되지 않았을경우 모든 조건을 충족하므로 True 반환
    return True


print(solution("helloworld"))
print(solution("Hello123"))