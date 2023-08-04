# Automated Browser Execution
## Description
The XXXXAutomation class provides a set of methods to automate interactions with the XXX web browser using PyAutoGUI, a library for GUI automation
## Methods
### Method: open_website()
This method automates the process of navigating to a specific website in the XXX browser. It uses PyAutoGUI to click
on a specific screen coordinate (X, Y), which suggests that it interacts with a specific UI element or shortcut to
set the focus to the address bar. Then, it types the URL 'http://192.168.1.145:8080/' and presses 'Enter' to load the
website. After loading the page, it waits for 10 seconds to allow the content to load.

### Method: close_browser()
This method closes the X browser. It simulates the 'Alt + F4' keyboard shortcut to close the active
window of the browser. It waits for 10 seconds to ensure the browser closes completely.

### Method: complet_run()
This method provides a way to execute a complete automation flow. It calls the open_browser(),
open_website(), and close_browser() methods in sequence, effectively opening the browser, navigating to the specified
website, and then closing the browser.

## Requirements

Python (used 3.11.4) and `pyautogui` (used version 0.9.54)

```
pip install pyautogui
```

## Settings

In each automated browser execution, the following settings are needed to be adjusted:

- the mouse click position, to enter the URL of the website
- the executable path of the browser