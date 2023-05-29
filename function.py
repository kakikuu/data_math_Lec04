from PIL import Image
import numpy as np


def ext_mean_rgb(file_path):
    # グレースケールである場合にもRGB空間に変換する
    img = np.array(Image.open(file_path).convert('RGB')).reshape(-1, 3)
    rgb_mean = np.array(
        [np.mean(img[:, 0]), np.mean(img[:, 1]), np.mean(img[:, 2])])
    return rgb_mean


def gen_color_vec(rgbvec):
    colorvec = np.array([])
    palette = np.array(
        [
            [255, 0, 0],  # 赤
            [255, 102, 0],  # 橙
            [255, 255, 0],  # 黄
            [0, 128, 0],  # 緑
            [0, 0, 255],  # 青
            [128, 0, 128],  # 紫
            [255, 0, 255],  # ピンク
            [255, 255, 255],  # 白
            [128, 128, 128],  # グレー
            [0, 0, 0]  # 黒
        ]
    )

    for col in palette:
        colorvec = colorvec = np.append(colorvec, np.linalg.norm(col - rgbvec))
    colorvec = 1-colorvec/np.linalg.norm(colorvec, np.inf)
    return colorvec.reshape(-1, 1)


def rgb_to_word(A, file_path):
    x = gen_color_vec(ext_mean_rgb(file_path))
    result = np.dot(A, x)
    max_index = np.argmax(result.reshape(-1, 1))
    impreword = ["明るい", "暗い", "かわいい", "悲しい", "情熱", "冷静", "自然"]
    return impreword[max_index]
