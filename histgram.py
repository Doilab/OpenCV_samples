#!/usr/bin/env python
# coding: utf-8

import cv2
import numpy as np

def __main():
    img_bgr = cv2.imread('./sample_data/fruits.jpg')
    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    
    img_bgr_dst = getHistgram(img_bgr)
    img_hsv_dst = getHistgram(img_hsv)

    cv2.imshow('HistGramBGR', img_bgr_dst)
    cv2.imshow('HistGramHSV', img_hsv_dst)

    cv2.imwrite("./output_data/HistGram-BGR.jpg", img_bgr_dst)
    cv2.imwrite("./output_data/HistGram-HSV.jpg", img_hsv_dst)

    #キー入力待機
    cv2.waitKey(0)

    #表示ウィンドウを削除
    cv2.destroyAllWindow()

def getResize(src):
    global shotSize
    basePixSize = 640 # 縦横で大きい辺の変更したいサイズ
    height = src.shape[0]
    width = src.shape[1]

    largeSize = max(height, width) # 大きい方の辺のサイズ
    resizeRate = basePixSize / largeSize # 変更比率を計算
    shotSize = min(height, width) * resizeRate
    dst = cv2.resize(src, (int(width * resizeRate), int(height * resizeRate)))

    return dst

def getHistgram(img):
    img = getResize(img)
    channel = 3
    upper = 70
    size = np.array([upper * 3, 256, channel])
    blackColor = np.array([0, 0, 0])
    hist = np.full(size, blackColor, dtype = np.uint8)
    height, width, _ = hist.shape

    for j in range(channel):
        bgrHist = cv2.calcHist(images=[img],channels=[j], mask= None, histSize=[256], ranges=[0, 256])
        cv2.normalize(src=bgrHist, dst=bgrHist, alpha = 0, beta = upper, norm_type=cv2.NORM_MINMAX)
        color = [0, 0, 0]
        color[j] = 255
        baseLine = j * upper + upper
        
        for i in range(0, 255):
            vertical = bgrHist[i]
            cv2.line(hist, (i, baseLine), (i, baseLine - vertical), color)

    y = 10
    x = 10
    img[y: y + height, x: x + width] = hist
    return img

if __name__ == '__main__':
    print(cv2.__version__)
    shotSize = 0
    __main()
