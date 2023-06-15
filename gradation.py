"""
1.ぼかし

参考URL:
http://advance-work.com/109/#:~:text=Python%E3%81%A7%E3%81%BC%E3%81%8B%E3%81%97%E7%94%BB%E5%83%8F%E5%87%A6%E7%90%86%201%20%E7%92%B0%E5%A2%83%20Python%203.6.5%20import%20matplotlib.pyplot%20as,%E3%83%94%E3%82%AF%E3%82%BB%E3%83%AB%E6%AF%8E%E3%81%AERGB%E5%80%A4%E3%82%92%E7%B8%A6%E3%83%BB%E6%A8%AA%E3%81%AE%E4%BA%8C%E6%AC%A1%E5%85%83%E9%85%8D%E5%88%97%E3%81%A8%E3%81%97%E3%81%A6%E6%A0%BC%E7%B4%8D%20...%204%20%E3%81%BC%E3%81%8B%E3%81%97%E7%94%BB%E5%83%8F%E5%87%A6%E7%90%86%E7%B5%90%E6%9E%9C%20%E3%82%AA%E3%83%AA%E3%82%B8%E3%83%8A%E3%83%AB%E7%94%BB%E5%83%8F%20%E3%81%BC%E3%81%8B%E3%81%9710%EF%BC%88%E3%83%95%E3%82%A3%E3%83%AB%E3%82%BF%E3%82%B5%E3%82%A4%E3%82%BA10%EF%BC%89%20%E3%81%BC%E3%81%8B%E3%81%9720%20
"""
import numpy as np
from PIL import Image

img = Image.open('./image/businessman.jpg')
width, height = img.size

# この数値を変更してぼかしの度合いを変更
filter_size = 10
out = Image.new('RGB', (width - filter_size, height - filter_size))

img_pixels = []
for y in range(height):
    row = []
    for x in range(width):
        row.append(img.getpixel((x, y)))
    # height毎に二次元配列としてappend
    img_pixels.append(row)
# numpyのarrayに変換
img_pixels = np.array(img_pixels)

for y in range(height - filter_size):
    for x in range(width - filter_size):
        # 縦、横 filter_size(pixel)分、RGB情報取得
        partial_img = img_pixels[y:y + filter_size, x:x + filter_size]
        # 行をfilter_sizeの二乗、列を3(R/G/B)に変換
        color_array = partial_img.reshape(filter_size ** 2, 3)
        # RGB平均値を算出
        mean_r, mean_g, mean_b = color_array.mean(axis=0)
        # 算出されたRGB情報を該当ピクセルに設定
        out.putpixel((x, y), (int(mean_r), int(mean_g), int(mean_b)))

out.show()
# 画像比較用にfilter_sizeをファイル名に入れておく
out.save('image/bokashi_{0}.jpg'.format(filter_size))
