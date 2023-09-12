import pyautogui
import time

screen_width, screen_height = pyautogui.size()
center_x = screen_width // 2
center_y = screen_height // 2

pyautogui.moveTo(center_x, center_y, duration=2)

time.sleep(2)

x = 200
y = 200

pyautogui.moveTo(x, y, duration=2)