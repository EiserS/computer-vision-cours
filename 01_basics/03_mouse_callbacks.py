import this

import cv2


def get_position(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f'x={x}, y={y}')


def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(
            img=img,
            center=(x, y),
            radius=50,
            color=(0, 255, 0),
            thickness=2
        )


# def draw_square(event, x, y, flags, param):
#     global x1, x2, y1, y2, img
#
#     if event == cv2.EVENT_LBUTTONDBLCLK:
#         x1 = x
#         y1 = y
#     if event == cv2.EVENT_LBUTTONUP:
#         x2 = x
#         y2 = y
#     if x1 is not None and x2 is not None:
#         cv2.rectangle(
#             img=img,
#             pt1=(x1, y1),
#             pt2=(x2, y2),
#             color=(0, 255, 0),
#             thickness=2,
#             lineType=cv2.LINE_8,
#             shift=0
#         )


img = cv2.imread(r'assets\gscreenshot.png')

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    if cv2.waitKey(1) == 27:
        break
