# bj1644번 문제
import math

N = int(input())
none_prime_list = [ True for _ in range(N + 1)]

def check_prime(num):
    global N, none_prime_list, prime_list
    # 0과 1은 소수가 아니기 때문에 False처리
    none_prime_list[0] = none_prime_list[1] = False
    num_sqrt = int(math.sqrt(num))
    # 2부터 소수의 시작이므로 시작은 i의 범위가 num의 제곱근을 벗어나지 않기 때문에 num의 제곱근을 사용
    # range함수는 두번째 매개변수의 바로 전까지만 처리를 하기 때문에 + 1
    # num_sqrt에 1을 안더해주면 36을 넣었을때 6 * 6의 경우의 수가 나오지 않음
    for i in range(2, num_sqrt + 1):
        if none_prime_list[i] == True:
            # j가 1이 아닌 2부터 시작하는 이유는 현제 True인 숫자는 소수이기 때문에 건너뛰고 수정한다.
            j = 2
            while(i*j <= N):
                # i의 배수들은 모두 소수가 아니기 때문에 False로 수정
                none_prime_list[i * j] = False
                j += 1
                
def combo_count():
    global N, prime_list
    # 투포인터 방식의 탐색
    # 여기서 prime_list는 이미 정렬이 되어있기 때문에 추가적인 정렬을 하지 않음
    start = end = 0
    count = 0
    sum_prime = 0
    while True:
        if sum_prime <= N:
            if sum_prime == N:
                count += 1
            
            if end == len(prime_list):
                break
            
            sum_prime += prime_list[end]
            end += 1
        else:
            sum_prime -= prime_list[start]
            start += 1
    
    return count
            
        
check_prime(N)
# none_prime_list를 순회하면서 True인 경우만 prime 리스트에 인댁스추가 (True인 경우가 곧 소수)
prime_list = [i for i in range(2, N + 1) if none_prime_list[i]]
print(combo_count())
