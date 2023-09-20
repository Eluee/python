
def check_prime_number(number):
    for i in range(2, (number // 2) + 1):
        if number % i == 0:
            return False
    return True

def recursion(number, depth):
    global N, sample
    if depth == N:
        print(number)
        return
    
    for i in sample:
        number_cp = int(number + i)
        if check_prime_number(number_cp):
            recursion(str(number_cp), depth+1)

N = int(input())
sample = [str(i) for i in range(1,10)]
for i in ['2', '3', '5', '7']: recursion(i, 1)