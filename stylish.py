import cv2
import numpy as np

def callBack1(value) :
    pass

def callBack2(value) :
    pass

img_path = 'fish.jpg'

img = cv2.imread(img_path)
img = cv2.resize(img, (400, 400))

cv2.namedWindow('Style',cv2.WINDOW_NORMAL)
cv2.createTrackbar("sigma_s", "Style", 0, 200, callBack1)
cv2.createTrackbar("sigma_r", "Style", 0, 100, callBack2)                          # 여기서 r값은 무조건 1보다 작아야 한다. 그러나 시작을 0, 끝을 1로 하면 끄고 키는 것밖에 못한다.
                                                                                   # 그래서 여기서는 1,100 으로 잡아둔 후에 아래에서 100으로 나누어서 소수로 다시 만들어 준다.


while True :

    sigma_s = cv2.getTrackbarPos("sigma_s","Style")
    sigma_r = cv2.getTrackbarPos("sigma_r","Style") / 100                           # r값은 밝기로 무조건 0,1로만 있어야함

    img_style = cv2.stylization(img, sigma_s, sigma_r)                              # 여기에 들어가는 변수들은 위의 getTrackbarPos에서 가져온 변수와 이름이 같다면 다른 것을 사용해도 상관없다

    cv2.imshow('Image',img)
    cv2.imshow('Image_style',img_style)

    if cv2.waitKey(10) & 0xff == ord('q'):
        break

cv2.destroyAllWindows()