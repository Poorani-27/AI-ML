import cv2
import imutils
img = cv2.imread("Day04-Moving object detection and tracking using openCv\download.jpeg")
cv2.imshow("image1",img)

resizeImg = imutils.resize(img,width=100)
cv2.imwrite("resizedImg.jpeg",resizeImg)
cv2.imshow("image",resizeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()