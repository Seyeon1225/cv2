import cv2

#print(cv2.__version__)

cap = cv2.VideoCapture(0)          # 어디에 있는 카메라를 쓸 지 정하는 것
cap.set(30, 200)
cap.set(40, 100)
low = 50
high = 150

while True :
    ret, frame = cap.read()        # 프레임을 while에 들어가서 계속 보는 것
    #print(ret)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    canny_frame = cv2.Canny(gray_frame,low,high)
    block_frame = cv2.GaussianBlur(frame,(5,5),0)            # (5,5)sms 무조건 홀수로만 가능, 뒤에 오는 0은 표준편자

    #cv2.imshow("Video",frame)           # Video라는 이름으로 저장
    #cv2.imshow("Gray",gray_frame) 
    #cv2.imshow("rgb",rgb_frame)
    cv2.imshow("Canny",canny_frame)
    cv2.imshow("Block_frame",block_frame)

    if cv2.waitKey(10) & 0xff ==ord('q'):      # q를 치면 종료
        break

cap.release()                               # 카메라 열어서 확인

cv2.destroyAllWindows()                    