import cv2
def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        colorsB = image[y,x,0]
        colorsG = image[y,x,1]
        colorsR = image[y,x,2]
        colors = image[y,x]
        print("Red: ",colorsR)
        print("Green: ",colorsG)
        print("Blue: ",colorsB)
        font = cv2.FONT_HERSHEY_COMPLEX
        if colorsR==0 and colorsG==0 and colorsB==0:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'BLACK', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        if colorsR==237 and colorsG==28 and colorsB==36:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'RED', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        if colorsR==255 and colorsG==242 and colorsB==0:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'YELLOW', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        if colorsR==181 and colorsG==230 and colorsB==29:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'L GREEN', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        if colorsR==255 and colorsG==127 and colorsB==39:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'ORANGE', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        if colorsR==255 and colorsG==0 and colorsB==128:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'PINK', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        if colorsR==34 and colorsG==177 and colorsB==76:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'D GREEN', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        if colorsR==153 and colorsG==217 and colorsB==234:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'SKYBLUE', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        if colorsR==0 and colorsG==162 and colorsB==232:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'BLUE', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        if colorsR==163 and colorsG==73 and colorsB==164:
            img2 = cv2.rectangle(image, (10, 10), (330, 150), (0, 0, 0), -1)
            img5 = cv2.putText(image, 'PURPLE', (10, 100), font, 2, (255, 255, 255), 4, cv2.LINE_AA)
        print("BRG Format: ",colors)
        print("Coordinates of pixel: X: ",x,"Y: ",y)
# Read an image, a window and bind the function to window
image = cv2.imread("untitled.png")
cv2.namedWindow('mouseRGB',1)
cv2.setMouseCallback('mouseRGB',mouseRGB)
#Do until esc pressed
while(1):
    cv2.imshow('mouseRGB',image)
    if cv2.waitKey(20) & 0xff==27:
        break
#if esc pressed, finish.
cv2.destroyAllWindows()