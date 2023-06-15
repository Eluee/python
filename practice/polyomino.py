map = [1, 2,3,4,5,6,7,8,9,10]
arr = []
result = []

map_size = [15, 15]

def printmap( set ):
    global map_size
    emt_map = [[0] * map_size[1] for _ in range(map_size[0])]
    for coodinate in tuple(set):
        emt_map[coodinate[0]][coodinate[1]] += 1

    emt_map[5][5] = 5
    print("\n")
    for item in emt_map:
        print(item)
    print("\n")

def find(index_x,index_y, list, depth):
    cp_result = list.copy()
    depth += 1
    print(depth," : " ,cp_result, "(", index_x,", ", index_y, ")")
    if len(cp_result) >= 4: #길이에 도달 했을때
        if (index_x, index_y) == cp_result[2]: # 되돌아가는 경우
            printmap(set(cp_result))
            return
        else:
            return #cp_result의 길이가 4개이지만 되돌아가지 않는 경우
    elif (index_x, index_y) not in cp_result: #길이에 도달하지 않았을때
        cp_result.append((index_x, index_y))
    else: return

    find(index_x + 1,index_y ,cp_result, depth)
    find(index_x - 1,index_y ,cp_result, depth)
    find(index_x,index_y + 1 ,cp_result, depth)
    find(index_x,index_y - 1 ,cp_result, depth)

find(5, 5, arr, 0)