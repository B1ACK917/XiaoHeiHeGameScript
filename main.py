import pyautogui
import cv2
import numpy as np
import time
import win32api
import win32con


WhiteMat = np.zeros((1, 1, 3))
WhiteMat[0, 0, :] = 255
GrayMat = np.zeros((1, 1, 3))
GrayMat[0, 0, :] = (192, 192, 176)
Flag = 0


def check_toward():
    img = pyautogui.screenshot(region=[675, 129, 570, 900])  # x,y,w,h
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    print((img[490, 105, :] == GrayMat).all())
    if (img[490, 105, :] == GrayMat).all():
        return 2
    else:
        return 1


def check_start():
    img = pyautogui.screenshot(region=[675, 129, 570, 900])
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    return (img[200, 165, :] == WhiteMat).all()


def mouse_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def run(_max):
    time.sleep(3)
    while check_start():
        continue
    time.sleep(3)
    for i in range(_max):
        if check_toward() == 1:
            mouse_click(850, 930)
        else:
            mouse_click(1050, 930)
        time.sleep(0.1)


if __name__ == '__main__':
    run(1000)
