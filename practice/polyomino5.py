map_size = list(map(int, input().split()))

maps = [] 

maxnumber = 0
height_coordinate = []

def find_height_number():
    global maps
    maxNumber = 0
    for item in maps:
        tmp = max(item)
        print(tmp)
        if maxNumber < tmp:
            maxNumber = tmp
    
    return maxNumber

def find_coordinate( Mnumber ):
    global maps, map_size, height_coordinate
    for col in range(map_size[0]):
        for row in range(map_size[1]):
            if maps[col][row] == Mnumber:
                height_coordinate.append([(col, row)])
    
            
            

for i in range(map_size[0]):
    maps.append(list(map(int, input().split())))

find_coordinate(find_height_number())
print(height_coordinate)