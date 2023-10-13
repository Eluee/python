# bj1644번 문제
import math

N = int(input())
none_prime_list = [ True for _ in range(N + 1)]

def check_prime(num):
    global N, none_prime_list, prime_list
    none_prime_list[0] = none_prime_list[1] = False
    num_sqrt = int(math.sqrt(num))
    for i in range(2, num_sqrt + 1):
        if none_prime_list[i] == True:
            j = 2
            while(i*j <= N):
                none_prime_list[i * j] = False
                j += 1
                
def combo_count():
    global N, prime_list
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
prime_list = [i for i in range(2, N + 1) if none_prime_list[i]]
print(combo_count())
