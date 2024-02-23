import pyautogui
import time
from PIL import Image
import pyscreenshot as ImageGrab
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd =r"C:\Users\thepe\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
time.sleep(5)
while True:
    region_screenshot = ImageGrab.grab(bbox=(119, 458, 1671, 546))
    region_screenshot.save('region_screenshot.png')
    img2 = np.array(Image.open("region_screenshot.png"))
    text = pytesseract.image_to_string(img2)
    pyautogui.write(text, interval=0.017)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.click(x=322, y=257)
    time.sleep(1)
