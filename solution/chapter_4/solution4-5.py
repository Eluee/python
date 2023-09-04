
def solution(money, price, n):
    # 처음 빈병의 갯수는 돈을 가격으로 나는 몫이 됨
    empty = money // price
    # 빈병의 갯수는 곧 주스를 마신 횟수 임.
    juice = empty
    # 주스를 마시고 나면 남은 병으로 다시 주스를 살 수 있는지 판단
    while empty // n != 0:
        # 나머지 병으로 주스를 마실 수 있다면 다시 빈병을 n으로 나눈 값을 총 마신 횟수에 더하기
        juice += empty//n
        # 빈병으로 산 주스를 마시고 남은 빈병을 다시 나머지 빈병에 추가 후 남은 병으로 다시 살 수 없을 때 까지 반복
        empty = empty%n +empty//n

    return juice

print(solution(8,2,4))
print(solution(6,2,2))