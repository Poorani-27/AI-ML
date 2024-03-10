import cv2
import imutils
img = cv2.imread("Day04-Moving object detection and tracking using openCv\download.jpeg")
blur = cv2.GaussianBlur(img, (5, 5), 2)  
cv2.imshow("image1",img)
cv2.imshow("image2",blur)
cv2.waitKey(0)
cv2.destroyAllWindows()