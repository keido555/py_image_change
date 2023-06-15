"""
3.色調変更

参考：
https://tat-pytone.hatenablog.com/entry/2019/03/06/192135
https://qiita.com/sitar-harmonics/items/d864728e002f94872d97
"""
import shutil

import cv2
import numpy as np

image = './image/businessman.jpg'
color_change_image = './image/color_change.jpg'

# 画像をコピー
shutil.copy(image, color_change_image)

# 画像を読み出しオブジェクトimgに代入
# img = cv2.imread(color_change_image)

# cv2.imreadで読み出したカラー画像は 高さ×幅×色(3要素)の3次元のndarrayとなっている
# 色3要素はB(青)、G(緑)、R(赤)それぞれの輝度を示す
# 全ての画素についてBの輝度を0としている(青が抜ける)
# img[:, :, 0] = 0

# cv2.imshow("B=0", img)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# HSV H(色相)の変更
def changedH(bgr_img, shift):
    # BGR->HSV
    hsvimage = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV_FULL)
    hi = hsvimage[:, :, 0].astype(np.int32)
    if shift < 0:
        nhi = hi.flatten()
        for px in nhi:
            if px < 0:
                px = 255 - px
        nhi = nhi.reshape(hsvimage.shape[:2])
        hi = nhi.astype(np.uint8)
    chimg = (hi + shift) % 255
    hsvimage[:, :, 0] = chimg
    hsv8 = hsvimage.astype(np.uint8)
    # HSV->BGR
    return cv2.cvtColor(hsv8, cv2.COLOR_HSV2BGR_FULL)


# HSV S(彩度),V(明度)の変更
def changedSV(bgr_img, alpha, beta, color_idx):
    # BGR->HSV
    hsvimage = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2HSV_FULL)
    hsvf = hsvimage.astype(np.float32)
    hsvf[:, :, color_idx] = np.clip(hsvf[:, :, 1] * alpha + beta, 0, 255)
    hsv8 = hsvf.astype(np.uint8)
    return cv2.cvtColor(hsv8, cv2.COLOR_HSV2BGR_FULL)


# HSV S(彩度)の変更
def changedS(bgr_img, alpha, beta):
    return changedSV(bgr_img, alpha, beta, 1)


# HSV V(明度)の変更
def changedV(bgr_img, alpha, beta):
    return changedSV(bgr_img, alpha, beta, 2)


bgr_img = cv2.imread(color_change_image, cv2.IMREAD_COLOR)


# HSV S(彩度)の変更
image_h1 = changedH(bgr_img, 85)
image_h2 = changedH(bgr_img, -85)

# HSV S(彩度)の変更
image_s1 = changedS(bgr_img, 2.0, -20)
image_s2 = changedS(bgr_img, 1 / 2, 20)

# HSV V(明度)の変更
image_v1 = changedV(bgr_img, 1.8, 20)
image_v2 = changedV(bgr_img, 1 / 2, -50)

# 画像表示
# cv2.imshow('original', bgr_img)
# cv2.imshow('HSV h1', image_h1)
# cv2.imshow('HSV h2', image_h2)
# cv2.imshow('HSV s1', image_s1)
# cv2.imshow('HSV s2', image_s2)
# cv2.imshow('HSV v1', image_v1)
# cv2.imshow('HSV v2', image_v2)
# cv2.waitKey(0)

# 画像の保存
cv2.imwrite(color_change_image, image_h1)
