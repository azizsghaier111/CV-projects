import time
import numpy as np
import handModule as hm
import mediapipe as mp
import cv2 as cv
from math import sqrt
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
def volumeC():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-20.0, None)
    ctime=0
    ptime=0
    cap=cv.VideoCapture(0)
    detector=hm.HandDetect(max_hands=1,detection_confidence=0.7)
    pvolume = -15
    while True:
        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        succ,img=cap.read()
        img=cv.flip(img,1)
        volumee=detector.findHands(img)
        if volumee==None :
            volume.SetMasterVolumeLevel(pvolume, None)
        else:
            volume.SetMasterVolumeLevel(volumee, None)
            pvolume=volumee
        cv.putText(img,str(int(fps)),(50,70),cv.FONT_HERSHEY_DUPLEX,1.0,(0,255,255),1)
        #info of the middle and index fingers


        cv.imshow('Volume Regulization', img)
        cv.waitKey(1)

volumeC()