import cv2
import numpy as np
import snake
import random
wait=-1
pos = (random.randint(10, 490),random.randint(10, 490))
i=3
apple_pos_x = random.randint(10, 490)
apple_pos_y = random.randint(10, 490)
key=5154
blank = np.zeros((500, 500, 3), dtype='uint8')
direction=['left','left']
direct='left'
k=0
l=[]
sk=snake.snake(pos,direction,3)
counter=0
while 1  :
    blank = np.zeros((500, 500, 3), dtype='uint8')

    k=1
    if counter>wait :
        l = sk.move(pos, blank, i, direction, k, l)
        if direction[0]=='right' :
            pos=(pos[0]+sk.width,pos[1])
            if len(l) != i:
                l.insert(0, (pos[0] , pos[1]))
                # l.insert(0, (pos[0] + sk.width, pos[1]))
                pos=(pos[0]+ sk.width, pos[1])
        elif direction[0]=='left' :
            pos=(pos[0]-sk.width,pos[1])
            if len(l) != i:
                l.insert(0, (pos[0] , pos[1]))
                # l.insert(0, (pos[0] + sk.width, pos[1]))
                pos=(pos[0]- sk.width, pos[1])
        elif direction[0]=='bottom' :
            pos=(pos[0],pos[1]+sk.width)
            if len(l) != i:
                l.insert(0, (pos[0] , pos[1]))
                # l.insert(0, (pos[0] + sk.width, pos[1]))
                pos=(pos[0], pos[1]+ sk.width)
        elif direction[0]=='top' :
            pos=(pos[0],pos[1]-sk.width)
            if len(l) != i:
                l.insert(0, (pos[0] , pos[1]))
                # l.insert(0, (pos[0] + sk.width, pos[1]))
                pos=(pos[0], pos[1]- sk.width)
        # if l[0] in l[3:] :
        #     break

        # if len(l) != i:
        #     if direction[0] == 'left':
        #         l.insert(0, (l[0][0] - sk.width, l[0][1]))
        #         pos=(l[0][0] - sk.width, l[0][1])
        #     elif direction[0] == 'right':
        #         l.insert(0, (l[0][0] + sk.width, l[0][1]))
        #     elif direction[0] == 'top':
        #         l.insert(0, (l[0][0], l[0][1] - sk.width))
        #     elif direction[0] == 'bottom':
        #         l.insert(0, (l[0][0], l[0][1] + sk.width))
        counter=0
    else :
        counter+=1

    if pos[1]>=500:
        pos=(pos[0],5)
    elif pos[1]<=0 :
        pos = (pos[0], 495)
    if pos[0]>=500:
        pos=(5,pos[1])
    elif pos[0]<=0 :
        pos = (495, pos[1])
    if ord('z')==key :
        direct='top'
        direction[1] = direction[0]
        direction[0] = direct
    if ord('q')==key :
        direct='left'
        direction[1] = direction[0]
        direction[0] = direct
    if ord('s')==key :
        direct='bottom'
        direction[1] = direction[0]
        direction[0] = direct
    if ord('d')==key :
        direct='right'
        direction[1] = direction[0]
        direction[0] = direct


    if (pos[0] in range(apple_pos_x-15,apple_pos_x+30)) and (pos[1] in range(apple_pos_y-15,apple_pos_y+30)) :
        apple_pos_x = random.randint(10, 490)
        apple_pos_y = random.randint(10, 490)
        i += 1
    score=i-3
    if (l[0] in l[3:]) and direction not in [['left','right'],['right','left'],['top','bottom'],['bottom','top']]:
        break
    cv2.putText(blank,'Your Score :'+str(score),(130,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0))
    cv2.rectangle(blank,(apple_pos_x,apple_pos_y),(apple_pos_x+15,apple_pos_y+15),(0,0,255),-1 )
    cv2.imshow('snake',blank)
    key=cv2.waitKey(75)