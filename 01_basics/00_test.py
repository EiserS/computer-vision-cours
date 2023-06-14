import cv2

orginal_img = cv2.imread(filename=r'assets/gscreenshot.png')
img = orginal_img.copy()
# cv2.imshow('foto', img)

grey = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
cv2.imshow('grey', grey)

gauss = cv2.GaussianBlur(src=grey, ksize=(5, 5), sigmaX=0)



for i in range(250):
    thresh = cv2.threshold(src=grey, thresh=i, maxval=255, type=cv2.THRESH_BINARY)[1]
    cv2.putText(
        img=thresh,
        text='threshold: ' + str(i),
        org=(20, 40),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1.5,
        color=(0, 255, 0),
        thickness=2
    )
    cv2.imshow('thresh', thresh)
    cv2.waitKey(0)
# thresh = cv2             .threshold(src=grey, thresh=9, maxval=150, type=cv2.THRESH_BINARY)[1]
# cv2.imshow('thresh', thresh)

# thresh = cv2.threshold(src=grey, thresh=100, maxval=250, type=cv2.THRESH_BINARY)[1]
# contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
# print(len(contours))
# for i in range(len(contours)):
#     img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[i]], contourIdx=-1, color=(0, 0, 255), thickness=2)
#     cv2.imshow('contours', img_cnt)
#     cv2.waitKey(0)
cv2.waitKey(0)
