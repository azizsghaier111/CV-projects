import cv2 as cv
def head_of_list(l:list,element) :
    l.insert(0,element)
    l.pop()
class snake() :

    def __init__(self,pos,direction,length,width=20):
        self.length=length
        self.direction=direction
        self.pos=pos
        self.width=width
    def move(self,pos,img,i,direction,intialization_check,l):
        #intialization via the direction
        if intialization_check==0 :
            for k in range(i) :
                i=pos[0]
                j=pos[1]
                i=i+k*self.width
                l.append((i,j))

            for square in l :
                cv.rectangle(img,(square[0],square[1]),(square[0]+self.width,square[1]+self.width),(0,255,0),-1)
            return l
        else :
            head_of_list(l,pos)
            for square in l :
                cv.rectangle(img,(square[0],square[1]),(square[0]+self.width,square[1]+self.width),(0,255,0),-1)

            return l






        #
        # if i==1 :
        #  L=[pos]
        #
        # if direction in ['right','left'] :
        #  for k in range (i,0,-1) :
        #     print(k)
        #     cv.rectangle(img,(pos[0]+self.width*k,pos[1]),(pos[0]+self.width*(1+k),pos[1]+self.width),(0,255,0),-1)
        # if direction in ['top','bottom'] :
        #  for k in range (i,0,-1) :
        #          cv.rectangle(img,(pos[0],pos[1]+self.width*k),(pos[0]+self.width,pos[1]+self.width*(1+k)),(0,255,0),-1)
    def grow(self,pos,img):
        cv.rectangle(img, (pos[0]+self.width, pos[1]+self.width), (pos[0] + self.width+self.width, pos[1] + self.width+self.width), (0, 255, 0), -1)