import cv2 as cv

capture = cv.VideoCapture('src/vlara.mp4')

while True:
    isTrue, frame = capture.read()
    if not isTrue:
        break
    cv.imshow('video lara', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break


capture.release()

cv.destroyAllWindows()
