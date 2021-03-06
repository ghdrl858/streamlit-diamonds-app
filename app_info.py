import streamlit as st
import pandas as pd
import seaborn as sns
from PIL import Image

def run_info() :
    st.header('๐ฌ Diamonds_Info')
    st.write('''##### โ๏ธ ๊ฐ ์ปฌ๋ผ์ ์๋ฏธ๋ฅผ ๋ชจ๋ฅผ ์ ์๊ธฐ์ ๊ฐ๋จํ ์ ๋ณด๋ฅผ ์ ๋ฌํ๊ณ ์ ๋ง๋  ํ์ด์ง์๋๋ค.''')

    # dataset ๋ถ๋ฌ์ค๊ธฐ
    df = sns.load_dataset("diamonds")

    # ํ์ํ ์ปฌ๋ผ๋ง ์ฌ์ฉํ๊ธฐ ์ํ ์์
    df_columns = df.columns[ : 6]

    # selectbox๋ฅผ ์ด์ฉํด ์ปฌ๋ผ ์ ํ
    my_choice = st.selectbox('Choice the Columns', df_columns)

    # ๊ฐ ์ปฌ๋ผ๋ค ๊ธฐ๋ฅ ์ ๋ฆฌ
    # carat ์ปฌ๋ผ ์ ๋ฆฌ
    if my_choice == df.columns[0] :
        st.write('')
        if st.checkbox('carat_columns') :
            st.dataframe(df['carat'].head(15))
            st.write('')
        if st.checkbox('carat_info') :
            st.write('''###### โ๏ธ Carat์ ์บ๋ฟ์ด๋ผ ๋ถ๋ฆ๋๋ค. ๋๋ค์ ์ฌ๋๋ค์ ํฌ๊ธฐ๋ผ๊ณ  ์๊ณ ์์ง๋ง, ์ค๋์ ์๋ฏธํฉ๋๋ค.
            
###### โ๏ธ ์บ๋ฟ ์ค๋์ ๋ผ์ด๋ ๋ธ๋ฆด๋ฆฌ์ธํธ, ํ๋ฆฐ์ธ์ค, ํ์ด, ์ค๋ฒ, ์ฟ ์, ๋งํด์ฆ, ์๋ฉ๋๋, ๋๋์ธํธ ๋๋ ํํธ์ ๊ฐ์ด ๊ฐ๊ฐ์ ๋ค์ด์๋ชฌ๋ ์์์ ๋ฐ๋ผ ๋ค๋ฅด๊ฒ ๋ณด์ผ ์ ์์ต๋๋ค.
            
            ''')
            image = Image.open('image/carat.webp')
            st.image(image, use_column_width=True)

    # cut ์ปฌ๋ผ ์ ๋ฆฌ
    elif my_choice == df.columns[1] :
        st.write('')
        if st.checkbox('cut_columns') :
            st.dataframe(df['cut'].head(15))
            st.write('')
        if st.checkbox('cut_info') :
            st.write('''###### โ๏ธ ์ฐ๋ฆฌ๊ฐ ํํ ๋ณด๋ ๋ค์ด์๋ชฌ๋๋ ***Cut*** ์ฆ, ์ฐ๋ง๊ณผ์ ์ ๊ฑฐ์ณ์ ๋์จ๊ฒ์๋๋ค.
            
###### โ๏ธ ์ฐ๋ฆฌ๊ฐ ๋ณด๋ ๋ค์ด์๋ชฌ๋๋ฅผ ๋ณด๋ ค๋ฉด ํฌ๊ฒ 5๊ฐ์ง์ ๊ณผ์ ์ด ์์ต๋๋ค.
###### โ๏ธ ์ ๋จ ๊ณํ -> ๋ค์ด์๋ชฌ๋ ์ ๋จ -> ์ํํ -> ๋ค์ด์๋ชฌ๋ ๊ดํ ์์ -> 4C ๊ฐ์นํ๋จ ์ด๋ ๊ฒ 5๊ฐ์ง์๋๋ค.
            
            ''')
            st.write('')
            video_file = open('video/diamonds_video.mp4', 'rb')
            st.video(video_file)

    # color ์ปฌ๋ผ ์ ๋ฆฌ
    elif my_choice == df.columns[2] :
        st.write('')
        if st.checkbox('color_columns') :
            st.dataframe(df['color'].head(15))
            st.write('')
        if st.checkbox('color_info') :

            st.write('''###### โ๏ธ ***color***์ ํ์ดํธ ๋ค์ด์๋ชฌ๋์ ๊ณ ์ ํ ์ฒ์ฐ ์์กฐ๋ฅผ ์๋ฏธํฉ๋๋ค.
            
###### โ๏ธ ์์ฐ ์ํ์์ ๋๋ถ๋ถ์ ๋ค์ด์๋ชฌ๋๋ ์ฝ๊ฐ์ ๋ธ๋์์ ๋ฑ๋๋ค. 
###### โ๏ธ ๋ค์ด์๋ชฌ๋๋ ๋ฌด์์ ๊ฐ๊น์ธ์๋ก ๋์ฑ ํฌ์ํ ๊ฐ์น๋ฅผ ์ง๋๋๋ค. ์๋์ฌ์ง์ ์์ ๋ฑ๊ธ์๋๋ค.
            
            ''')
            image = Image.open('image/diamonds_color.webp')
            st.image(image, use_column_width=True)

    # clarity ์ปฌ๋ผ ์ ๋ฆฌ
    elif my_choice == df.columns[3] :
        st.write('')
        if st.checkbox('clarity_columns') :
            st.dataframe(df['clarity'].head(15))
            st.write('')
        if st.checkbox('clarity_info') :

            st.write('''###### โ๏ธ ๋ค์ด์๋ชฌ๋ ํฌ๋ช๋๋ ํ๋ฏธ๊ฒฝ์ผ๋ก 10๋ฐฐ ํ๋ํ์ ๋ ๋ณด์ด๋ ๋ค์ด์๋ชฌ๋์ ์๋, ํฌ์์ฑ์ ๋ํ ์ธก์ ๊ธฐ์ค์๋๋ค.
            
| clarity       | Explanation   |
| ------------- |:-------------:|
| FL            | ๋ด๋ถ์  / ์ธ๋ถ์ ํน์ง์ด ์ ํ์๋ ์ํ |
| IF            | ๋ด๋ถ์  ํน์ง X / ๊ทนํ ๋ฏธ์ธํ ์ธ๋ถ์  ํน์ง O |
| VVS1 VVS2     | VVS ๋ค์ด์๋ชฌ๋์ ์์ฃผ ๋ฏธ์ธํ ๋ด๋ถ์  ํน์ง O |
| VS1 Vs2       | VS ๋ค์ด์๋ชฌ๋์ ๋ฏธ์ธํ ๋ด๋ถ์  ํน์ง O |
| SI1 SI2       | SI ๋ค์ด์๋ชฌ๋์ ์ฝ๊ฐ์ ๋ด๋ถ์  ํน์ง O |
| I1 I2 I3      | I ๋ค์ด์๋ชฌ๋๋ ๋ถ์์  |
            
            ''')
            st.write('')
            image = Image.open('image/diamonds_clarity.webp')
            st.image(image, use_column_width=True)
    
    # depth ์ปฌ๋ผ ์ ๋ฆฌ
    elif my_choice == df.columns[4] :
        st.write('')
        if st.checkbox('depth_columns') :
            st.dataframe(df['depth'].head(15))
            st.write('')
        if st.checkbox('depth_info') :

            st.write('''###### โ๏ธ ***depth***๋ ๋ง ๊ทธ๋๋ก ๊น์ด๋ฅผ ์๋ฏธํฉ๋๋ค.
            
###### โ๏ธ ์ฌ์ง์ฒ๋ผ ๋ง์ด ๋ด์ผํ  ๋ถ๋ถ์ด ๋ง์ง๋ง ๊น์ด๋ ์ฌ์ง์ ***'total depth'*** ๋ฅผ ์ฃผ๋ก ํ์ธํฉ๋๋ค.
###### โ๏ธ 59% ~ 62.3%๋ฉด Excellent, 58% ~ 58.9%๋ 62.4% ~ 63.5% ์ ๋๋ฉด Very Good์ด๋ผ๊ณ ํฉ๋๋ค.
            
            ''')
            image = Image.open('image/diamonds_depth.png')
            st.image(image, use_column_width=True)

    # table ์ปฌ๋ผ ์ ๋ฆฌ
    elif my_choice == df.columns[5] :
        st.write('')
        if st.checkbox('table_columns') :
            st.dataframe(df['table'].head(15))
            st.write('')
        if st.checkbox('tlble_info') :

            st.write('''###### โ๏ธ ๋ค์ด์๋ชฌ๋ ์๋ฉด์ ํํธํ ๋ถ๋ถ์ ํ์ด๋ธ์ด๋ผ๊ณ  ํฉ๋๋ค.
            
###### โ๏ธ ์๋ฉด ์ฆ, ํ์ด๋ธ์ ๋ชจ์์ ์ฐ๋ง ๊ณผ์ ์ค์์ ๋ฐ์ํฉ๋๋ค.
###### โ๏ธ 52% ~ 62%๋ ***Excellent***, 50% ~ 66%๊น์ง๋ ***Very Good***์ผ๋ก ํ์ด๋ธ์ ๋ฑ๊ธ์ด ๋ฉด์  %์ ๋ฐ๋ผ ๋๋ฉ๋๋ค.
            ''')
            image = Image.open('image/diamonds_table.jpg')
            st.image(image, use_column_width=True)