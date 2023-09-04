
def solution(people):
    #사이즈 표를 담은 리스트
    sizes = [120, 105, 100, 95]
    # 결과를 저장할 리스트
    result = [0, 0, 0, 0]
    # people 리스트를 순차적으로 순회하여 각 사람마다 사이즈의 어떤 인댁스에 속하는지 구별
    for item in people:
        for index, value in enumerate(sizes):
            if item < value:
                flag = index
        #사이즈표의 인댁스와 결과 리스트의 인댁스를 일치시켜서 횟수를 저장
        result[flag] += 1
        # 횟수를 저장하면서 사이즈의 순서가 거꾸로 되어있었기 때문에 반환할때 뒤집어서 반환
    return result[::-1]

print(solution([97, 102, 93, 100, 107]))
                
                