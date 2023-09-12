import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
st.write('Start!!')

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)


left_column, right_column = st.columns(2)
button = left_column.button('→カラムに文字を表示')
if button:
    right_column.write('ここは→カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容')


option = st.text_input('あなたの趣味は？')
st.write('あなたの趣味は', option, 'です。')

condicion = st.slider('あなたの今の調子は', 0, 10, 5)
st.write(condicion)
