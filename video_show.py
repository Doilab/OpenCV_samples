import sys
import cv2

# ビデオファイルを開く
cap = cv2.VideoCapture('./sample_data/vtest.avi')
# ビデオファイルが開けなかったとき
if not cap.isOpened():
    print('Can not open video file')
    sys.exit()

# ループ開始
while True:
    # 1フレーム読み込み
    ret, img = cap.read()
    # ビデオ終端でフレームが読み込めなくなったら中断
    if not ret:
        break
    # 1フレーム表示
    cv2.imshow('win_img', img)
    # キー入力待機(30ms)．Escキーで中断
    if cv2.waitKey(30) == 27:
        break
    
cv2.destroyAllWindows()
# ビデオファイルを閉じる
cap.release()
