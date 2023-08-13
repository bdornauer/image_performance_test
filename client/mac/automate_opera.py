import pyautogui
import keyboard

class OperaAutomation:

    def __init__(self):
        print("calling __init__() constructor...")

    def open_browser(self):
        pyautogui.sleep(2)
        pyautogui.hotkey('command', 'shift')
        pyautogui.hotkey('command', 'space')
        pyautogui.sleep(1)
        pyautogui.typewrite('terminal')
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(1)
        keyboard.write('open -na "Opera" --args --incognito')
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(10)

    def open_website(self):
        keyboard.write('http://192.168.1.145:8080/')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(10)

    def close_browser(self):
        pyautogui.hotkey('command', 'w')
        pyautogui.sleep(10)

    def complet_run(self):
        self.open_browser()
        self.open_website()
        self.close_browser()