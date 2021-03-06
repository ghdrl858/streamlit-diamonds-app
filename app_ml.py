import streamlit as st
import seaborn as sns
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def run_ml():
    st.header('๐ ๏ธ Diamonds_ML')
    st.write('''##### โ๏ธ ์ธ๊ณต์ง๋ฅํ์ต์ํค๊ณ  ๊ทธ๋ํ๋ก ์ค์ ๊ฐ๊ณผ ์์ธก๊ฐ์ ๋น๊ตํ๋ ํ์ด์ง์๋๋ค.''')

    # colab์์ ์์ํ ๋ฐ์ดํฐ๋ฅผ pkl ํ์ผ๋ก ์ ์ฅํ์ฌ ์ฌ์ฉ ์ค๋นํ๊ธฐ
    df = sns.load_dataset("diamonds")
    cut_encoder = joblib.load('data/cut_encoder.pkl')
    color_encoder = joblib.load('data/color_encoder.pkl')
    clarity_encoder = joblib.load('data/clarity_encoder.pkl')
    model = joblib.load('data/model.pkl')\
    
    # cut, color, clarity๋ฅผ ์ธ์ฝ๋ฉ ์ํจ๊ฑฐ ์คํ์ํค๊ธฐ
    df['cut'] = cut_encoder.transform(df['cut'])
    df['color'] = color_encoder.transform(df['color'])
    df['clarity'] = clarity_encoder.transform(df['clarity'])

    # ์ปฌ๋ผ์ ์ ํํด์ ํด๋น ๊ฐ์ ํ์ธ
    column_list = st.multiselect('Choice Columns', df.columns[ : 6])
    if len(column_list) != 0 :
        st.dataframe(df[column_list])
    st.write("""***""")

    # ํ์ต ์ํจ ๋ชจ๋ธ๋ก ์์ธกํ๋ค.
    y_pred = model.predict(df.drop('price', axis = 1))

    # ์์ธก % ์ค๋ช ๋ฒํผ
    if st.button('์ธ๊ณต ์ง๋ฅ ์์ธก ๊ฒฐ๊ณผ') :
        st.write('''###### โ๏ธ 0.9806099673065828 ๋ก ์์ธก๊ฐ์ด ๊ฑฐ์ ์ค์ ๊ฐ๊ณผ ๊ทผ์ ํ๋ค๋ ๊ฒ์ ์๋ฏธํฉ๋๋ค.''')

    # ๋น๊ต ๊ทธ๋ํ ๊ทธ๋ฆฌ๊ธฐ - Scatter 1
    if st.button('Predict VS Actual_1 Chart') :
        st.write('''###### โ๏ธ x์ถ์๋ ํ์ต์ํจ ์์ธก๊ฐ์, y์ถ์๋ dataset์ ์๋ price๊ฐ์ ๋ฃ์ด์ ํํํ ๊ทธ๋ํ์๋๋ค.
            
###### โ๏ธ ์ค์ ์ ์์ธก์ด ๊ฑฐ์ ๋น์ทํ ์์ญ์ผ๋ก ์์นํ๋ ๊ทธ๋ํ์์ ๋ณผ ์ ์์ต๋๋ค.
            ''')
        fig1 = px.scatter(df, x = y_pred, y="price", title='predict vs actual')
        st.plotly_chart(fig1)

    # ๋น๊ต ๊ทธ๋ํ ๊ทธ๋ฆฌ๊ธฐ - Scatter 2
    if st.button('Predict VS Actual_2 Chart') :
        st.write('''###### โ๏ธ ์ ๊ทธ๋ํ์์ ์ถ๊ฐ๋ก cut ์์ญ์ ๋ฃ์ด์ ํด๋น ์์ญ์ ์ผ๋ง๋ ๋ฐ์ง๋์ด์๋์ง ํ์ธํ  ์ ์์ต๋๋ค.
            ''')
        fig2 = px.scatter(df, x = y_pred, y="price", title='predict vs actual', color='cut')
        st.plotly_chart(fig2)