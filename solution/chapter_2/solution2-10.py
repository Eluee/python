def solution(purchase):
    
    def gift(cost):
        gift_card = {
        1000000: 50000,
        600000: 30000,
        400000: 20000,
        200000: 10000
        }
        for key in list(gift_card):
            if cost // key > 0:
                return gift_card[key]


    return sum([ gift(price) for price in purchase ])


print(solution( [150000, 210000, 399990, 990000, 1000000] ))