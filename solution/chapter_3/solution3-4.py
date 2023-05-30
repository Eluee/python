
def solution(words, word):
    return len([(i,j) for i in range(len(words)) for j in range(len(word)) if words[i][j] != word[j]])

print(solution( ["CODE", "COED", "CDEO"], "CODE" ))