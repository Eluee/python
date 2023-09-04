
def solution(number):
    # number를 거꾸로 하기 위해 문자열로 형변환 후 슬라이싱뒤 정수형으로 변환
    # 정수형으로 변환한 수와 number의 차를 구하는데 음수가 나올 수 있으므로 abs함수를 통해 절대값을 구함
    return abs(number - int(str(number)[::-1])) 

print(solution(120))
print(solution(23))

