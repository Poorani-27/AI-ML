import cv2
#load img
img = cv2.imread("Day03-Computer vision libraries\download.jpeg")
cv2.imshow("Image",img) #display
#saving img imwrite
cv2.imwrite("Duplicate.jpeg", img)
#converting to gray scale 
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("image2",gray_img)

#thresholding
thresImg = cv2.threshold(gray_img,170,445,cv2.THRESH_BINARY_INV)[1]
cv2.imshow("image3",thresImg)

cv2.waitKey(0)
cv2.destroyAllWindows()