
def solution(money, price, n):
    empty = money // price
    juice = empty
    while empty // n != 0:
        juice += empty//n
        empty = empty%n +empty//n

    return juice

print(solution(8,2,4))
print(solution(6,2,2))