import cv2 as cv
import time
import Handmodule as hm
import drawkeyboard
import numpy as np
import AImouse
def main():

    cap= cv.VideoCapture(0)
    import keyboard
    keys=drawkeyboard.keyboardm((10,100),10)
    cap.set(3,480)
    cap.set(4,640)
    blank=np.zeros((480,640,3),'uint8')
    detector=hm.HandDetect()
    wait=4
    k=0
    while  1 :
        _,img=cap.read()
        keys.draw(blank)
        hand1,hand2,lmls1,lmls2=detector.findHands(img)
        imgOut = cv.addWeighted(img, 0.5, blank, 0.5, 0.5)
        if hand1==[0,1,0,0,0] or hand1==[0,1,1,0,0] :
            [cx,cy]=lmls1[8][1:]
            for key in keys.keydict :
                if key==' ' and (cx in range(keys.keydict[key][0],keys.keydict[key][0]+400)) and ( cy in range(keys.keydict[key][1],keys.keydict[key][1]+50)):
                    cv.rectangle(imgOut, (keys.keydict[key][0], keys.keydict[key][1]),
                                 (keys.keydict[key][0] + 400, keys.keydict[key][1] + 50), (0, 255, 0), 1)
                    if hand1 == [0, 1, 1, 0, 0]:
                        if k == wait:
                            print(key)
                            keyboard.write(key)
                            k = 0
                        else:
                            k += 1
                elif (cx in range(keys.keydict[key][0],keys.keydict[key][0]+50)) and ( cy in range(keys.keydict[key][1],keys.keydict[key][1]+50)):
                    cv.rectangle(imgOut,(keys.keydict[key][0],keys.keydict[key][1]),(keys.keydict[key][0]+50,keys.keydict[key][1]+50),(0,255,0),1)
                    if hand1 == [0, 1, 1, 0, 0]:
                        if k == wait:
                            print(key)
                            keyboard.write(key)
                            k = 0
                        else:
                            k += 1
        if hand1==[0,1,0,0,1]:
            AImouse.main()
        cv.imshow('final',imgOut)
        cv.waitKey(1)
main()