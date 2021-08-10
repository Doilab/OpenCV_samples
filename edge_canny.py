import cv2
src = cv2.imread('./sample_data/squirrel_cls.jpg',flags=cv2.IMREAD_COLOR)

#Cannyエッジ検出
dst =cv2.Canny(src,50,200)

cv2.imshow('win_src',src)
cv2.imshow('win_dst',dst)

#出力画像の保存
cv2.imwrite('./output_data/dst_squirrel_cls.jpg',dst)

cv2.waitKey(0)

#すべての表示ウィンドウを削除
cv2.destroyWindow()