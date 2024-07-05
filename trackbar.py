import cv2
import numpy as np

def callBack(value):
    pass

img_path = 'cat.jpg'

img = cv2.imread(img_path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (5,5), 10)                   

cv2.namedWindow('Slider')                                        # 우리가 만드려는 Trackbar의 이름을 정하는 것
cv2.createTrackbar('high_t','Slider',0, 225, callBack)          # 우리가 조절하는 Trackbar 만드는 것 (bar의 처음 위치와 마지막 위치도 알려줌)

while True:

    high_t = cv2.getTrackbarPos("high_t","Slider")                # 실시간으로 우리가 움직이는 Trackbar의 위치(Position)을 받는것
    img_canny = cv2.Canny(img_blur, 10, high_t)                   

    cv2.imshow('Cat',img_canny)

    if cv2.waitKey(10) & 0xff==ord('q'):
        break

cv2.destroyAllWindows()