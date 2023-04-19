import pytesseract
import cv2
import win32gui, win32ui, win32con, win32api
import time
import keyboard
import numpy as np
import mss

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

### ------ Global var ------ ###
x, y = 0, 0
w, h = 1280, 960
color_yellow = (0, 255, 255)
### ------------------------ ###


def pause():
    print('pause, press E to continue')
    while not keyboard.is_pressed('e'):
        time.sleep(0.01)

def getWindowCoord():
    # hwnd = win32gui.FindWindow(None, r'World of Warcraft') # any desired window name by default
    hwnd = win32gui.GetForegroundWindow()  # coords of active window
    # win32gui.SetForegroundWindow(hwnd)
    dimensions = win32gui.GetWindowRect(hwnd)
    bbox = (dimensions[0], dimensions[1], dimensions[2], dimensions[3])
    return bbox

while (True):
    time.sleep(2)

    bbox = getWindowCoord()
    image = np.array(mss.mss().grab(bbox), np.uint8)
    # image[210:230, 350:440] = (0, 0, 0)
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # ret, threshold1 = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    text = pytesseract.image_to_string(image)
    cv2.putText(image, text, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color_yellow, 2)
    #cv2.imshow('result', cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    cv2.imshow('result', image)
    print(text)
    with open("readFromScreen.txt", "w", encoding="utf-8") as text_file: #"a"
        text_file.write(text + "\n")
    # cv2.imshow('result', threshold1)
    if (cv2.waitKey(25) & 0xFF == ord('q')):
        cv2.destroyAllWindows()
        break;