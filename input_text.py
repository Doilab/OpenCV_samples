import cv2

img = cv2.imread('./sample_data/cat.jpg')

cv2.putText(img,
            text='Name:Tom',
            org=(10, 30),
            fontFace=cv2.FONT_HERSHEY_SIMPLEX,
            fontScale=0.8,
            color=(255, 0, 0),
            thickness=2,
            lineType=cv2.LINE_4)

cv2.imshow('./sample_after.png', img)

cv2.waitKey(0)
