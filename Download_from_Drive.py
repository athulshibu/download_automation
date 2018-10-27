import pyautogui
import sys
import time


print("Assuming the folder has been opened and downloaded episodes deleted or untouched!!!")
c = int(input("\nEnter Number of Episodes to be Downloaded: "))
pyautogui.hotkey('ctrl','win','left')
time.sleep(0.2)

for x in range(c):
    try:
        pyautogui.moveTo(386,14)
        pyautogui.hotkey('shift','f10')
        for i in range(11):
            pyautogui.press('down')
        pyautogui.press('enter')
        if x!=c-1 :
            time.sleep(12)
            pyautogui.press('right')
    except KeyboardInterrupt:
        break
pyautogui.hotkey('ctrl','win','right')
print("All Cool!!!")
input()
pyautogui.hotkey('ctrl','win','left')
time.sleep(0.2)
