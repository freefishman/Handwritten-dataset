import cv2 as cv

src = cv.imread('09.jpg')
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
ret,binary = cv.threshold(gray, 0, 255,cv.THRESH_BINARY_INV|cv.THRESH_OTSU)
cv.imwrite('new09.jpg',binary)
