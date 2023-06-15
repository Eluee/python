

def solution(shirt_size):
    size = [ "XS", "S", "M", "L", "XL", "XXL"]
    size_result = []
    for sizes in size : size_result.append(shirt_size.count(sizes))
    return size_result

input_list = ["XS", "S", "L", "L", "XL", "S"]

print(solution(input_list))

