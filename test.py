

# 문자열 : 리스트랑 동일
# 리스트 : 변경이 가능하다. - 검색이 느림
# 튜플 특징: 변경이 불가능 - 검색이 빠름

# 세트 (집합) - 중복을 허용하지 않음, 헤시함수를 사용하기 때문에 검색이빠름
# 딕셔너리 (키 : 값) - 검색이 빨라.


arr = [x for x in range(10)]
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

arr2 = [x for x in range(10) if x%2 == 0]

arr3 = [x if x%2 == 0 else 'odd' for x in range(10)]

arr4 = [(x, y) for x in range(5) for y in range(5)]


arr5 = [a / score for a in range(10) for score in [0.3, 0.7, 1]]

print(arr5)