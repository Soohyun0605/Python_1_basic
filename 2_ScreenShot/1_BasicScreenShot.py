from PIL import Image
import pyautogui as pag
import time

time.sleep(2)

filepath='C:\\Users\\visioncoding1\\Desktop\\Soohyun Song\\2_ScreenShot\\images'

for i in range(1, 4):
    curr_time=time.strftime("_%Y%m%d_%H%M%S")
    pag.screenshot(f"{filepath}/image{curr_time}.png")