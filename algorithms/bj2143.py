T = int(input())
N = int(input())
list_N = list(map(int, input().split()))
M = int(input())
list_M = list(map(int, input().split()))

def prime_list(number_list, len):
    global T
    prime = []
    def sum_list(i):
        for j in range(i, len):
            total_sum = sum(number_list[i:j + 1])      

            prime.append(total_sum)

    for i in range(len): sum_list(i)
    return prime

def binary_search(prime_list_N, prime_list_M):
    global T
    counter = 0
    if len(prime_list_N) > len(prime_list_M):
        list_A = sorted(prime_list_N)
        list_B = prime_list_M
    else:
        list_A = sorted(prime_list_M)
        list_B = prime_list_N

    list_A_len = len(list_A) - 1
    for item in list_B:
        item = T - item 
        left = 0
        right = list_A_len
        while(left < right):
            mid = (left + right) // 2
            if list_A[mid] < item:
                left = mid + 1
            elif list_A[mid] > item:
                right = mid - 1
            else:
                right = mid
        start_index = left = right
        right = list_A_len

        while(left < right):
            mid = (left + right) // 2 + 1
            if list_A[mid] < item:
                left = mid + 1
            elif list_A[mid] > item:
                right = mid - 1
            else:
                left = mid
        end_index = left
        
        if list_A[start_index] == item: 
            counter += abs(start_index - (end_index + 1))
    
    return counter

print(binary_search(prime_list(list_N, N),prime_list(list_M, M)))
