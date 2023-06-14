import cv2

vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    img = frame
    cv2.imshow('orginal2_img', img)

    gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey', gray)

    blur = cv2.GaussianBlur(src=gray, ksize=(5, 5), sigmaX=50)
    cv2.imshow('blur', blur)

    edges = cv2.Canny(image=blur, threshold1=70, threshold2=200)
    cv2.imshow('edges',edges)

    # thresh = cv2.threshold(src=blur, thresh=180, maxval=255, type=cv2.THRESH_BINARY)[1]
    # cv2.imshow('thresh', thresh)

    contours = cv2.findContours(image=edges, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
    print(len(contours))

    # for i in range(len(contours)):
    #     img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[i]], contourIdx=-1, color=(0, 255, 0), thickness=2)
    #     cv2.imshow('image contour', img_cnt)
    #     cv2.waitKey(0)
    max_area = 0
    idx_area = -1
    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour=contour, oriented=True)
        if area > max_area:
            max_area = area
            idx_area = idx
    print(f'[INFO] Indeks konturu o największym polu: {idx_area}\nPole: {max_area}')
    #
    img_cnt_max_area = cv2.drawContours(image=img.copy(), contours=[contours[idx_area]],
                                        contourIdx=-1, color=(0, 255, 0), thickness=2)
    # cv2.imshow('img_cnt_max_area', img_cnt_max_area)

    # Display the resulting frame
    cv2.imshow('frame_thresh', edges)
    cv2.imshow('frame', img_cnt_max_area)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
