maps = []
max_set = set()
resort = 0

def compare( set ):
    global resort, map_size, maps
   
    for index in tuple(set):
        total = 0
        for item in index:
            total += maps[item[0]][item[1]]    
        if total >= resort: resort = total

def printmap( set ):
    global map_size
    emt_map = [[0] * map_size[1] for _ in range(map_size[0])]
    for coodinate in tuple(set):
        emt_map[coodinate[0]][coodinate[1]] += 1

    print("\n")
    for item in emt_map:
        print(item)
    print("\n")

def find(x, y, set, depth):
    global max_set, map_size
    if(0 > x or x >= map_size[1] or 0 > y or  y >= map_size[0]): return

    cp_depth = depth[:]
    cp_depth +=  "(" + str(x) + ", " + str(y) + ")"
    cp_set = set.copy()
    if (y, x) in cp_set:
        return
    elif len(cp_set) >= 4:
        print(cp_set, "depth : ", depth)
        #printmap(cp_set)
        return
    else:
        cp_set.add((y, x))

    find(x + 1, y,  cp_set, cp_depth)
    find(x - 1, y,  cp_set, cp_depth) 
    find(x, y + 1,  cp_set, cp_depth) 
    find(x, y - 1,  cp_set, cp_depth)     
    
map_size = list(map(int, input().split()))

# for i in range(map_size[0]):
#     maps.append(list(map(int, input().split())))

myset = set()

# for y in range(map_size[0]):
#     for x in range(map_size[1]):
#         find(x, y, 0, myset)
mystr = ""
find(7, 7, myset, mystr)

#compare(max_set)
#print(resort)