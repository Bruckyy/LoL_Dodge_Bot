from pyautogui import *
import pyautogui
from time import sleep
import keyboard
import win32api, win32con
from datetime import datetime

sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

i=0
while keyboard.is_pressed('q')==False and i<13:
    if pyautogui.locateOnScreen('find.png',confidence=0.8) !=None:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('find.png',confidence=0.8))
        x, y = pyautogui.position()
        click(x,y)


    if pyautogui.locateOnScreen('accept.png',confidence=0.8) !=None:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('accept.png',confidence=0.8))
        x, y = pyautogui.position()
        click(x,y)


    if pyautogui.locateOnScreen('ok.png',confidence=0.8) !=None:
        pyautogui.moveTo(pyautogui.locateCenterOnScreen('ok.png',confidence=0.8))
        x, y = pyautogui.position()
        click(x,y)
        i+=1
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")       
        print("Dodge n°"+str(i)+" Current time: "+ current_time)
        
