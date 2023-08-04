import pyautogui
class EdgeAutomation:

    def __init__(self):
        print("calling __init__() constructor...")

    def open_browser(self):
        pyautogui.sleep(5)
        pyautogui.hotkey('win', 'r')
        pyautogui.typewrite('msedge.exe --inprivate')
        pyautogui.press('enter')
        pyautogui.sleep(5)

    def open_inspector(self):
        pyautogui.hotkey('ctrl', 'shift', 'i')
        pyautogui.sleep(2)

    def disable_cache(self):
        pyautogui.click((396, 726))  # open network
        pyautogui.sleep(2)
        pyautogui.click((371, 762))
        pyautogui.sleep(2)

    def open_website(self):
        pyautogui.click((350, 76))
        pyautogui.typewrite('http://192.168.1.145:8080/')
        pyautogui.sleep(2)
        pyautogui.press('enter')
        pyautogui.sleep(10)

    def close_browser(self):
        pyautogui.hotkey('alt', 'f4')
        pyautogui.sleep(10)

    def complet_run(self):
        self.open_browser()
        self.open_website()
        self.close_browser()