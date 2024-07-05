import cv2
import numpy as np

path1 = 'cat.jpg'
path2 = 'fish.jpg'

img1 = cv2.imread(path1)
img2 = cv2.imread(path2)

#print(img1.shape)   #이미지 크기 확인 후 비교하여 같게 만들자
#print(img2.shape)

img1 = cv2.resize(img1, (img2.shape[1],img2.shape[0]))                         # resize는 요소르 넣을 때 1,0

print(img1.shape)
 
img3 = cv2.add(img1,img2)                                                      # add로 이미지 합치기

img4 = img1[0:90,0:279,2]                                                      # 이미지를 자르는 법

img5 = img2

img5[0:90,0:279,] = [0,225,0]                              # 여기는 [:,:,ㅁ]로 ㅁ에 아무것도 넣지 않으므로써 전체의 색을 [0,225,0으로 만든다는 것이다]

#img5[:,:,1] = 225                                         # 여기는 앞에서 지정한 [:,:,1] 즉 초록색부분만 최고의 초록색으로 올린 다는 것이고

mask = np.ones((img2.shape[0],img2.shape[1],3),dtype='uint8')*50              # 차원이 않맞아서 오류가 날 수 있으니 아것 신경쓰기
#print(mask.shape)                                                            # 요소로 넣을 때 도 위와 달리 0,1

img_brighter = cv2.add(img1, mask)
img_darker = cv2.subtract(img1, mask)                                         # bgr값을 뺼 수 있음

#cv2.imshow('Cat',img1)
#cv2.imshow('Fish',img2)
#cv2.imshow('CatFish',img3)
#cv2.imshow('brighter',img_brighter)
#cv2.imshow('darker',img_darker)
#cv2.imshow('half',img4)
cv2.imshow('be_green',img5)

cv2.waitKey()
cv2.destroyAllWindows()