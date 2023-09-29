
number_list = [ int(input()) for _ in range(10)]

print(len({i%42 for i in number_list }))
