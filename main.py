import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
})

st.write('"write"には"高さ"と"幅"の引数が用意されていない')
"""
```python
st.write(df)
```
"""
st.write(df)

st.write('"dataframe"には"高さ"と"幅"の引数が用意されている')
"""
```python
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)
```
"""
st.dataframe(df.style.highlight_max(axis=0), width=100, height=100)

st.write('"dataframe"には"highlight"がある。列なら"0"を、行なら"1"を引数に指定してハイライトを付ける')
"""
```python
st.dataframe(df.style.highlight_max(axis=0))
```
"""
st.dataframe(df.style.highlight_max(axis=0))

st.write('"st.table"はソートができない。ただ表を表示させたいだけの時に使用する')
"""
```python
st.table(df.style.highlight_max(axis=0))
```
"""
st.table(df.style.highlight_max(axis=0))

st.write('"""（ダブルコーテーション）を三つ重ねる事でマークダウンやコードをappに載せる事ができる')
"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
```
"""
# -----------------------------------------------------------------------------------------------------------

"""
## グラフの表示
"""
st.write('新しくデータフレームを用意する')
"""
```python
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
```
"""
df2 = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.write('"st.line_chart()"で、データのグラフを作成する事ができる')
"""
```python
st.line_chart(df2)
```
"""
st.line_chart(df2)

st.write('"area_chart()"で表示すると、データの下部分のエリアを塗りつぶしてくれる')
"""
```python
st.area_chart(df2)
```
"""
st.area_chart(df2)

st.write('"st.bar_chart()"で棒グラフを作成する事ができる')
"""
```python
st.bar_chart(df2)
```
"""
st.bar_chart(df2)

# -----------------------------------------------------------------------------------------------------------

"""
## マップへの表示
"""
st.write('新しくデータフレームを用意する。（今回は新宿周辺の緯度と経度）')
"""
```python
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)
```
"""
df3 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.write('"st.map()"でマップ上にグラフをプロットしてくれる')
"""
```python
st.map(df3)
```
"""
st.map(df3)

# -----------------------------------------------------------------------------------------------------------

"""
## 画像の表示
"""

st.write('まず、"Image.open()"で画像を取り込み、"img"変数に入れる（別ファイルにある場合は"DSC02300.JPG"の部分にファイルの格納先を入れる）')
"""
```python
img = Image.open('DSC02300.JPG')
```
"""

st.write('次に、"st.image"でweb上に画像を表示する。（"caption"で画像の名前を付け、"use_column_width=True"で画像の大きさを全表示にする）')
"""
```python
st.image(img, caption='fish', use_column_width=True)
```
"""

st.write('Display Image')
img = Image.open('DSC02300.JPG')
st.image(img, caption='fish', use_column_width=True)