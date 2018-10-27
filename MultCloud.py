import pyautogui
import sys
import time

print("Assuming all URL's have been Opened")
c = int(input("\nEnter Number of URL's opened: "))
pyautogui.hotkey('ctrl','win','left')
time.sleep(0.2)
pyautogui.moveTo(386,14)
pyautogui.click()

for x in range(c):
    try:
        pyautogui.press('f6')
        pyautogui.hotkey('ctrl','c')
        pyautogui.hotkey('altleft','tab')
        pyautogui.moveTo(672,392)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1028,565)
        pyautogui.click()
        pyautogui.hotkey('ctrl','v')
        time.sleep(2)
        pyautogui.moveTo(1187,668)
        pyautogui.click()
        time.sleep(3)
        pyautogui.hotkey('altleft','tab')
        pyautogui.hotkey('ctrl','tab')
    except KeyboardInterrupt:
        break

pyautogui.hotkey('ctrl','win','right')
print("All Cool!!!")
input()
pyautogui.hotkey('ctrl','win','left')
time.sleep(0.2)
pyautogui.hotkey('altleft','tab')
