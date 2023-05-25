

def find(x, y, duple, set):
    if 0 <= x and x < map_size[0] and 0 <= y and y < map_size[1]:
        if (x, y) in set:
            duple += 1
        else:
            cp_set = set.copy()
            cp_set.add((x, y))

        if 2 < duple or len(set) > 4:
            for item in cp_set:
                print(item)
            return
        
        find(x + 1, y, duple, cp_set)
        find(x - 1, y, duple, cp_set)
        find(x, y + 1, duple, cp_set)
        find(x, y - 1, duple, cp_set)
    else: return

# for i in range(map_size[0]):
#     maps.append(list(map(int, input().split())))
map_size = list(map(int, input().split()))
maps = []
set = set()
find(20, 20, 0, set)