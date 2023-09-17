com = list(map(int, input().split()))

four_arti = ['+','-','*','/']

arti_list = [[four_arti[index] for _ in range(value)]for index, value in enumerate(com)]




print(arti_list.sort())