"""
4.コントラスト付与

参考：
https://qiita.com/isso_w/items/a6f4ffa6c788b64fc6ec#:~:text=%E7%94%BB%E5%83%8F%E3%81%AE%E3%82%B3%E3%83%B3%E3%83%88%E3%83%A9%E3%82%B9%E3%83%88%E3%82%92%E8%AA%BF%E6%95%B4%E3%81%99%E3%82%8BPython%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E3%82%92%E6%9B%B8%E3%81%8D%E3%81%BE%E3%81%97%E3%81%9F%E3%80%82%20%E3%82%B3%E3%83%BC%E3%83%89%20import%20cv2%20import%20numpy%20as%20np,%23float%E5%9E%8B%E3%81%AB%E5%A4%89%E6%8F%9B%20newImage%20%3D%20np.array%28img%2C%20dtype%20%3D%20%27float64%27%29%20%23%E3%82%B3%E3%83%B3%E3%83%88%E3%83%A9%E3%82%B9%E3%83%88%E8%AA%BF%E6%95%B4%E3%80%82
"""
import shutil

import cv2
import numpy as np

image = './image/businessman.jpg'
contrast_image = './image/contrast.jpg'

# 画像をコピー
shutil.copy(image, contrast_image)

img = cv2.imread(contrast_image)

# コントラスト
contrast = 128

# コントラスト調整ファクター
factor = (259 * (contrast + 255)) / (255 * (259 - contrast))

# float型に変換
newImage = np.array(img, dtype='float64')

# コントラスト調整。（0以下 or 255以上）はクリッピング
newImage = np.clip((newImage[:, :, :] - 128) * factor + 128, 0, 255)

# int型に戻す
newImage = np.array(newImage, dtype='uint8')

# 出力
cv2.imwrite(contrast_image, newImage)
