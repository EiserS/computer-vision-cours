import cv2
import numpy
import imutils

img = cv2.imread(r'assets/phone.jpg')

img = imutils.resize(image=img, width=800)
# cv2.imshow('img', img)

gray = cv2.cvtColor(src=img.copy(), code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)

blur = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=100)
# cv2.imshow('blur', blur)

thresh = cv2.threshold(src=blur, thresh=200, maxval=255, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('threshold', thresh)

contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
print(f'[INFO] Liczba wszystkich konturów: {len(contours)}')

# for i in range(len(contours)):
#     img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[i]], contourIdx=-1, color=(0, 255, 0), thickness=2)
#     cv2.imshow('image contour', img_cnt)
#     cv2.waitKey(0)

max_area = 0

for idx, contour in enumerate(contours):
    area = cv2.contourArea(contour=contour, oriented=True)
    if area < max_area:
        max_area = area
        idx_flag_area = idx
print(f'[INFO] Indeks konturu o największym polu: {idx_flag_area}\nPole: {max_area}')


img_cnt_max_area = cv2.drawContours(image=img.copy(), contours=[contours[idx_flag_area]], contourIdx=-1,
                                    color=(255, 255, 0), thickness=2)
cv2.imshow('max_area', img_cnt_max_area)

cv2.waitKey(0)
