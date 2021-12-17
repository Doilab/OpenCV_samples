import cv2
import numpy as np


# 画像の読み込み + グレースケール化
img = cv2.imread('./sample_data/messi5.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

template = cv2.imread('./sample_data/messi_face.jpg')
template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# 処理対象画像に対して、テンプレート画像との類似度を算出する
res = cv2.matchTemplate(img_gray, template_gray, cv2.TM_CCOEFF_NORMED)

# 類似度の高い部分を検出する
threshold = 0.8
loc = np.where(res >= threshold)

# テンプレートマッチング画像の高さ、幅を取得する
h, w = template_gray.shape

# 検出した部分に赤枠をつける
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

# 画像の表示
cv2.imshow('messi_img', img)
cv2.imwrite('./output_data/detect_messi.jpg', img)

#キー入力待機
cv2.waitKey(0)

#表示ウィンドウを削除
cv2.destroyWindow('messi_img')
