import cv2 as cv
import numpy as np

#blank canvas
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('blank', blank)
#500,500 adalah lebar dan tinggi canvas angka 3 adalah rgb untuk bisa memberikan warna


#coloring canvas
blank[450:470, 20:40] = 255,0,0
cv.imshow('blue', blank)
#[:] inimemiliki arti menunjuk ke pixel
# 450 turun per pixel, 470 itu mulai 0 sampai ke 470, 20 mulai dari sisi kanan, 40 mulai dari 0 sisi kanan ke kiri


#draw rectangle
cv.rectangle(blank, (0,0), (255,255), (255,0,0), thickness=2)
cv.imshow('rectangle', blank)
#blank itu canvasnya (0,0) kordinat pertama (255,255) kordinat ke dua, (255,0,0) itu warna 
#thicness itu ketebalan, cv.FILLED buat mengisi atau -1


#draw a circle / lingkaran point, besar, warna,   ketebalan
cv.circle(blank, (122,122), 40, (0,0,255), thickness=4)
cv.imshow('circle', blank)


#draw a line
cv.line(blank, (0,0), (255,255), (0,255,0), thickness=3)
cv.imshow('line', blank)


#text add
cv.putText(blank, 'hello world', (255,377), cv.FONT_HERSHEY_COMPLEX, 1.0, (255,0,0), thickness=1)
cv.imshow('text',blank)

cv.waitKey(0)