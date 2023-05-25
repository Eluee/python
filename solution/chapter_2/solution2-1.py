def func_a(arr):
    return {key: arr.count(key) for key in list(set(arr))}

def solution(left_gloves, right_gloves):
    right_dict = func_a(right_gloves)
    left_dict = func_a(left_gloves)
    inter_key = set(left_dict) & set(right_dict)
    return sum([right_dict[key] if right_dict[key] < left_dict[key] else left_dict[key] for key in inter_key ])

print(solution([2, 1, 2, 2, 4],[1, 2, 2, 4, 4, 7])) 