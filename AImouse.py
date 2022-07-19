import numpy as np
import Handmodule as hm
import cv2 as cv
import time
import autopy as atp
import VirtualKeyboard
# import SoundControle
def main () :
    ptime=0
    detector=hm.HandDetect()
    cap=cv.VideoCapture(0)
    wait=2
    tim=0
    while 1 :
        ctime=time.time()
        fps=int(1/(ctime-ptime))
        ptime=ctime
        succ,img=cap.read()
        # img=cv.flip(img,1)
        hand,hand1,lmls1,lmls2=detector.findHands(img)
        if len(lmls1)!=0 :
           [x_1, y_1] = lmls1[12][1:]
           [x_2, y_2] = lmls1[8][1:]
           x_m = int((x_1 + x_2) / 2)
           y_m = (y_1 + y_2) // 2
           cv.line(img, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
           cv.circle(img, (x_1, y_1), 10, (0, 255, 255), -1)
           cv.circle(img, (x_2, y_2), 10, (0, 255, 255), -1)
           cv.circle(img, (x_m, y_m), 10, (0, 255, 255), -1)
           if (hand==[0,1,0,0,0]):
                xmouse,ymouse=int((x_2/540)*2000),int((y_2/380)*1300)
                if xmouse>1598 :
                    xmouse=1595
                if ymouse>898:
                    ymouse=898
                if xmouse<5 :
                    xmouse=5
                if ymouse<5:
                    ymouse=5
                atp.mouse.move(xmouse,ymouse)


           elif  hand==[0,1,1,0,0] :
                tim+=1
                if tim==wait:
                    cv.circle(img, (x_m, y_m), 20, (0, 255, 0), -1)
                    tim=0
                atp.mouse.click();print('left click')
        cv.putText(img,str(fps),(50,70),cv.FONT_HERSHEY_PLAIN,2,(0,0,255),2)
        cv.imshow('AI mouse',img)
        if hand==[0,1,0,0,1] :
            VirtualKeyboard.main()
        cv.waitKey(1)
main()
    # exec(open("E:/ComputerVisionProjects/SoundControle/SoundContro.py")).read()