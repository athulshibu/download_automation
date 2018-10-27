import pyautogui
import sys
import time

print("Assuming 1 eisode has been put to download!!!")
c = int(input("\nEnter Number of URL's to be opened: "))
if c>6 :
    c=6
    print("Maximum is 6, so 6 it is!!!")
pyautogui.hotkey('ctrl','win','left')
time.sleep(0.2)

for x in range(c):
    try:
        pyautogui.moveTo(167,0)
        pyautogui.click() ###Top of the Tab
        pyautogui.moveTo(820,893)
        pyautogui.click() ### Episodes
        time.sleep(0.2)
        pyautogui.moveTo(820,689)
        pyautogui.click() ###Choose Episode
        time.sleep(2)
        ###
        pyautogui.moveTo(560,899)
        pyautogui.click() ###Downloader
        time.sleep(0.2)
        pyautogui.moveTo(547,821)
        pyautogui.click()### Choose Downloader
        time.sleep(2)
        ###
        pyautogui.moveTo(1146,906)
        pyautogui.click()### Quality
        time.sleep(0.2)
        pyautogui.moveTo(1136,851)
        pyautogui.click()### Choose Quality
        time.sleep(6)
        ###
        pyautogui.moveTo(1379,838)
        pyautogui.click()### Click Download
        pyautogui.moveTo(413,0)
        pyautogui.dragTo(1588,0,1,button='left')###Drag
        time.sleep(6)
        pyautogui.moveTo(1420,1007)
        pyautogui.click() ### Click Download
    except KeyboardInterrupt:
        break

pyautogui.hotkey('ctrl','win','right')
print("All Cool!!!")
input()
pyautogui.hotkey('ctrl','win','left')

