import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門（インタラクティブなウィジェット編）')

st.write('・チェックボックスにチェックを入れたら、画像を表示する')
"""
```python
if st.checkbox('Show Image'):
    img = Image.open('DSC02300.JPG')
    st.image(img, caption='fish', use_column_width=True)
```
"""
st.write('Display Image')

if st.checkbox('Show Image'):
    img = Image.open('DSC02300.JPG')
    st.image(img, caption='fish', use_column_width=True)

st.write('・"st.selectbox"で、セレクトボックスに選択肢を表示する')
"""
```python
option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'
```
"""
option = st.selectbox(
    'あなたが好きな数字を教えて下さい。',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'

st.write('・"st.text_input"で、テキストボックスを表示する')
"""
```python
text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味は、', text, 'です。'
```
"""
text = st.text_input('あなたの趣味を教えて下さい。')
'あなたの趣味は、', text, 'です。'

st.write('・"st.slider"で、スライドバー入力を表示する')
"""
```python
condition = st.slider('あなたの今の調子は？', 0, 10, 5)
'コンディション', condition
```
"""
condition = st.slider('あなたの今の調子は？', 0, 10, 5)
'コンディション', condition
