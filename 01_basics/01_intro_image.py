import cv2

print(cv2.__version__)

image = cv2.imread(filename=r'D:\prepos\01_basics\assets\gscreenshot.png')

cv2.imshow(winname='nazwaokna',mat=image)
cv2.waitKey(delay=0)