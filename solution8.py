
def solution(sentence):
    flag = True
    sentence = sentence.replace(" ","")
    sentence = sentence.replace(".","")
    i = 0
    j = len(sentence) - 1
    while(i < j):
        if sentence[i] != sentence[j]:
            flag = False
            break
        i += 1
        j -= 1
    return flag



print(solution("never odd or even."))