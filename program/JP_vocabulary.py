import tkinter as tk


question = "단어가 나오는 공간입니다."
result = "이전 문제의 정답여부를 표시해주는 창입니다."
answer = ["","",""]

word = ""

def button_click():
    print("test")


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
label = tk.Label(root, text=question, font=("Arial", 14))
label.grid(row=1, column=1, columnspan=3, padx=10, pady=70)

result_label = tk.Label(root, text=result, font=("Arial", 10))
result_label.grid(row=3, column=1, columnspan=3, padx=10, pady=10)
# 창의 크기 조정
root.resizable(True, True)

root.mainloop()
