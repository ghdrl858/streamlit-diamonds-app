import streamlit as st
import pandas as pd
from PIL import Image

def run_home() :
    st.write('''# What is a ***Diamonds***?
    
##### ° 광물의 종류 중 하나, 탄소 하나의 원소로 이루어진 원소 광물입니다.
    
    ''')


    image = Image.open('image/diamonds.jpg')
    st.image(image, use_column_width=True)