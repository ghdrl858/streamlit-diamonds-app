import streamlit as st
import pandas as pd
import seaborn as sns
from PIL import Image

def run_info() :
    st.header('Diamonds_Info')

    # dataset 불러오기
    df = sns.load_dataset("diamonds")

    # 필요한 컬럼만 사용하기 위한 작업
    df_columns = df.columns[ : 6]

    my_choice = st.selectbox('Choice the Columns', df_columns)

    if my_choice == df.columns[0] :
        st.write('')
        if st.checkbox('carat_columns') :
            st.dataframe(df['carat'].head(15))
            st.write('')
        if st.checkbox('carat_info') :
            st.write('''###### ° Carat은 캐럿이라 부릅니다. 대다수 사람들은 크기라고 알고있지만, 중량을 의미합니다.
            
###### ° 캐럿 중량은 라운드 브릴리언트, 프린세스, 페어, 오벌, 쿠션, 마퀴즈, 에메랄드, 래디언트 또는 하트와 같이 각각의 다이아몬드 쉐입에 따라 다르게 보일 수 있습니다.
            
            ''')
            image = Image.open('image/carat.webp')
            st.image(image, use_column_width=True)

    elif my_choice == df.columns[1] :
        st.write('')
        if st.checkbox('cut_columns') :
            st.dataframe(df['cut'].head(15))
            st.write('')
        if st.checkbox('cut_info') :
            st.write('''###### ° 우리가 흔히 보는 다이아몬드는 ***Cut*** 즉, 연마과정을 거쳐서 나온것입니다.
            
###### ° 우리가 보는 다이아몬드를 보려면 크게 5가지의 과정이 있습니다.
###### ° 절단 계획 -> 다이아몬드 절단 -> 원형화 -> 다이아몬드 광택 작업 -> 4C 가치판단 이렇게 5가지입니다.
            
            ''')
            st.write('')
            video_file = open('video/diamonds_video.mp4', 'rb')
            st.video(video_file)

    elif my_choice == df.columns[2] :
        st.write('')
        if st.checkbox('color_columns') :
            st.dataframe(df['color'].head(15))
            st.write('')
        if st.checkbox('color_info') :

            st.write('''###### ° ***color***은 화이트 다이아몬드의 고유한 천연 색조를 의미합니다.
            
###### ° 자연 상태에서 대부분의 다이아몬드는 약간의 노란색을 띱니다. 
###### ° 다이아몬드는 무색에 가까울수록 더욱 희소한 가치를 지닙니다. 아래사진은 색상 등급입니다.
            
            ''')
            image = Image.open('image/diamonds_color.webp')
            st.image(image, use_column_width=True)

    elif my_choice == df.columns[3] :
        st.write('')
        if st.checkbox('clarity_columns') :
            st.dataframe(df['clarity'].head(15))
            st.write('')
        if st.checkbox('clarity_info') :

            st.write('''###### ° 다이아몬드 투명도는 현미경으로 10배 확대했을 때 보이는 다이아몬드의 순도, 희소성에 대한 측정기준입니다.
            
| clarity       | Explanation   |
| ------------- |:-------------:|
| FL            | 내부적 / 외부적특징이 전혀없는 상태 |
| IF            | 내부적 특징 X / 극히 미세한 외부적 특징 O |
| VVS1 VVS2     | VVS 다이아몬드에 아주 미세한 내부적 특징 O |
| VS1 Vs2       | VS 다이아몬드에 미세한 내부적 특징 O |
| SI1 SI2       | SI 다이아몬드에 약간의 내부적 특징 O |
| I1 I2 I3      | I 다이아몬드는 불완전 |
            
            ''')
            st.write('')
            image = Image.open('image/diamonds_clarity.webp')
            st.image(image, use_column_width=True)
    
    # elif my_choice == df.columns[4] :
    #     if st.checkbox('carat_columns') :
    #         st.dataframe(df['carat'].head(15))
    #     if st.checkbox('carat_info') :

    #         st.write('''''')
    #         image = Image.open('image/carat.webp')
    #         st.image(image, use_column_width=True)

    # elif my_choice == df.columns[5] :
    #     if st.checkbox('carat_columns') :
    #         st.dataframe(df['carat'].head(15))
    #     if st.checkbox('carat_info') :

    #         st.write('''''')
    #         image = Image.open('image/carat.webp')
    #         st.image(image, use_column_width=True)