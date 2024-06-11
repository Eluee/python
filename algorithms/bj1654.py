# K, N = map(int, input().split())
# cable_list = [int(input()) for _ in range(K)]
    

# def check_div(cable_list, length):
#     for cable in cable_list:
#         print(f"{cable % length}: cable: {cable}, length: {length}")
#         if cable % length != 0:
#             return False
#     return True 


# def recursion(cable_list, depth):
#     global K, N
#     if sum(cable_list) >= N and depth > 0:
#         print(max_len)
#     max_len = min(cable_list)
#     for length in range(max_len, 1, -1):

#         if check_div(cable_list, length):
#             print(length, max_len)
#             print(*cable_list)
#             recursion([value//length for value in cable_list], depth+1)
#             break

# recursion(cable_list, 0)