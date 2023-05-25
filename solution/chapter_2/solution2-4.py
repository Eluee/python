
def solution(arr):
    text = ''
    for item in arr: 
        if len(item) >= 5:
            text += item
    return text
print(solution(["my", "favorite", "color", "is", "violet"]))

