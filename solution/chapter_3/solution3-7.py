def solution(num_apple, num_carrot, k):
    #주어진 과일로 만들 수 있는 최대 주스 갯수
    max_juice = num_apple // 3 if num_apple // 3 < num_carrot else num_carrot
    #주스를 최대로 만들고 남은 과일 수
    remain_fruit = (num_apple - (max_juice * 3)) + (num_carrot - max_juice)  
    if remain_fruit < k and 0 < remain_fruit :
      # 먹이의 갯수가 남는 과일 수보다 더 많을 때 
      k = k - remain_fruit
      max_juice -= k // 4
      max_juice -= 1 if k % 4 > 0 else 0 
    return  0 if max_juice < 0 else max_juice

print(solution(300, 10, 40))
    