"""
5.ノイズ付与

参考：
https://www.higashisalary.com/entry/cv2-pic-noise
"""
import shutil

import cv2
import numpy as np

image = './image/businessman.jpg'
noize_image = './image/noize.jpg'

# 画像をコピー
shutil.copy(image, noize_image)

img = cv2.imread(noize_image)

# ベース画像の読み込み
img = cv2.imread(noize_image, cv2.IMREAD_GRAYSCALE)
h, w = img.shape[:2]

# ノイズ画像の作成
# ノイズの濃さを変更
noise_level = 150
noise = np.random.randint(0, noise_level, (h, w))

# 画像にノイズを足す
img = img + noise

# 画像を保存
cv2.imwrite(noize_image, img)
