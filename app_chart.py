import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def run_chart() :
    st.header('📈 Diamonds_Chart')
    st.write('''##### ✔️ 각 컬럼에 대한 그래프를 확인할 수 있는 페이지입니다.''')

    # dataset 불러오기
    df = sns.load_dataset("diamonds")


    # 필요한 컬럼만 사용하기 위한 작업
    df_columns = df.columns[ : 4]

    # selectbox를 이용해 컬럼 선택
    my_choice = st.selectbox('Diamonds_4C : Choice the Columns', df_columns)
    if my_choice == df.columns[0] :
        if st.button('carat_chart 1') :
            st.write('''###### ✔️ 이 그래프는 '***carat***' 과 '***depth***' 에 상관관계 그래프입니다.
            
###### ✔️ 대체로 '***carat***' 은 0 ~ 2.5정도, '***depth***' 에 경우 55 ~ 65 부근에 밀집되어있는 것을 볼 수 있습니다.
###### ✔️ color에 cut을 추가함으로써 두 컬럼과 같이 밀집되어있는지 확인이 가능합니다.
###### ✔️ 확인해보니 'Very Good' 부분이 55 ~ 65 부근에 밀집되어있습니다.
            ''')
            carat1 = px.scatter(df, x="carat", y="depth", color="cut")
            st.plotly_chart(carat1)
        
        if st.button('carat_chart 2') :
            st.write('''###### ✔️ 이 그래프는 '***carat***' 과 '***price***' 에 상관관계 그래프입니다.
            
###### ✔️ '***carat***' 이 증가함에따라 '***price***' 에 가격이 증가함을 확인할 수 있습니다.
###### ✔️ 'Very Good' 등급이 많지만 비싼 가격에서 'ideal' 등급이 간간히 보이는 것을 확인할 수 있습니다.
            
            ''')
            carat2 = px.scatter(df, x="carat", y="price", color="cut")
            st.plotly_chart(carat2)

    if my_choice == df.columns[1] :
        st.write('')
        if st.checkbox('cut_value_counts') :
            st.write('''
                
| 등 급         | 총 갯수 |
| ------------- |:-----: |
| Ideal         | 21551  |
| Premium       | 13791  |
| Very Good     | 12082  |
| Good          | 4906   |
| Fair          | 1610   |
                
                        ''')
        st.write('')
        if st.button('cut_chart 1') :
            st.write('''###### ✔️ '***cut***' 과 '***price***' 에 그래프이며, 평균값을 히스토그램으로 나타냈습니다. 
                
###### ✔️ Primium이 수치가 높고 Good과 Very Good이 거의 비슷하다고 볼 수 있습니다. 
            ''')
            cut1 = px.histogram(df, x="cut", y="price", histfunc="avg")
            st.plotly_chart(cut1)
    
    if my_choice == df.columns[2] :
        if st.button('color_chart 1') :
            st.write('''###### ✔️ '***color***' 에 연마 등급인 '***cut***' 을 같이 나타낸 그래프입니다.

###### ✔️ 아래 그래프를 통해 해당하는 색상에 따라서 연마 등급의 비율을 확인할 수 있습니다.
            ''')

            color1 = px.histogram(df, x="color", histfunc="count", color="cut")
            st.plotly_chart(color1)
        
        if st.button('color_chart 2') :
            st.write('''###### ✔️ color_chart 1 과 같은 색상에 관한 그래프지만, 각 그래프마다 연마 등급별로 나눠진 그래프입니다.
            
###### ✔️ color_chart 1 과 color_chart 2 를 비교해서보면 더 정확한 수치를 확인할 수 있을것입니다.
            ''')

            color2 = px.histogram(df, x="color", histfunc="count", color="cut", facet_col="cut")
            st.plotly_chart(color2)

    if my_choice == df.columns[3] :
        if st.button('clarity_chart 1') :
            st.write('''###### ✔️ '***clarity***' 즉, 투명도에 관한 그래프입니다.

###### ✔️ 연마 등급과 같이 나타낸 그래프이며, 각 등급에 따른 투명도 비율을 눈으로 확인할 수 있습니다.
            ''')

            clarity1 = px.histogram(df, x="clarity", histfunc="count", color="cut", facet_col="cut")
            st.plotly_chart(clarity1)