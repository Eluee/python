import tkinter as tk
import JPV_account
import random


#내 단어장
vocabulary = []
#문제
question = "단어가 나오는 공간입니다."
# 이전문제의 결과 변수
result = ""
#선택지
choice = ["","",""]

answer = ""

def button_click():
    if result == "":
        init_Page()
        set_problem()
    else:
        set_problem()
       
 

def init_Page():
    '''
    페이지 초기화
    '''
    global vocabulary
    # 내 단어장 가져오기
    my_voca = JPV_account.read_my_voca()
    vocabulary = my_voca["vocabulary"]

def next():
    '''
    다음 문제 함수
    '''


def set_problem():
    '''
    문제를 설정하는 함수
    '''
    global vocabulary
    global answer
    global question
    global choice

    global button
    global label
    #문제 선택

    idx = random.randint(0,len(vocabulary) - 1)
    if vocabulary[idx]["Kanji"] != "None":
        #한자가 있는 단어
        question = vocabulary[idx]["Kanji"]
        print(idx)
        answer = vocabulary[idx]["Onyomi"]
        choice[0] = answer + "\n" + vocabulary[idx]["mean"]
        
        #객관식의 중복을 막기위한 코드
        for i in range(1,3):
            choice_idx = random.randint(0,len(vocabulary) - 1)
            while idx == choice_idx or vocabulary[choice_idx]["Onyomi"] + "\n" + vocabulary[choice_idx]["mean"] in choice:
                choice_idx = random.randint(0,len(vocabulary) - 1)
            choice[i] = vocabulary[choice_idx]["Onyomi"] + "\n" + vocabulary[choice_idx]["mean"]

    else:
        #한자가 없는 단어
        question = vocabulary[idx]["Onyomi"]
        answer = vocabulary[idx]["mean"]
        choice[0] = answer
        for i in range(1,3):
            choice_idx = random.randint(0,len(vocabulary) - 1)
            #객관식의 중복을 막기위한 코드
            while idx == choice_idx or vocabulary[choice_idx]["mean"] in choice:
                choice_idx = random.randint(0,len(vocabulary) - 1)
            choice[i] = vocabulary[choice_idx]["mean"]
    
    # UI 문제 표시
    print("문제: ",question ,"정답: ", answer, "선택지: ",choice)
    label.config(text=question)
    random.shuffle(choice)
    for i, item in enumerate(choice):
        button[i].config(text=item)

   


root = tk.Tk()

# 창의 크기 설정
root.geometry("510x300")

# 창의 제목 설정
root.title("일본어 단어 암기 프로그램 - made by Aya")

# 창을 중앙에 배치
window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry("+{}+{}".format(position_right, position_down))
button_color = "#A8C8F9"

button = []
for i in range(3):
    button.append(tk.Button(root, text="단어 암기를 시작합니다.", command=button_click, width=20, height=3, bg=button_color))
    button[i].grid(row=2, column=i+1, padx=10, pady=10)


# 레이블
label = tk.Label(root, text=question, font=("Arial", 20))
label.grid(row=1, column=1, columnspan=3, padx=10, pady=70)

result_label = tk.Label(root, text=result, font=("Arial", 10))
result_label.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
# 창의 크기 조정
root.resizable(True, True)

root.mainloop()
