import time

import cv2

from cvzone.HandTrackingModule import HandDetector


class Button:

    def __init__(self, pos, width, height, val):

        self.pos = pos
        self.width = width
        self.height = height
        self.val = val

    def draw(self, img):
        cv2.rectangle(img, self.pos, (self.pos[0]+self.width, self.pos[1]+self.height),
                      (225, 225, 225), cv2.FILLED)
        cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                      (50, 50, 50), 3)
        cv2.putText(img, self.val, (self.pos[0] + 37, self.pos[1] + 64), cv2.FONT_HERSHEY_PLAIN,
                   3, (50, 50, 50), 4)


    def checkClick(self,x,y):
        if self.pos[0] < x < self.pos[0]+ self.width and self.pos[1] < y < self.pos[1]+ self.height:
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (244, 194, 194), cv2.FILLED)
            cv2.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height),
                          (50, 50, 50), 3)
            cv2.putText(img, self.val, (self.pos[0] + 37, self.pos[1] + 64), cv2.FONT_HERSHEY_PLAIN,
                        3, (0, 0, 0), 4)

            return True
        else:
            return False

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280) # width
cap.set(4,720) # height
detector = HandDetector(detectionCon=0.8, maxHands=1)

# creating buttons
buttonListVals = [['7', '8', '9', '*'],
                  ['4', '5', '6', '-'],
                  ['1', '2', '3', '+'],
                  ['0', '/', '.', '=']]


buttonList = []
for x in range(4):
    for y in range(4):
        xpos = x*100 + 100
        ypos = y*100 + 100
        buttonList.append(Button((xpos,ypos), 100, 100, buttonListVals[y][x]))


# variables
myEq = ''
delayCounter = 0



# Loop
while True:
    # get img from webcam
    success, img = cap.read()
    img = cv2.flip(img, 1)

    # detection of hand
    hands, img = detector.findHands(img, flipType=False)



    # draw all buttons
    cv2.rectangle(img, (100,20), (100+400,50 +100), (225,225,225), cv2.FILLED)
    cv2.rectangle(img, (100,20), (100 + 400, 50 + 100), (50, 50, 50), 3)
    for button in buttonList:
        button.draw(img)

    # check for hand
    if hands:
        lmList = hands[0]['lmList']
        length, _, img = detector.findDistance((lmList[8][0],lmList[8][1]), (lmList[12][0],lmList[12][1]), img)
        # print(length)
        length2, _, img = detector.findDistance((lmList[4][0], lmList[4][1]), (lmList[8][0], lmList[8][1]), img)
        if length2<50:
            myEq = ''

        x,y = lmList[8][0],lmList[8][1]
        if length<40:
            for i,button in enumerate(buttonList):
                if button.checkClick(x,y) and delayCounter==0:
                    myVal = buttonListVals[int(i%4)][int(i/4)]
                    if myVal == "=":
                        if myEq == '':
                            myEq=''
                        else:
                            myEq = str(eval(myEq))
                    else:
                        myEq += myVal
                    # time.sleep(0.2)
                    delayCounter = 1


    # avoid duplicates
    if delayCounter != 0:
        delayCounter += 1
        if delayCounter >10:
            delayCounter = 0




    # display the Eqs
    cv2.putText(img, myEq, (110,80), cv2.FONT_HERSHEY_PLAIN,
                3, (50, 50, 50), 4)

    # Display img
    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('c'):
        myEq = ''
