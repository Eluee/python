def solution(characters):
    strlen = len(characters)
    result = ''
    for i in range(strlen):
        if i == strlen-1:
            result +=  characters[i]
        elif characters[i] != characters[i + 1]:
            result +=  characters[i]
    return result

ret = solution('senteeeencccccceeeee')
print(ret)
        
            