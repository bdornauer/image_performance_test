import pyautogui


def open_browser():
    pyautogui.hotkey('win', 'r')
    pyautogui.typewrite('chrome.exe')
    pyautogui.press('enter')
    pyautogui.sleep(2)

def open_inspector():
    pyautogui.hotkey('ctrl', 'shift', 'i')
    pyautogui.sleep(2)

def disable_cache():
    pyautogui.click((396, 726))  # open network
    pyautogui.sleep(2)
    pyautogui.click((371, 762))
    pyautogui.sleep(2)


def open_website():
    pyautogui.click((198, 76))
    pyautogui.typewrite('http://192.168.1.145:8080/')
    pyautogui.sleep(2)
    pyautogui.press('enter')
    pyautogui.sleep(10)

def close_browser():
    pyautogui.hotkey('alt', 'f4')
    pyautogui.sleep(10)


if __name__ == '__main__':
    ''' Disable cache if not already happend - config. should stay 
    open_browser()
    open_inspector()
    disable_cache()
    open_website()
    close_browser()
    '''

    for i in range(0, 10):
        open_browser()
        open_inspector()
        #disable_cache()
        open_website()
        close_browser()
