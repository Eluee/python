
def solution(password):
    # 각 글자의 존재 여부를 확인하기 위해 변수 3개를 0으로 초기화
    up_case = down_case = number_case = symbol_case = 0 
    # 문자열의 각 항목을 순회
    # 문자열의 길이에 따른 판단
    if len(password) > 15: return False 

    for text in password:
        #문자는 아스키 코드 값을 사용하기 때문에 각 문자에 대한 범위를 지정하여
        #해당 범위에 들어간다면 변수의 값 증가
     # 대문자 확인
        if 'A' <= text and text <= 'Z':
            up_case += 1
        # 소문자 확인
        elif 'a' <= text and text <= 'z':
            down_case += 1
        # 숫자 확인
        elif '0' <= text and text <= '9':
            number_case += 1
        elif text in ['!', '#', '$']:
            # 특수문자는 하나만 들어가야 하기 때문에 해당 특수문자의 개수를 파악
            symbol_case += 1
        else:
            #이 외의 문자는 들어가면 바로 False로 반환
            return False
    
    # 각 케이스의 존재 여부와 지정한 특수문자가 하나만 존재 하는지 확인 후 확인 되었다면 True반환
    if 0 < up_case and 1 < down_case and 1 < number_case and symbol_case == 1:
        return True
    else:
        #아니라면 False 반환
        return False
           
print(solution(input()))