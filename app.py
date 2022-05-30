from pyparsing import alphas
import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
from app_home import run_home
from app_info import run_info
from app_chart import run_chart
from app_ml import run_ml

def main() :

    # 옵션 메뉴 꾸미기 코드
    with st.sidebar:
        menu = option_menu('Menu',['Home','Info','Chart', 'ML'], menu_icon='caret-down-fill', icons = ['bi bi-house-fill','bi bi-info-circle-fill',"bi bi-bar-chart-line-fill", 'bi bi-tools'], default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#16B4F2", },
        "icon": {"color": "white", "font-size": "25px"}, 
        "nav-link": {'color' : 'white', "font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#F2CB05"},
        "nav-link-selected": {"background-color": "#24BF4B"}
    })
    if menu == 'Home':
        run_home()
    elif menu == 'Info':
        run_info()
    elif menu == 'Chart':
        run_chart()
    elif menu == 'ML':
        run_ml()
   
    # 이미지 구현
    # with st.sidebar :
    #     st.write('')
    #     st.write('')
    #     image = Image.open('image/headphones.png')
    #     st.image(image, use_column_width=True)

if __name__ == '__main__' :
    main()