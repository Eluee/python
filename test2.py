items = {"커피음료": 7, "펜": 3, "종이컵": 2, "우유": 1, "콜라": 4, "책": 5}

menu = input("메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료")

if menu == "1":
  name = input("물건의 이름을 입력하시오: ")
  print("재고 : ", items[name])

elif menu == "2":
  name = input("[입고] 물건의 이름과 수량을 입력하시오: ").split()
  su = items.get(name[0]) + int(name[1])
  items[name[0]] = su
  print(name[0],"의 재고 : ", su)

elif menu == "3":
  name = input("[출고] 물건의 이름과 수량을 입력하시오: ").split()
  su = items.get(name[0]) - int(name[1])
  items[name[0]] = su
  print( name[0] ,"의 재고 : ", su)

else:
  print("프로그램을 종료합니다.")



