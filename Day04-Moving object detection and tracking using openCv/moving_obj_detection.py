import cv2
import time
import imutils

cam =cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
area =500
while True:
    _,img =cam.read()
    text = "Normal "
    img = imutils.resize(img,width=500)
    gray_img =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gaussian_img = cv2.GaussianBlur(gray_img,(21,21),0)
    if first_frame is None : 
        first_frame =gaussian_img
        continue
    imgDiff =cv2.absdiff(first_frame,gaussian_img)
    thresh_img = cv2.threshold(imgDiff,25,255,cv2.THRESH_BINARY)[1]
    thresh_img=cv2.dilate(thresh_img, None,iterations =2 )
    cnts = cv2.findContours(thresh_img.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts=imutils.grab_contours(cnts)
    for c in cnts:
        if cv2.contourArea(c)<area :
            continue
        (x,y,w,h)=cv2.boundingRect(c)
        cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),2)
        text="Moving Object Detected"
    print(text)
    cv2.putText(img , text , (10,20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,255),2)
    cv2.imshow("videocapturing",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
cam.release()
cv2.destroyAllWindows()
