

# 문자열 : 리스트랑 동일
# 리스트 : 변경이 가능하다. - 검색이 느림
# 튜플 특징: 변경이 불가능 - 검색이 빠름

# 세트 (집합) - 중복을 허용하지 않음, 헤시함수를 사용하기 때문에 검색이빠름
# 딕셔너리 (키 : 값) - 검색이 빨라.




def solution(para):
    arr = [para.count(item) for item in list(set(para))]
    return max(arr) // min(arr)

print(solution([1,2,3,3,1,3,3,2,3,2]))
