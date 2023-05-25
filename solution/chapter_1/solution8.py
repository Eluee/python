
def solution(sentence):
    sentence = sentence.replace(" ","")
    sentence = sentence.replace(".","")
    i = 0
    j = len(sentence) - 1
    while(i < j):
        if sentence[i] != sentence[j]:
           return False
        i += 1
        j -= 1
    return True



print(solution("never odd or even."))