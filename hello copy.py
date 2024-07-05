import cv2
# print(cv2.__version__)
cap = cv2.VideoCapture(0) # 선생님과 관련된 비디오를 열어주세요.
while True:
    _, frame =cap.read()
    cv2.imshow("Video", frame)
    if cv2.waitKey(10) & 0xff ==ord('q'):
        break
cap.release()
cv2.destroyAllwindows()