import cv2 as cv


img = cv.imread('src/lara.jpg')
cv.imshow('lara', img)

cv.waitKey(0)

cv.destroyAllWindows()