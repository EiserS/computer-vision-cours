import numpy as np
import cv2
from mss import mss

# Define the bounding box for screen capture
bounding_box = {'top': 0, 'left': 0, 'width': 1720, 'height': 1440}

# Initialize MSS
sct = mss()

# Define the desired window size
window_width = 800
window_height = 600

while True:
    # Capture the screen
    sct_img = sct.grab(bounding_box)

    # Resize the captured image
    resized_img = cv2.resize(np.array(sct_img), (window_width, window_height))

    gray = cv2.cvtColor(src=resized_img, code=cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey', gray)

    blur = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=1)
    cv2.imshow('blur', blur)

    edges = cv2.Canny(image=blur, threshold1=1, threshold2=255)
    cv2.imshow('edges', edges)

    contours, _ = cv2.findContours(image=edges, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        cv2.drawContours(image=resized_img, contours=[contour], contourIdx=-1, color=(0, 255, 0), thickness=2)

    cv2.imshow('image contour', resized_img)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
