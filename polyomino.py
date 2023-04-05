map = [1, 2,3,4,5,6,7,8,9,10]
arr = []
result = []

def find(index, list):
    global map, result
    cp_result = list.copy()
    if map[index] in list: return 

    elif len(list) >= 4: 
        print(cp_result)
        return
 
    else:
       
        cp_result.append(map[index])

    find(index + 1, cp_result)
    find(index - 1, cp_result)


find(4, arr)

