maps = []



max_set = set()

def printmap( myset ):
    global maps
    cp_maps = maps.copy()
    for coordinate in list(myset):
        cp_maps[coordinate[0]][coordinate[1]] = -1 
    print("===================")
    for row in cp_maps:
        print(row)
    print("===================")

def find(x, y, duplicate, set):
    global max_set, map_size
    if(0 > x or x > map_size[1] or 0 > y or  y > map_size[0]): return
    cp_set = set.copy()
    if (y, x) in cp_set:
        duplicate += 1
        if duplicate >= 2:
            return
    elif len(cp_set) >= 4:
        printmap(cp_set)
        return
    else:
        cp_set.add((y, x))

    find(x + 1, y, duplicate, cp_set)
    find(x - 1, y, duplicate, cp_set) 
    find(x, y + 1, duplicate, cp_set) 
    find(x, y - 1, duplicate, cp_set)     
    

map_size = list(map(int, input().split()))

for i in range(map_size[0]):
    maps.append(list(map(int, input().split())))

myset = set()

find(0, 0, 0, myset)
