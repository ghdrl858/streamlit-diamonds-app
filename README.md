# 💎 streamlit-diamonds-app
 ✔️ dataset을 찾아보던중 seaborn라이브러리에 diamonds라는 자체 dataset이 있었고, 컬럼과 데이터가 깔끔해서 사용하기로 결정했습니다.

 ✔️ carat, cut, color, clarity 같은 컬럼들이 price에 얼마나 영향을 주는지가 궁금해서 예측하기로 했습니다.

 ✔️ 데이터 작업은 'Google Colab' 으로 작업, 'Streamlit' 사용으로 웹 대시보드를 만들어 시각화하기 위해 'Visual Studio Code' 로 작업한 데이터를 옮기면서 'Streamlit' 에 문법에 맞게 만드는 작업을 했습니다.
 
 ➡️ 사용 라이브러리 : streamlit_option_menu 사용했습니다.
 ➡️ 출처 : seaborn 라이브러리에 자체 diamonds Dataset을 이용했습니다.

# 📄 주요 컬럼 정리
1. carat       : 캐럿이라 부르며, 다이아몬드의 크기가 아닌 중량을 의미합니다. 1캐럿에 0.20g입니다.

2. cut         : 연마라고 부르며, 커팅이라고도 합니다. Good 등급 이상의 것을 선택하는 것이 좋습니다.

3. color       : D ~ Z까지 있습니다.  
> - DEF : 무색, GHIJ : 무색에 가까움  
> - KLM : 희미한 노란색  
> - NOPQR : 매우 옅은 노란색  
> - S ~ Z : 옅은 노란색으로 구분됩니다.

4. clarity     : 투명도를 의미합니다.  
> - I1(최악), SI2, SI1, VS2, VS1, VVS2, VVS1, IF(최상)으로 구분합니다.

5. depth       : 깊이를 의미합니다. 깊이가 깊을수록 더 단단하다고 합니다.

6. table       : 다이아몬드에 윗부분, 표면에 평평한면을 의미합니다.

# 💻 작업진행률
 ✔️ 1일차 : dataset 찾기 결과, seaborn 라이브러리에 있는 자체 dataset인 diamondse로 결정 및 dataset 정리. dataset 확인 및 그래프 작업

 ✔️ 2일차 : 인공지능 작업. 3개의 컬럼의 문자열 값이 있어 LabelEncoder로 숫자 치환 작업 사용한 모델은 ExtraTreesRegressor. 예측값은 히트맵으로 표현할 예정

 ✔️ 3일차 : streamlit 작업, 메뉴 구성 및 color 구성 조합 찾기, 웹 대시보드 일부 작업, app_home, app_info 중간까지 작업

 ✔️ 4일차 : app_info 작업 마무리, app_chart 및 app_ml부분까지 마무리 후, 지속적인 검토
