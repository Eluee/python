maps = []
max_set = set()
resort = 0

def compare( set ):
    global resort, map_size, maps
    total = 0
    for index in tuple(set):
        #print(index[0] , " &" , index[1])
        total += maps[index[0]][index[1]]

    if total >= resort: resort = total


def find(x, y, duplicate, set):
    global max_set, map_size
    if(0 > x or x >= map_size[1] or 0 > y or  y >= map_size[0]): return
    cp_set = set.copy()
    if (y, x) in cp_set:
        duplicate += 1
        if duplicate >= 2:
            return
    elif len(cp_set) >= 4:
        #print(cp_set)
        compare(cp_set)
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

for y in range(map_size[0]):
    for x in range(map_size[1]):
        find(x, y, 0, myset)

print(resort)