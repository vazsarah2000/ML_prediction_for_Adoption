import pyautogui
import time

def save():
    pyautogui.hotkey('ctrl', 's')
    # Wait for the Save As dialog to load. Might need to increase the wait time on slower machines
    time.sleep(1)
    # File path + name
    FILE_NAME ='C:\\Users\\Sara\\PycharmProjects\\Adoption_survey\\templates'
    # Type the file path and name is Save AS dialog
    pyautogui.typewrite(FILE_NAME+'\\'+'data.html')
    pyautogui.click(1698,984)       #cursor position of 'Save' button
    pyautogui.press('left')         # default would be NO , so press left arrow and YES is selected
    pyautogui.press('enter')
    #Hit Enter to save
    #pyautogui.press('enter')