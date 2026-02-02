import cv2 as cv

larav = cv.VideoCapture('src/vlara.mp4')


#function untuk mengubah video yang awal nya besar menjadi mengecil
def rescalevid(frame, lebar = 300): #300 itu akan menjadi lebaran video nya nanti entah videonya berapa pun
    hight, width = frame.shape[:2]
    rasio = lebar / width
    tinggi = int(hight * rasio)
    return cv.resize(frame, (lebar, tinggi), interpolation = cv.INTER_AREA)

while True:
    isTrue, frame = larav.read()
    if not isTrue:
        break
    play = rescalevid(frame)
    cv.imshow('original', frame)
    cv.imshow('video rescale', play)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

larav.release()
cv.destroyAllWindows()