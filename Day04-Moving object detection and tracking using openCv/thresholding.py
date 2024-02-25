import cv2 
import imutils
img = cv2.imread("Day04-Moving object detection and tracking using openCv\download.jpeg")
cv2.imshow("image1",img)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
thresholding = cv2.threshold(gray_img,250,295,cv2.THRESH_BINARY)[1]
cv2.imshow("image2",thresholding)
cv2.waitKey(0)
cv2.destroyAllWindows()