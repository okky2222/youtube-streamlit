import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門（レイアウトを整える）')


st.write('・"st.sidebar.~"で、サイドバーに記入欄等を表示する')
"""
```python
st.sidebar.write('サイドバーを使用した表示')
text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 10, 5)

'あなたの趣味は、', text, 'です。'
'コンディション', condition
```
"""
st.sidebar.write('サイドバーを使用した表示')
text = st.sidebar.text_input('あなたの趣味を教えて下さい。')
condition = st.sidebar.slider('あなたの今の調子は？', 0, 10, 5)

'あなたの趣味は、', text, 'です。'
'コンディション', condition

# -----------------------------------------------------------------------------------------------

