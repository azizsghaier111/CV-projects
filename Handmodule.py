import cv2 as cv
import time
import autopy as atp
import numpy as np
import mediapipe as mp
from numpy import angle

class HandDetect():
    def __init__(self,mode=False,max_hands=2,detection_confidence=0.5,track_confidence=0.5):
        self.mode=mode
        self.max_hands=max_hands
        self.detection_confidence=detection_confidence
        self.track_confidence=track_confidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self,img,draw=True):
            h, w, c = img.shape
            l=[0,0,0,0,0]
            l1= [0, 0, 0, 0, 0]
            distance=250
            lmls1 = []
            lmls2=[]
            i=0
            imgRGB = cv.cvtColor(img, cv.COLOR_BGRA2RGB)
            results = self.hands.process(imgRGB)
            if draw:
                if results.multi_hand_landmarks:
                    m=-1
                    l3=[]
                    for k in range(len(results.multi_hand_landmarks)-1,-1,-1):
                            hanLms=results.multi_hand_landmarks[k]
                            lmls=[]
                            for id, lm in enumerate(hanLms.landmark):
                                cx, cy = int(lm.x * w), int(lm.y * h)
                                lmls.append([id,cx,cy])
                            if i==0 :
                                lmls1=lmls
                            else:
                                lmls2=lmls
                            i+=1
                            self.mpDraw.draw_landmarks(img,landmark_list=hanLms,connections=self.mpHands.HAND_CONNECTIONS)
                            lx = [int(hanLms.landmark[i].x * w) for i in range(len(hanLms.landmark))]
                            ly = [int(hanLms.landmark[i].y * h) for i in range(len(hanLms.landmark))]
                            x1 = min(lx)
                            y1 = min(ly)
                            x2 = max(lx)
                            y2 = max(ly)
                            l3.append([x1,y1,x2,y2])
                            print(len(l3))
                            cv.rectangle(img, (x1-20, y2+20), (x2+20, y2 + 50), (0, 255, 0), -1)
                            if m == -1:
                                cv.putText(img, 'right', ((lmls1[0][1], lmls1[0][2] + 30)), cv.FONT_HERSHEY_PLAIN, 1,
                                           (0, 0, 255), 1)
                            elif len(lmls2)!=0 :

                                cv.putText(img, 'right', (lmls1[0][1], lmls1[0][2] + 30), cv.FONT_HERSHEY_PLAIN, 1,
                                           (0, 0, 255), 1)
                                cv.putText(img, 'left', (lmls2[0][1], lmls2[0][2] + 30), cv.FONT_HERSHEY_PLAIN, 1,
                                           (0, 0, 255),
                                           1)

                            m+=1
                            cv.rectangle(img, (x1-20, y1-20), (x2+20, y2+20), (0, 255, 0), thickness=1)


                    hand = {1: [1, 2, 3, 4], 2: [5, 6, 7, 8], 3: [9, 10, 11, 12], 4: [13, 14, 15, 16],
                                    5: [17, 18, 19, 20]}
                    if len(lmls1) != 0:
                                for m in hand.keys():
                                    if lmls1[hand[m][3]][2] == min([lmls1[k][2] for k in hand[m]]):
                                        l[m - 1] = 1

                                x1 = lmls1[0][1]
                                x2 = lmls1[3][1]
                                x3 = lmls1[4][1]
                                y1 = lmls1[0][2]
                                y2 = lmls1[3][2]
                                y3 = lmls1[4][2]
                                z1 = complex((x3 - x2), (y3 - y2))
                                z2 = complex((x2 - x1), (y2 - y1))
                                if z1!=0 :
                                    a = -angle(z2 / z1, True)
                                    # cv.putText(img, str(a), (100, 100), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
                                    if abs(a) > 10:
                                        l[0] = 0
                    if len(lmls2) != 0:
                                for m in hand.keys():
                                    if lmls2[hand[m][3]][2] == min([lmls2[k][2] for k in hand[m]]):
                                        l1[m - 1] = 1

                                x1 = lmls2[0][1]
                                x2 = lmls2[3][1]
                                x3 = lmls2[4][1]
                                y1 = lmls2[0][2]
                                y2 = lmls2[3][2]
                                y3 = lmls2[4][2]
                                z1 = complex((x3 - x2), (y3 - y2))
                                z2 = complex((x2 - x1), (y2 - y1))
                                if z1 != 0:
                                    a = -angle(z2 / z1, True)
                                    # cv.putText(img, str(a), (100, 100), cv.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 1)
                                    if abs(a) > 10:
                                        l1[0] = 0
                            # atp.mouse.move(x_1,y_1)
            return l,l1,lmls1,lmls2