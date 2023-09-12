import pyautogui
import time

time.sleep(3)
current_mouse_x, current_mouse_y = pyautogui.position()

# x, y 좌표 출력
print(f"현재 마우스 위치: X={current_mouse_x}, Y={current_mouse_y}")
print(pyautogui.position())