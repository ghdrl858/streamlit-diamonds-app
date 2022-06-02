import streamlit as st
import seaborn as sns
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def run_ml():
    st.header('Diamonds_ML')
    st.write('''##### ° 인공지능학습시키고 그래프로 실제값과 예측값을 비교하는 페이지입니다.''')

    # colab에서 작업한 데이터를 pkl 파일로 저장하여 사용 준비하기
    df = sns.load_dataset("diamonds")
    cut_encoder = joblib.load('data/cut_encoder.pkl')
    color_encoder = joblib.load('data/color_encoder.pkl')
    clarity_encoder = joblib.load('data/clarity_encoder.pkl')
    model = joblib.load('data/model.pkl')

    # cut, color, clarity를 인코딩 시킨거 학습시키기
    df['cut'] = cut_encoder.fit_transform(df['cut'])
    df['color'] = color_encoder.fit_transform(df['color'])
    df['clarity'] = clarity_encoder.fit_transform(df['clarity'])

    # 컬럼을 선택해서 해당 값을 확인
    column_list = st.multiselect('Choice Columns', df.columns[ : 6])
    if len(column_list) != 0 :
        st.dataframe(df[column_list])
    st.write("""***""")

    # 학습 시킨 모델로 예측한다.
    y_pred = model.predict(df.drop('price', axis = 1))

    # 예측 % 설명 버튼
    if st.button('인공 지능 예측 결과') :
        st.write('''###### ° 0.9806099673065828 로 예측값이 거의 실제값과 근접하다는 것을 의미합니다.''')

    # 비교 그래프 그리기 - Scatter 1
    if st.button('Predict VS Actual_1 Chart') :
        st.write('''###### ° x축에는 학습시킨 예측값을, y축에는 dataset에 있는 price값을 넣어서 표현한 그래프입니다.
            
###### ° 실제와 예측이 거의 비슷한 영역으로 상승하는 그래프임을 볼 수 있습니다.
            ''')
        fig1 = px.scatter(df, x = y_pred, y="price", title='predict vs actual')
        st.plotly_chart(fig1)

    # 비교 그래프 그리기 - Scatter 2
    if st.button('Predict VS Actual_2 Chart') :
        st.write('''###### ° 위 그래프에서 추가로 cut 영역을 넣어서 해당 영역에 얼마나 밀집되어있는지 확인할 수 있습니다.
            ''')
        fig2 = px.scatter(df, x = y_pred, y="price", title='predict vs actual', color='cut')
        st.plotly_chart(fig2)