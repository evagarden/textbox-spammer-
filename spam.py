import pyautogui, time

time.sleep(8)
file = open("wordlist.txt", 'r')
for word in file:
    pyautogui.typewrite(word)
    pyautogui.press("enter")