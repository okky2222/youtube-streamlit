import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門（レイアウトを整える）')


st.write('・"st.columns()"で、カラム分けできる')
"""
```python
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
```
"""
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')

# ---------------------------------------------------------------------------------------------

st.write('・"st.expander()"で、縮める文字欄を表示')
"""
```python
left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
```
"""
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')
