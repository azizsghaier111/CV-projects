import cv2
import keyboard


class button() :

    def __init__(self,origin:tuple,height=50,width=50,keyboard_color=(255,0,255),character_color=(255,255,255)):
        self.origin=origin
        self.height=height
        self.width=width
        self.keyboard_color=keyboard_color
        self.character_color=character_color

    def draw(self,img,char):
        cv2.rectangle(img,self.origin,(self.origin[0]+self.width,self.origin[1]+self.height),self.keyboard_color,-1)
        if char!='CapsLock' :
            cv2.putText(img,char,(self.origin[0]+15,self.origin[1]+33),cv2.FONT_HERSHEY_PLAIN,2,self.character_color,2)
        else:
            cv2.putText(img, char, (self.origin[0] + 15, self.origin[1] + 33), cv2.FONT_HERSHEY_PLAIN, 1,
                        self.character_color, 2)
#
class keyboardm() :
    def __init__(self,origin:tuple,space,keyboard_color=(255,0,255),character_color=(255,255,255)):
        self.origin=origin
        self.space=space
        self.keyboard_color=keyboard_color
        self.character_color=character_color
    def draw(self,img,Upcase=0):
        space=self.origin[0]
        if Upcase==1:
            self.keydict = dict()
            cv2.rectangle(img,(self.origin[0]+50,self.origin[1]-50),(self.origin[0]+500,self.origin[1]-10),self.keyboard_color,-1)
            L=['Q','W','E','R','T','Y','U','I','O','P']
            for i in range(10) :
                key=button(origin=(space,self.origin[1]),keyboard_color=self.keyboard_color, character_color=self.character_color)
                self.keydict[L[i]]=(space,self.origin[1])
                key.draw(img,L[i])
                space=self.space+space+key.width
            L1=['A','S','D','F','G','H','J','K','L',';']
            space=self.origin[0]+15
            for i in range(10) :
                key=button(origin=(space,self.origin[1]+self.space+key.height),keyboard_color=self.keyboard_color, character_color=self.character_color)
                key.draw(img,L1[i])
                self.keydict[L1[i]]=space,self.origin[1]+self.space+key.height
                space=self.space+space+key.width
            space = self.origin[0] +30
            L2=['Z','X','C','V','B','N','M',',','.','/']
            for i in range(10):
                key = button(origin=(space, self.origin[1] + 2*self.space +2* key.height),keyboard_color=self.keyboard_color, character_color=self.character_color)
                key.draw(img, L2[i])
                self.keydict[L2[i]]=space, self.origin[1] + 2*self.space +2* key.height
                space = self.space + space + key.width
        else :
            self.keydict = dict()
            cv2.rectangle(img, (self.origin[0] + 50, self.origin[1] - 50), (self.origin[0] + 500, self.origin[1] - 10),
                          self.keyboard_color, -1)
            L = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
            for i in range(10):
                key = button(origin=(space, self.origin[1]),keyboard_color=self.keyboard_color, character_color=self.character_color)
                self.keydict[L[i].lower()] = (space, self.origin[1])
                key.draw(img, L[i].lower())
                space = self.space + space + key.width
            L1 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';']
            space = self.origin[0] + 15
            for i in range(10):
                key = button(origin=(space, self.origin[1] + self.space + key.height),keyboard_color=self.keyboard_color, character_color=self.character_color)
                key.draw(img, L1[i].lower())
                self.keydict[L1[i].lower()] = space, self.origin[1] + self.space + key.height
                space = self.space + space + key.width
            space = self.origin[0] + 30
            L2 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
            for i in range(10):
                key = button(origin=(space, self.origin[1] + 2 * self.space + 2 * key.height),keyboard_color=self.keyboard_color, character_color=self.character_color)
                key.draw(img, L2[i].lower())
                self.keydict[L2[i].lower()] = space, self.origin[1] + 2 * self.space + 2 * key.height
                space = self.space + space + key.width

        key = button(origin=(self.origin[0]+100, self.origin[1] + 3 * self.space + 3 * key.height),width=400,keyboard_color=self.keyboard_color, character_color=self.character_color)
        key.draw(img, '')
        self.keydict[' ']=self.origin[0]+100, self.origin[1] + 3 * self.space + 3 * key.height
        key = button(origin=(self.origin[0] -10, self.origin[1] + 3 * self.space + 3 * key.height), width=100,keyboard_color=self.keyboard_color, character_color=self.character_color)
        key.draw(img, 'CapsLock')
        self.keydict['low/up'] = self.origin[0] -10, self.origin[1] + 3 * self.space + 3 * key.height
        key = button(origin=(self.origin[0] + 500+10, self.origin[1] + 3 * self.space + 3 * key.height),width=100,keyboard_color=self.keyboard_color, character_color=self.character_color)
        key.draw(img,'back')
        self.keydict['backspace'] = self.origin[0] + 510, self.origin[1] + 3 * self.space + 3 * key.height
        key = button(origin=(self.origin[0]+500+10, self.origin[1]-50), width=110,height=40,keyboard_color=self.keyboard_color, character_color=self.character_color)
        key.draw(img, 'enter')
        self.keydict['enter']=self.origin[0]+500+10, self.origin[1]-50
