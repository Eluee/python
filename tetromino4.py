map_size = list(map(int, input().split()))
maps = []

def find(x, y, duple, set):
    if 0 <= x and x < map_size[0] and 0 <= y and y < map_size[1]:
        if {{x, y}} in set:
            duple += 1
        else:
            set.add({x, y})
        if 2 < duple or set.len() > 4:
            

    else: return

for i in range(map_size[0]):
    maps.append(list(map(int, input().split())))

print(maps)