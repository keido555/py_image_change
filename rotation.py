"""
2.90度回転

参考：
https://note.nkmk.me/python-pillow-rotate/
"""
import shutil

import cv2

image = './image/businessman.jpg'
rotate_image = './image/rotate_90.jpg'

# 画像をコピー
shutil.copy(image, rotate_image)

# コピーした画像の角度を変更
img = cv2.imread(rotate_image)

img_rotate_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite(rotate_image, img_rotate_90_clockwise)
