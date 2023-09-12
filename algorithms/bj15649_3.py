
n, m = map(int, input().split())
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

glo_arr = []

def combination(text, n, depth, len):
    global glo_arr
    if len >= depth:
        glo_arr.append(text.strip())
        print(text.strip())
        return
    else:
        for i in range(n):
            if str(i) not in text:
                cp_text = text
                cp_text += ' ' + str(i)
                combination(cp_text, n, depth, len+1)


for i in range(n):
    text = ""
    text += str(i)
    combination(text, n, m, 1)

print(len(glo_arr))
