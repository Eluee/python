import random

door = ['염소', '염소', '자동차']  # 문 안의 정보를 담은 리스트
door_len = len(door)  # 리스트의 길이를 담은 변수


def mix():  # door리스트 섞기
    for i in range(door_len):
        rand_num = random.randint(0, door_len - 1)
        if rand_num != i:  # 선택한 문과 일치할경우 건너뜀.
            emt = door[i]
            door[i] = door[rand_num]
            door[rand_num] = emt


def unselect_door(select, open):  # 선택 되지 않은 문의 인덱스를 반환하는 함수
    for i in range(door_len):
        if i != select - 1 and i != open:
            return i


while True:
    select = int(input("3개의 문 중 하나를 선택해주세요 ex(1, 2, 3): "))
    if 1 > select or select > 3:  # 입력받은 정수의 범위가 아닐경우
        print("1 ~ 3 까지의 정수를 입력해주세요")
        continue  # 처음으로

    mix()
    for i in range(door_len):  # 염소가 들어있는 문 찾기
        if select - 1 != i and door[i] == '염소':  # 염소가 들어있는 문 하나 열어주기.
            unselect = unselect_door(select, i)
            print(i + 1, ' 번째 문은 염소입니다!',
                  unselect + 1, ' 번째 문으로 바꾸시겠습니까? (Y or N): ', end='')  # 염소가 들어있고 선택되지 않은 문을 알려줌.
            txt = input()
            if 'Y' == txt:
                print(unselect + 1, ' 번째 문은 ', door[unselect], "입니다!!")
            else:
                print(select, ' 번째 문은 ', door[select - 1], "입니다!")
