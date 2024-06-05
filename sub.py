import streamlit as st
import time 

st.title('自己紹介')

st.write('私は山田　花子')
st.write('エアギターが得意だよ')


# 問い合わせフォームを表示
expander = st.expander('エアギターはどれくらい練習したんですか？')
expander.write('ぶっつけ本番です')

# プログレスバーの表示
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    # f(fストリング)で値を文字列に書き込める
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!!!'