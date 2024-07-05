import cv2

cap = cv2.VideoCapture(0)      

while True :
    ret, frame = cap.read()    
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow("Video",frame)           
    cv2.imshow("HVS_Video",hsv_frame)  

    if cv2.waitKey(10) & 0xff == 27:    
        break

cap.release()                            

cv2.destroyAllWindows()                    