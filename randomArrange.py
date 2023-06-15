"""
6.ランダム配置
"""
import random
import shutil

import cv2

image = './image/businessman.jpg'
random_image = './image/random.jpg'
imgae_paste1 = "./image/quita.png"
imgae_paste2 = "./image/staff.png"
imgae_paste3 = "./image/icon.png"

# 画像をコピー
shutil.copy(image, random_image)

# 背景画像の設定
background_image = cv2.imread(random_image)

# 貼り付ける画像のリスト
images = [imgae_paste1, imgae_paste2, imgae_paste3]

# 背景画像のサイズを取得
bg_height, bg_width, _ = background_image.shape

# 貼り付ける画像の最大幅と最大高さ
max_width = 256
max_height = 256

# 背景画像に対して複数の画像を貼り付ける
for image_path in images:
    # 画像の読み込み
    image = cv2.imread(image_path)

    # 画像のリサイズ
    # 幅をランダムに設定
    width = random.randint(50, max_width)
    # 高さをランダムに設定
    height = random.randint(50, max_height)
    image = cv2.resize(image, (width, height))

    # 貼り付け位置のランダムな座標を計算
    x = random.randint(0, bg_width - width)
    y = random.randint(0, bg_height - height)

    # 背景画像に画像を貼り付ける
    background_image[y: y + height, x: x + width] = image

# 画像の表示
# cv2.imshow('Composite Image', background_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 画像の保存
cv2.imwrite(random_image, background_image)
