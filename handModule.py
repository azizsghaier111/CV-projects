import cv2 as cv
import time
import numpy as np
import mediapipe as mp
from math import sqrt

class HandDetect():
    def __init__(self,mode=False,max_hands=2,detection_confidence=0.5,track_confidence=0.5):
        self.mode=mode
        self.max_hands=max_hands
        self.detection_confidence=detection_confidence
        self.track_confidence=track_confidence
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
    def findHands(self,img,draw=True,hand=None):
            distance=0
            h, w, c = img.shape
            imgRGB = cv.cvtColor(img, cv.COLOR_BGRA2RGB)
            results = self.hands.process(imgRGB)
            if draw:
                if results.multi_hand_landmarks:

                        for hanLms in results.multi_hand_landmarks:
                            for id, lm in enumerate(hanLms.landmark):
                                cx, cy = int(lm.x * w), int(lm.y * h)
                                cv.circle(img,(cx,cy),10,(0,0,255),-1)
                                lx=[hanLms.landmark[i].x*w for i in range(len(hanLms.landmark))]
                                ly = [hanLms.landmark[i].y * h for i in range(len(hanLms.landmark))]
                                x1=min(lx)
                                y1=min(ly)
                                x2= max(lx)
                                y2 = max(ly)
                            x_1 = int(hanLms.landmark[4].x*w)
                            y_1 = int(hanLms.landmark[4].y*h)
                            x_2 = int(hanLms.landmark[8].x*w)
                            y_2 = int(hanLms.landmark[8].y*h)
                            x_m=int((x_1+x_2)/2)
                            y_m=(y_1+y_2)//2
                            cv.line(img,(x_1, y_1),(x_2, y_2),(0,255,0),2)
                            cv.circle(img, (x_1, y_1), 10, (0, 0, 255), -1)
                            cv.circle(img, (x_2, y_2), 10, (0, 0, 255), -1)
                            cv.circle(img, (x_m, y_m), 10, (0, 0, 255), -1)
                            distance=int(sqrt((x_1-x_2)**2+(y_1-y_2)**2))
                            if distance > 270:
                                distance = 270
                            elif distance < 20:
                                distance = 20
                            cv.circle(img, (x_m, y_m), 10, (0, (distance-20)*255/250,255-(distance-20)*255/250), -1)
                            volume=int(((distance-20)/25)*10)
                            cv.rectangle(img,(60,100),(200,400),(0,255,0),thickness=1 )
                            cv.rectangle(img,(200,400),(60,-3*volume+400),(0,255,0),-1)
                            cv.putText(img,str(volume),(110,450),cv.FONT_HERSHEY_SIMPLEX,1.5,(0,255,0))
                            # if distance<50:
                            #     cv.circle(img, (x_m, y_m), 10, (0,0,255),-1)
                            distance = ((distance - 20) * 0.261) - 65.25
                            cv.rectangle(img,(int(x2)+30,int(y2)+30),(int(x1)-30,int(y1)-30),(0,255,255),2)
                            self.mpDraw.draw_landmarks(img,landmark_list=hanLms,connections=self.mpHands.HAND_CONNECTIONS)
                            return distance
                else:
                     return None



    def detectFind(self,img,hand=1):
        h, w, c = img.shape
        lmls=[]
        imgRGB = cv.cvtColor(img, cv.COLOR_BGRA2RGB)
        results=self.hands.process(imgRGB)
        if results.multi_hand_landmarks:
            hanlms=results.multi_hand_landmarks[hand-1]
            for id, lm in enumerate(hanlms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmls.append((cx,cy,id))
        return lmls
    # def fingersup(self,img,hand=1):
    #     l=[]
    #     f1=[1,2,3,4]
    #     f2=[5,6,7,8]
    #     f3=[9,10,11,12]
    #     f4=[13,14,15,16]
    #     f5=[17,18,19,20]
    #     h, w, c = img.shape
    #     imgRGB = cv.cvtColor(img, cv.COLOR_BGRA2RGB)
    #     results = self.hands.process(imgRGB)
    #     if results.multi_hand_landmarks:
    #         hanlms = results.multi_hand_landmarks[hand - 1]
    #         for id, lm in enumerate(hanlms.landmark):
    #             cx, cy = int(lm.x * w), int(lm.y * h)
    #             l.append(cy)
    #         fc1=[l[i] for i in f1]
    #         fc2=[l[i] for i in f2]
    #         fc3=[l[i] for i in f3]
    #         fc4=[l[i] for i in f4]
    #         fc5=[l[i] for i in f5]
    #         c1=(fc1[3]==max(fc1))
    #         c2=(fc2[3]==max(fc2))
    #         c3=(fc3[3]==max(fc3))
    #         c4=(fc4[3]==max(fc4))
    #         c5=(fc5[3]==max(fc5))
    #         return [c1,c2,c3,c4,c5]
    #     else:
    #         return [0,0,0,0,0]


# def main():
#     ctime = 0
#     ptime = 0
#     cap = cv.VideoCapture(0)
#     detector=HandDetect()
#     while True:
#         succ, img = cap.read()
#         img=cv.flip(img,1)
#         detector.findHands(img,True,1)
#         lmls=detector.detectFind(img,1)
#         if len(lmls)!=0 :
#             print('id={} , x={} , y={} '.format(lmls[4][0],lmls[4][1],lmls[4][2]))
#         ctime = time.time()
#         fps = 1 / (ctime - ptime)
#         ptime = ctime
#         cv.putText(img, str(int(fps)), (70, 50), cv.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
#         cv.imshow('cap', img)
#         cv.waitKey(1)
#
# main()
