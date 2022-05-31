import streamlit as st
import pandas as pd
import plotly.express as px
import chart_studio.plotly as py
import matplotlib.pyplot as plt
import seaborn as sns

def run_chart() :
    st.header('Diamonds_Chart')

    # dataset 불러오기
    df = sns.load_dataset("diamonds")

    # 필요한 컬럼만 사용하기 위한 작업
    df_columns = df.columns[ : 6]

    # selectbox를 이용해 컬럼 선택
    my_choice = st.selectbox('Choice the Columns', df_columns)

    # 라디오 버튼을 이용한 차트 그래프 표현하기

    carat_ = plt.figure()
    px.scatter(df, x="carat", y="depth", color="cut")
    py.(carat_)
