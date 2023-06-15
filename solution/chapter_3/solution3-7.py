

# 만약 주어진 모든 과일로 주스를 만들었을 때 남는과일의 종류 상관없이 0개라면 무조건 사과를 토끼에게 주는게 우선이다.
# 만약 토끼에게 줘야하는 과일의 갯수가 3개 이상이라면 예를 들어 4개 를 줘야한다면 사과 사과 사과 당근 순서대로 빼줘야한다.

# 먼저 주어진 과일 수에서 토끼의 먹이를 먼저 뺀다. 순서는 사과 사과 사과 당근 순으로 빼주는데 먼저 주어진 과일로 만들 수 있는
# 최대 주스를 만들고 남은 종류와 상관없이 과일이 있다면 토끼 먹이에서 먼저 빼준다
# 남은 과일의 갯수 가 토끼에게 줄 먹이보다 크다면 처음에 만든 최대 주스 갯수를 반환
# 아니라면 먹이 갯수 - 남은 과일 갯수 의 결과값을 

def solution(num_apple, num_carrot, k):
    max_juice = num_apple // 3 if num_apple // 3 < num_carrot else num_carrot
    remain_fruit = (num_apple % (max_juice * 3)) + (num_carrot - max_juice)  
    if remain_fruit < k:
      k = k - remain_fruit
      max_juice -= k // 4
      max_juice -=  1 if k % 4 > 0 else 1 
    return max_juice 

print(solution(10, 5, 4))


# 당근 사과 사과 사과 당근 사과 사과 사과 . 
    