import streamlit as st
from function import rgb_to_word
import numpy as np
from PIL import Image

st.title("画像から印象語を出力します！！")

img = st.file_uploader("画像ファイルをアップロードしてください", type='png')
if img:
    print(img)
    # file_path = "/content/drive/MyDrive/B2/math/img/tomato.jpg"
    A = np.array([[0.5, 1, 1, 1, 0, 0, 1, 1, 0, -1], [0, -1, -1, 0, 0.5, 0, -1, -1, 0.5, 1],
                  [0, 0.5, 0.5, 0, 0, 0, 1, 0, 0, 0,], [
        0, -1, -1, 0, 1, 0, -1, 0, 1, 1],
        [1, 1, 0.5, -1, -1, 0.5, 0, 0, 0, 0], [-1, -
                                               1, -1, 0.5, 1, 0, 0, 0.5, 0.5, 0.5],
        [0, 0.5, 0.5, 1, 0, 0, 0, 0, 0, 0, ]])
    result = rgb_to_word(A, img)
    image = np.array(Image.open(img))
    st.image(image, caption="アップロードされた画像", use_column_width=True)
    st.markdown(f"""
        選ばれた印象語は **「{result}」** です！！
    """)
