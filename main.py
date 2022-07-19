import numpy as np
import Handmodule as hm
import cv2 as cv
import time
import autopy as atp
import keyboard
import drawkeyboard
j=False
selector=0
ptime = 0
detector = hm.HandDetect()
Webcam=0
cap = cv.VideoCapture(Webcam)
wait =7
tim = 4
keys=drawkeyboard.keyboardm((15,100),10,keyboard_color=(255,0,255),character_color=(255,0,0))
blank=np.zeros((480,640,3),'uint8')
k=4
c=''
ch=''
maxch=20
keyboard_status=0# 0 lower #1 upcase
backspace_time=0
while 1:

    ctime = time.time()
    fps = int(1 / (ctime - ptime))
    ptime = ctime
    succ, img = cap.read()
    img=cv.flip(img,1)
    hand, hand1, lmls1, lmls2 = detector.findHands(img)
    if selector in [0,1,2,3,4,5,6] :
        cv.putText(img, 'Mouse Mode', (230, 450), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)
        if len(lmls1) != 0:
            print(lmls1)
            [x_1, y_1] = lmls1[12][1:]
            [x_2, y_2] = lmls1[8][1:]
            x_m = int((x_1 + x_2) / 2)
            y_m = (y_1 + y_2) // 2
            cv.line(img, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
            cv.circle(img, (x_1, y_1), 10, (0, 255, 255), -1)
            cv.circle(img, (x_2, y_2), 10, (0, 255, 255), -1)
            cv.circle(img, (x_m, y_m), 10, (0, 255, 255), -1)
            if (hand == [0, 1, 0, 0, 0]):
                xmouse, ymouse = int((x_2 / 540) * 2000), int((y_2 / 380) * 1300)
                if xmouse > 1598:
                    xmouse = 1595
                if ymouse > 898:
                    ymouse = 898
                if xmouse < 5:
                    xmouse = 5
                if ymouse < 5:
                    ymouse = 5
                atp.mouse.move(xmouse, ymouse)


            elif hand == [0, 1, 1, 0, 0]:
                tim += 1
                if tim == wait:
                    cv.circle(img, (x_m, y_m), 20, (0, 255, 0), -1)
                    tim = 0
                    atp.mouse.click();
                    print('left click')
            if  hand==[0,1,0,0,1]:
                selector+=1
        print(hand,hand1)

    if selector>=wait :

        keys.draw(blank,keyboard_status)
        imgOut = cv.addWeighted(img, 0.5, blank, 0.5, 0.5)
        if hand== [0, 1, 0, 0, 0] or hand == [0, 1, 1, 0, 0]:
            [cx, cy] = lmls1[8][1:]
            for key in keys.keydict:
                if key == ' ' and (cx in range(keys.keydict[key][0], keys.keydict[key][0] + 400)) and (
                        cy in range(keys.keydict[key][1], keys.keydict[key][1] + 50)):
                    cv.rectangle(imgOut, (keys.keydict[key][0], keys.keydict[key][1]),
                                 (keys.keydict[key][0] + 400, keys.keydict[key][1] + 50), (0, 255, 0), 1)

                    if hand == [0, 1, 1, 0, 0]:

                        if k >= wait:
                            print('space')
                            keyboard.press_and_release('Space')
                            k = 0
                            c=' '
                            backspace_time=0
                            wait=7
                        else :
                            k = k + 1
                elif key == 'backspace' and (cx in range(keys.keydict[key][0], keys.keydict[key][0] + 100)) and (
                                cy in range(keys.keydict[key][1], keys.keydict[key][1] + 50)):
                            cv.rectangle(imgOut, (keys.keydict[key][0], keys.keydict[key][1]),
                                         (keys.keydict[key][0] + 100, keys.keydict[key][1] + 50), (0, 255, 0), 1)
                            if hand == [0, 1, 1, 0, 0]:
                                if k >= wait:
                                    print(key)
                                    keyboard.press_and_release('Backspace')
                                    k = 0
                                    ch=ch[:len(ch)-1]
                                    j==True
                                    backspace_time+=1
                                    if 6>backspace_time>4 :
                                        wait=3
                                    elif 10>backspace_time>6 :
                                        wait=1
                                else:
                                     k += 1
                elif key == 'enter' and (cx in range(keys.keydict[key][0], keys.keydict[key][0] + 110)) and (
                                cy in range(keys.keydict[key][1], keys.keydict[key][1] + 40)):
                            cv.rectangle(imgOut, (keys.keydict[key][0], keys.keydict[key][1]),
                                         (keys.keydict[key][0] + 110, keys.keydict[key][1] + 40), (0, 255, 0), 1)
                            if hand == [0, 1, 1, 0, 0]:
                                if k >= wait:
                                    print(key)
                                    keyboard.press_and_release('Enter')
                                    k = 0
                                    ch=''
                                    backspace_time=0
                                    wait=7
                                else:
                                     k += 1
                elif key == 'low/up' and (cx in range(keys.keydict[key][0], keys.keydict[key][0] + 100)) and (
                                cy in range(keys.keydict[key][1], keys.keydict[key][1] + 50)):
                            cv.rectangle(imgOut, (keys.keydict[key][0], keys.keydict[key][1]),
                                         (keys.keydict[key][0] + 100, keys.keydict[key][1] + 50), (0, 255, 0), 1)
                            if hand == [0, 1, 1, 0, 0]:
                                if k >= wait:
                                    print(key)
                                    keyboard.press_and_release('caps lock')
                                    k = 0
                                    keyboard_status+=1
                                    backspace_time = 0
                                    wait=7
                                    if keyboard_status>1 :
                                        keyboard_status=0
                                else:
                                     k += 1
                elif (cx in range(keys.keydict[key][0], keys.keydict[key][0] + 50)) and (
                        cy in range(keys.keydict[key][1], keys.keydict[key][1] + 50)) and key not in ['enter','space','backspace']:
                    cv.rectangle(imgOut, (keys.keydict[key][0], keys.keydict[key][1]),
                                 (keys.keydict[key][0] + 50, keys.keydict[key][1] + 50), (0, 255, 0), 1)
                    if hand == [0, 1, 1, 0, 0]:
                        if k >= wait:
                            print(key)
                            if key=='.' :
                                keyboard.write('.')
                            else :
                             keyboard.press_and_release(key)
                            k = 0
                            c=key
                            backspace_time = 0
                            wait=7
                        else:
                            k += 1
        cv.putText(imgOut, 'Keyboard Mode', (230, 450), cv.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 1)
        if keyboard_status==0 :
            cv.putText(imgOut, 'Lower Characters', (10, 470), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

        elif keyboard_status == 1:
                cv.putText(imgOut, 'Upper Characters', (10, 470), cv.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
        if  hand==[0,1,0,0,1] :
                print('switch')
                selector+=1
                if selector>11 :
                    selector=0
        ch=ch[:]+c
        ch1=ch[:]
        if len(ch1)>=maxch :
            ch1=ch1[len(ch)-maxch:len(ch)]
        elif j==True:
            if len(ch)>=maxch:
             ch1=ch[len(ch)-maxch:]
            else :
                ch1=ch[:]
            j=False
        c=''
        cv.putText(imgOut,ch1,(keys.origin[0]+60,keys.origin[1]-25),cv.FONT_HERSHEY_PLAIN,2,(0,255,0),2)
        print(k)
    cv.putText(img, str(fps), (50, 70), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    if selector>=8:
         cv.putText(imgOut, str(wait), (50, 90), cv.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
    if selector in [0,1,2,3,4,5,6,7] :
        cv.imshow('Keyboard & Mouse', img)
    elif selector>=8 :
        cv.imshow('Keyboard & Mouse',imgOut)
        cv.imshow('blank',blank)
    cv.waitKey(1)


gVFB