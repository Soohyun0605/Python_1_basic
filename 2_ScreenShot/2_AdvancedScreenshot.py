from PIL import Image
import pyautogui as pag
import time
import keyboard



filepath='C:\\Users\\visioncoding1\\Desktop\\Soohyun Song\\2_ScreenShot\\images'

running=True
while running:
    if keyboard.is_pressed("ctrl"):
        curr_time=time.strftime("_%Y%m%d_%H%M%S")
        pag.screenshot(f"{filepath}/image{curr_time}.png")
    elif keyboard.is_pressed("esc"):
        running=False