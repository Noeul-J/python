# pip install pyautogui
import pyautogui
import time

# 1. 화면 크기 출력
print(pyautogui.size())

# 2. 마우스 위치 출력
time.sleep(2)
print(pyautogui.position())

# 3. 마우스 이동
pyautogui.moveTo(633, 858, 2)
time.sleep(0.5)

# 4. 마우스 클릭
pyautogui.click()
# pyautogui.click(button='right')
# pyautogui.doubleClick()
# pyautogui.click(click=3, interval=1) # 1초 텀으로 3번 클릭

# 5. 마우스 드래그
pyautogui.moveTo(816, 81, 2)
pyautogui.dragTo(539, 80, 2)

# 6. 마우스 정보
pyautogui.mouseInfo()