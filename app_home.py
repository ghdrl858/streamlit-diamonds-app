import streamlit as st
import pandas as pd
from PIL import Image

def run_home() :
    st.write('''## 💎 What is a ***Diamonds***?
    
###### ✔️  이 웹 대시보드는 ***다이아몬드***에 대해 다룰 것입니다.
###### ✔️  해당 📄 Dataset에 컬럼들에 의미를 모를 수 있으니 ***📋 Info***를 통해 설명할 것이며,
###### ✔️  ***📊 그래프***를 통해 중요 컬럼들을 확인 및 ***🖥️ 인공지능 학습***을 통해 보여줄 것입니다.

    
    ''')

    # 이미지 출력하기
    image = Image.open('image/diamonds.jpg')
    st.image(image, use_column_width=True)