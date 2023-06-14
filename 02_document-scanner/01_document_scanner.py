import numpy as np
from numpy.linalg import norm
import imutils
import cv2
import skimage

img = cv2.imread(r'assets/paragon_1.jpg')
# cv2.imshow('show', img)
# print(img.shape)

org_img = img.copy()
ratio = img.shape[0] / 500.0

img = imutils.resize(image=img, height=500)
# print(img)
# cv2.imshow('resized', img)

gray_img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray_img)

gaussingBlur = cv2.GaussianBlur(src=gray_img, ksize=(5, 5), sigmaX=0)

edges = cv2.Canny(image=gaussingBlur, threshold1=70, threshold2=200)
# cv2.imshow('edges', edges)

contours = cv2.findContours(image=edges.copy(), mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
# print(f'Liczba wszystkich wyszukanych punktów (kontur): {len(contours)}')
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:5]

# for contour in contours:
    # print(len(contour))

cnt1 = cv2.drawContours(img.copy(), contours[0], -1, (0, 255, 0), 2)
# cv2.imshow('cnt', cnt1)

cnt2 = cv2.drawContours(img.copy(), contours[1], -1, (0, 255, 0), 2)
# cv2.imshow('cv2', cnt2)

cnt3 = cv2.drawContours(img.copy(), contours[2], -1, (0, 255, 0), 2)
# cv2.imshow('cnt3', cnt3)

cnt4 = cv2.drawContours(img.copy(), contours[3], -1, (0, 255, 0), 2)
# cv2.imshow('cnt3', cnt4)

cnt5 = cv2.drawContours(img.copy(), contours[4], -1, (0, 255, 0), 2)
# cv2.imshow('cnt3', cnt5)

for contour in contours:
    # print('Sprawdzanie...')
    # obliczymy obwód każdej wyszukanej figury
    perimeter = cv2.arcLength(curve=contour, closed=True)

    # przybliżenie krzywej wielokąta (w naszym przypadku prostokąt) z określoną precyzją
    approx = cv2.approxPolyDP(curve=contour, epsilon=0.02 * perimeter, closed=True)

    if len(approx) == 4:
        screen_contour = approx
        break

# print(screen_contour)

# wyświetlenie znalezionych wierzchołków

w_contour = cv2.drawContours(img, contours=screen_contour, contourIdx=-1, color=(0, 255, 0), thickness=15)
# cv2.imshow('corner', w_contour)

points = screen_contour.reshape(4, 2)
points = points * ratio
# print(points)

rectangle = np.zeros((4, 2), dtype='float32')
# print(rectangle)

total = points.sum(axis=1)

rectangle[0] = points[np.argmin(total)]
rectangle[2] = points[np.argmax(total)]
# print(rectangle)

difference = np.diff(points, axis=1)
rectangle[1] = points[np.argmin(difference)]
rectangle[3] = points[np.argmax(difference)]
# print(rectangle)

(a, b, c, d) = rectangle

width1 = norm(c - d)
width2 = norm(b - a)
max_width = max(int(width1), int(width2))

height1 = norm(b - c)
height2 = norm(a - d)
max_height = max(int(height1), int(height2))

# print(f'max_width: {max_width}')
# print(f'max_height: {max_height}')

vertices = np.array([
    [0, 0],
    [max_width - 1, 0],
    [max_width - 1, max_height - 1],
    [0, max_height - 1]
], dtype='float32')

# macierz transformacji 3x3
M = cv2.getPerspectiveTransform(rectangle, vertices)
# print(M)

# przekształcenie dokumentu do obrazu
out = cv2.warpPerspective(src=org_img, M=M, dsize=(max_width, max_height))
# cv2.imshow('out', out)

# konwersja do skali szarości
out = cv2.cvtColor(out, cv2.COLOR_BGR2GRAY)

# obliczenie maski progowej na podstawie sąsiedztwa pikseli
T = skimage.filters.threshold_local(image=out, block_size=11, offset=10, method='gaussian')
out = (out > T).astype('uint8') * 255
cv2.imshow('out2', out)

cv2.waitKey(0)
