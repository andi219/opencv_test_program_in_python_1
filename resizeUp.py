import cv2 as cv
img = cv.imread('src/koopa.png')


#resize up
hight, width = img.shape[:2]
lebar = 580
rasio = lebar / width
tinggibaru = int(hight * rasio)
resizedd = cv.resize(img, (lebar,tinggibaru), interpolation=cv.INTER_CUBIC)
resizeaa = cv.resize(img, (lebar,tinggibaru), interpolation=cv.INTER_NEAREST)

cv.imshow('kasar(nearest)',resizeaa)
cv.imshow('halus(area)', resizedd)

cv.waitKey(0)
cv.destroyAllWindows()
