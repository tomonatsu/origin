import streamlit as st
import numpy as np
import pandas as pd
import time 
from PIL import Image


# pip install streamlit 
# pip install jupyter
# でpcにインストール
# streamlit run main.py
#jupyter labで起動

st.title('自己紹介')

st.write('私は山田　花子')
st.write('エアギターが得意だよ')
# df = pd.DataFrame({
#     '1列目':[1,2,3,4],
#      '2列目':[10,20,30,40]
# })

# これでも表は表示できる
# st.write(df)
# axis=1は行
# st.dataframe(df.style.highlight_max(axis=1))
# 動的な表
# st.dataframe(df.style.highlight_max(axis=0))

# 静的な表
# st.table(df.style.highlight_max(axis=0))


# マークダウンと呼ばれる
# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """

# 折れ線グラフ
# 縦に20、横に3の行列を作成
# 値はランダムで正規分布にのっとって生成される？規則性
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a','b','c']
# )

# これをプロットすると
# st.line_chart(df)
# 折れ線より下を縫ってくれる
# st.area_chart(df)
# 棒グラフ
# st.bar_chart(df)

# 緯度経度でマップ表示
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )
# st.map(df)

#画像の表示
# use_column_widthで画面のサイズに合わせて表示してくれる
# checkboxでチェックボックスを表示　戻り値はboolean
# if st.checkbox("とっておきのエアギターを見る"):
#     img = Image.open('nana.JPG')
#     st.image(img, caption='nattyan', use_column_width=True)

# selectboxでセレクトボックスを表示
# 戻り値を変数に代入可能
# option = st.selectbox(
#     'あなたが好きな数字を教えてください',
#     list(range(1,10))    
# )
# 'なっちゃんの好きな数字は、', option,'です。'

# text_inputで1行のテキストエリアを表示
# text_areaで複数行のテキストエリアを表示
# text = st.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は、',text,'です。'

# sliderで横長のスライダーを表示
# condition = st.slider('あなたの今の調子は？',0,100,50)
# 'コンディション:',condition


# buttonでボタンを表示
# click = st.button('絶対に押さないでね')
# img = ''
# if click :
#     img = Image.open('nana.JPG')
#     st.image(img, caption='nattyan', use_column_width=True)
#     img.close

# sidebarでサイドにに表示
# text = st.sidebar.text_input('趣味を入力してください')
# '趣味：',text
# slider = st.sidebar.slider('調子',0,100,50)
# 'コンディション：',slider

# 画面をカラム2つに分割
# left_column, right_column = st.columns(2)
# button = left_column.button('お気に入りの一枚を表示')
# img = Image.open('nana.JPG')
# if button:
#     right_column.image(img, caption='nattyan', use_column_width=True)
# buttonClose = left_column.button('お気に入りの一枚を閉じる')
# if buttonClose:
#     img.close()

# 問い合わせフォームを表示
expander = st.expander('エアギターはどれくらい練習したんですか？')
expander.write('ぶっつけ本番です')

# プログレスバーの表示
# latest_iteration = st.empty()
# bar = st.progress(0)
# for i in range(100):
#     # f(fストリング)で値を文字列に書き込める
#     latest_iteration.text(f'Iteration {i + 1}')
#     bar.progress(i + 1)
#     time.sleep(0.1)

'Done!!!!!!!'