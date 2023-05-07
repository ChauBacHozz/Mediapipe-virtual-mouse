import cv2
import math
import numpy as np
import time
import HandTrackingModule   
import HumanTrackingModule
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from win32api import GetSystemMetrics
import win32api, win32con
import pyautogui
import mouse
SCREEN_WIDTH = GetSystemMetrics(0)
SCREEN_HEIGHT = GetSystemMetrics(1)
loc = {'clocx': 0,
       'clocy': 0,
       'plocx': 0,
       'plocy': 0}


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
vol_range = volume.GetVolumeRange()
min_vol = vol_range[0]
max_vol = vol_range[1]
 
frameWidth = 680
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
pTime = 0
cTime = 0
hd = HandTrackingModule.HandDetector(detectionCon=0.6)
modes = ['MouseControl', 'MouseScroll']
option = 0
option_touch = False
def mouseControl(img, loc):
    global option, option_touch
    lmList = hd.findRHandPos(img, [4, 8, 12, 16])
    option_touch = False
    if len(lmList) != 0:
        x1, y1 = lmList[0][1],lmList[0][2] 
        x2, y2 = lmList[1][1],lmList[1][2]
        x3, y3 = lmList[2][1],lmList[2][2]
        x4, y4 = lmList[3][1],lmList[3][2]
        pos_x = np.interp(x2, (200, 550), (0, SCREEN_WIDTH))
        pos_y = np.interp(y2, (100, 250), (0, SCREEN_HEIGHT))
        loc['clocx'] = int(loc['plocx'] + (pos_x - loc['plocx']) / 7)
        loc['clocy'] = int(loc['plocy'] + (pos_y - loc['plocy']) / 7)
        win32api.SetCursorPos((loc['clocx'], loc['clocy']))
        loc['plocx'], loc['plocy'] = loc['clocx'], loc['clocy']

        if math.hypot(x3 - x1, y3 - y1) < 20:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,loc['clocx'], loc['clocy'])
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

        if math.hypot(x4 - x1, y4 - y1) < 20 and option_touch == False:
            option = (option + 1) % 2
            option_touch = True
            
def mouseScroll(img):
    global option, option_touch
    lmList = hd.findRHandPos(img, [4, 6, 8, 16])
    option_touch = False
    if len(lmList) != 0:
        x1, y1 = lmList[0][1],lmList[0][2] 
        x2, y2 = lmList[1][1],lmList[1][2]
        x3, y3 = lmList[2][1],lmList[2][2]
        x4, y4 = lmList[3][1],lmList[3][2]
        if y3 > y2:
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -4, 0)
        if y3 < y2:
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 4, 0)
        if math.hypot(x4 - x1, y4 - y1) < 20 and option_touch == False:
            option = (option + 1) % 2
            option_touch = True

def menu(img):
    global option, option_touch
    lmList = hd.findRHandPos(img, [0, 13], draw=False)
    option_touch = False
    if len(lmList) != 0:
        x1, y1 = lmList[0][1],lmList[0][2] 
        x2, y2 = lmList[1][1],lmList[1][2]
        print(math.degrees(math.atan((y1 - y2)/(x1 - x2 + 0.000000000000000001))))

        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
while True:
    sucsess, img = cap.read()
    img = cv2.flip(img,1)
    # menu(img)
    if modes[option] == 'MouseControl':
        mouseControl(img, loc)
    else:
        mouseScroll(img)
    cTime = time.time()
    fps = 1 /(cTime - pTime)
    pTime = cTime
    cv2.putText(img, "FPS: " + str(int(fps)), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)
    cv2.putText(img, "Mode: " + modes[option], (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 4)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        break
