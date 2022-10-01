import os
import pyautogui
import time
from random import randint
from PIL import Image

SCN = 7 #single cycle number
TCN = 12 #total cycle number


def ImgClick(ImgName, wait_time = 3, conf = 0.9):
    location = pyautogui.locateCenterOnScreen('img/' + ImgName + '.png', confidence=conf)
    img = Image.open('img/' + ImgName + '.png')
    if location is not None:
        now_time = time.strftime('%H:%M:%S', time.localtime())
        print('[%s] successful to find icon %s' %(now_time, ImgName))
        #pyautogui.moveTo(float(location.x) + randint(-(img.width//3), (img.width//3)), float(location.y) + randint(-(img.height//3), (img.height//3)), duration=1)
        pyautogui.click(int(location.x) + randint(-img.width//3, img.width//3), int(location.y) + randint(-img.height//3, img.height//3), clicks=1, button='left')
        time.sleep(wait_time)
        return 1
    else:
        now_time = time.strftime('%H:%M:%S', time.localtime())
        print('[%s] fail to find icon %s' %(now_time, ImgName))
        return 0

def exist(ImgName, conf = 0.9):
    img = pyautogui.locateCenterOnScreen('img/' + ImgName + '.png', confidence=conf)
    if img is not None:
        now_time = time.strftime('%H:%M:%S', time.localtime())
        print('[%s] the icon %s is exist' % (now_time, ImgName))
        return True
    else:
        now_time = time.strftime('%H:%M:%S', time.localtime())
        print('[%s] the icon %s is not exist' % (now_time, ImgName))
        return False

def enhance():
    ImgClick('dock')
    # ImgClick('filter') #设置筛选条件为可强化
    # if exist('enhanceable_false'):
    #     ImgClick('enhanceable_false')
    # elif exist('enhanceable_true'):
    #     time.sleep(3)
    # ImgClick('confirm')
    pyautogui.click(randint(220, 380), randint(210, 450), clicks=1, button='left') #select the first wife that can be strengthened
    time.sleep(3)
    ImgClick('enhance_page')
    while True:
        ImgClick('enhance_advice', 2)
        if exist('none_to_enhance'):
            break
        ImgClick('enhance')
        ImgClick('confirm')
        ImgClick('confirm')
        pyautogui.click(950 + randint(-100, 100), 850 + randint(-100, 100))  #click anykey
        time.sleep(3)
    time.sleep(3)
    pyautogui.click(1848 + randint(-20, 20), 117 + randint(-20, 20))  #click home button
    time.sleep(3)

def retire():
    ImgClick('build')
    pyautogui.click(73 + randint(-45, 45), 876 + randint(-45, 45))  #successful to entir the retire page
    time.sleep(3)
    while True:
        ImgClick('one_key_retire', 2)
        if exist('none_to_retire'):
            break
        ImgClick('confirm')
        ImgClick('confirm')  #let my wife take a fucking rest
        pyautogui.click(950 + randint(-100, 100), 850 + randint(-100, 100)) #click anykey
        time.sleep(3)
        ImgClick('confirm')
        ImgClick('confirm')
        pyautogui.click(950 + randint(-100, 100), 850 + randint(-100, 100))  # click anykey
        time.sleep(3)
    time.sleep(3)
    pyautogui.click(1848 + randint(-20, 20), 117 + randint(-20, 20))  # click home button
    time.sleep(3)

def D3():
    for n in range(TCN):
        ImgClick('attack')
        pyautogui.click(randint(900, 1400), randint(300, 500), clicks=1, button='left')  # 进入活动地图
        time.sleep(3)
        ImgClick('D3')
        ImgClick('go_now_level')
        ImgClick('go_now_formation')
        m = 1
        time.sleep(30)
        while True:
            if exist('attack_again'):
                if m >= SCN:
                    break
                ImgClick('attack_again')
                m += 1
            else:
                time.sleep(30)
        pyautogui.click(1679 + randint(-150, 150), 622 + randint(-150, 150))  #exit the attack again page
        time.sleep(3)
        pyautogui.click(1848 + randint(-20, 20), 117 + randint(-20, 20))  # click home button
        time.sleep(3)
        enhance()
        retire()



if __name__ == '__main__':
    time.sleep(3)
    D3()

