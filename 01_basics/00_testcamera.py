import cv2

vid = cv2.VideoCapture(0)

while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    img = frame
    # cv2.imshow('orginal2_img', img)

    grey = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
    # cv2.imshow('grey', grey)

    thresh = cv2.threshold(src=grey, thresh=250, maxval=255, type=cv2.THRESH_BINARY)[1]
    # cv2.imshow('thresh', thresh)

    contours = cv2.findContours(image=thresh, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)[0]
    # print(len(contours))

    # for i in range(len(contours)):
    # img_cnt = cv2.drawContours(image=img.copy(), contours=[contours[4]], contourIdx=-1, color=(0, 255, 0), thickness=2)
    # cv2.imshow('image contour', img_cnt)
    #    cv2.waitKey(0)
    max_area = 0
    idx_flag_area = -1
    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour=contour, oriented=True)
        if area > max_area:
            max_area = area
            idx_flag_area = idx
    print(f'[INFO] Indeks konturu o największym polu: {idx_flag_area}\nPole: {max_area}')

    img_cnt_max_area = cv2.drawContours(image=img.copy(), contours=[contours[idx_flag_area]],
                                        contourIdx=-1, color=(0, 255, 0), thickness=2)
    # cv2.imshow('img_cnt_max_area', img_cnt_max_area)

    # Display the resulting frame
    cv2.imshow('frame', img_cnt_max_area)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
