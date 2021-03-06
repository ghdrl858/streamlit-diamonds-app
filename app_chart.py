import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

def run_chart() :
    st.header('π Diamonds_Chart')
    st.write('''##### βοΈ κ° μ»¬λΌμ λν κ·Έλνλ₯Ό νμΈν  μ μλ νμ΄μ§μλλ€.''')

    # dataset λΆλ¬μ€κΈ°
    df = sns.load_dataset("diamonds")


    # νμν μ»¬λΌλ§ μ¬μ©νκΈ° μν μμ
    df_columns = df.columns[ : 4]

    # selectboxλ₯Ό μ΄μ©ν΄ μ»¬λΌ μ ν
    my_choice = st.selectbox('Diamonds_4C : Choice the Columns', df_columns)
    if my_choice == df.columns[0] :
        if st.button('carat_chart 1') :
            st.write('''###### βοΈ μ΄ κ·Έλνλ '***carat***' κ³Ό '***depth***' μ μκ΄κ΄κ³ κ·Έλνμλλ€.
            
###### βοΈ λμ²΄λ‘ '***carat***' μ 0 ~ 2.5μ λ, '***depth***' μ κ²½μ° 55 ~ 65 λΆκ·Όμ λ°μ§λμ΄μλ κ²μ λ³Ό μ μμ΅λλ€.
###### βοΈ colorμ cutμ μΆκ°ν¨μΌλ‘μ¨ λ μ»¬λΌκ³Ό κ°μ΄ λ°μ§λμ΄μλμ§ νμΈμ΄ κ°λ₯ν©λλ€.
###### βοΈ νμΈν΄λ³΄λ 'Very Good' λΆλΆμ΄ 55 ~ 65 λΆκ·Όμ λ°μ§λμ΄μμ΅λλ€.
            ''')
            carat1 = px.scatter(df, x="carat", y="depth", color="cut")
            st.plotly_chart(carat1)
        
        if st.button('carat_chart 2') :
            st.write('''###### βοΈ μ΄ κ·Έλνλ '***carat***' κ³Ό '***price***' μ μκ΄κ΄κ³ κ·Έλνμλλ€.
            
###### βοΈ '***carat***' μ΄ μ¦κ°ν¨μλ°λΌ '***price***' μ κ°κ²©μ΄ μ¦κ°ν¨μ νμΈν  μ μμ΅λλ€.
###### βοΈ 'Very Good' λ±κΈμ΄ λ§μ§λ§ λΉμΌ κ°κ²©μμ 'ideal' λ±κΈμ΄ κ°κ°ν λ³΄μ΄λ κ²μ νμΈν  μ μμ΅λλ€.
            
            ''')
            carat2 = px.scatter(df, x="carat", y="price", color="cut")
            st.plotly_chart(carat2)

    if my_choice == df.columns[1] :
        st.write('')
        if st.checkbox('cut_value_counts') :
            st.write('''
                
| λ± κΈ         | μ΄ κ°―μ |
| ------------- |:-----: |
| Ideal         | 21551  |
| Premium       | 13791  |
| Very Good     | 12082  |
| Good          | 4906   |
| Fair          | 1610   |
                
                        ''')
        st.write('')
        if st.button('cut_chart 1') :
            st.write('''###### βοΈ '***cut***' μ λ¦¬λ νμ΄λΈμ κ·Έλνλ‘ νννμ΅λλ€.

###### βοΈ νμ΄λΈκ³Ό κ·Έλνλ₯Ό κ°μ΄ νμΈν¨μΌλ‘μ νλμ λΉκ΅νκΈ° μ¬μΈκ²μλλ€.
            ''')
            cut_count = df["cut"].value_counts()
            cut1 = px.bar(cut_count, text = cut_count, title="cut count")
            st.plotly_chart(cut1)
    
    if my_choice == df.columns[2] :
        if st.button('color_chart 1') :
            st.write('''###### βοΈ '***color***' μ μ°λ§ λ±κΈμΈ '***cut***' μ κ°μ΄ λνλΈ κ·Έλνμλλ€.

###### βοΈ μλ κ·Έλνλ₯Ό ν΅ν΄ ν΄λΉνλ μμμ λ°λΌμ μ°λ§ λ±κΈμ λΉμ¨μ νμΈν  μ μμ΅λλ€.
            ''')

            color1 = px.histogram(df, x="color", histfunc="count", color="cut")
            st.plotly_chart(color1)
        
        if st.button('color_chart 2') :
            st.write('''###### βοΈ color_chart 1 κ³Ό κ°μ μμμ κ΄ν κ·Έλνμ§λ§, κ° κ·Έλνλ§λ€ μ°λ§ λ±κΈλ³λ‘ λλ μ§ κ·Έλνμλλ€.
            
###### βοΈ color_chart 1 κ³Ό color_chart 2 λ₯Ό λΉκ΅ν΄μλ³΄λ©΄ λ μ νν μμΉλ₯Ό νμΈν  μ μμκ²μλλ€.
            ''')

            color2 = px.histogram(df, x="color", histfunc="count", color="cut", facet_col="cut")
            st.plotly_chart(color2)

    if my_choice == df.columns[3] :
        if st.button('clarity_chart 1') :
            st.write('''###### βοΈ '***clarity***' μ¦, ν¬λͺλμ κ΄ν κ·Έλνμλλ€.

###### βοΈ μ°λ§ λ±κΈκ³Ό κ°μ΄ λνλΈ κ·Έλνμ΄λ©°, κ° λ±κΈμ λ°λ₯Έ ν¬λͺλ λΉμ¨μ λμΌλ‘ νμΈν  μ μμ΅λλ€.
            ''')

            clarity1 = px.histogram(df, x="clarity", histfunc="count", color="cut", facet_col="cut")
            st.plotly_chart(clarity1)