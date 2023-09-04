
n, m = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

def combination(text, n, depth, len):
    if len >= depth:
        print(text)
        return
    else:
        for i in range(1, n+1):
            if str(i) not in text:
                text += ' ' + str(i)
                combination(text, n, depth, len+1)


for i in range(1, n+1):
    text = ""
    text += str(i)
    combination(text, n, m, 1)
    
