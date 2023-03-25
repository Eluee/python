total = 0
len = int(input())  # 길이 입력
brackets = input()  # 문자열 입력

for i in range(len):
    if brackets[i] == '(':
        total += 1  # 여는 괄호
    else:
        total -= 1  # 닫는 괄호

    if (total < 0):  # 닫는괄호가 먼저 나올경우
        break

# 결과 출력
if total == 0:
    print("올바른 괄호 입니다.")
else:
    print("잘못된 괄호입니다.")
