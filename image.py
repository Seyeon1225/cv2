import cv2
import numpy as np

path = 'cat.jpg'

image = cv2.imread(path)

cv2.resize(image, dsize=(200, 100))

print(image.shape)
print(image.shape[0])             # image.shape[0]이건 높이를 나타냄

cv2.circle(image,(image.shape[1]//2, image.shape[0]//2), 100, (225,0,0), 10)        # 내부 설명(x좌표,y좌표,크기,색,두께,)
cv2.rectangle(image,(image.shape[1]//2, image.shape[0]//2), (100,400),(225,0,0), 10) 

gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow('Cat',image)
#cv2.imshow('gray_image',gray_image)

cv2.waitKey()
cv2.destroyAllWindows()