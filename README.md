# 💎 streamlit-diamonds-app
 ✔️ dataset을 찾아보던중 seaborn라이브러리에 diamonds라는 자체 dataset이 있었고, 컬럼과 데이터가 깔끔해서 사용하기로 결정했습니다.

 ✔️ carat, cut, color, clarity 같은 컬럼들이 price에 얼마나 영향을 주는지가 궁금해서 예측하기로 했습니다.

  ✔️ 데이터 작업은 'Google Colab' 으로 작업, 'Visual Studio Code' 로 'Google Colab' 에서 작업한 데이터를 옮기면서 'Streamlit' 에 문법에 맞게 작업하면서 웹 대시보드를 구성했습니다.
 
 ➡️ 출처 : seaborn 자체 라이브러리를 사용 / 'diamonds dataset'

# 📚 Use the Library

- ### streamlit_option_menu
  ##### - 옵션 메뉴를 사용을 위해 설치.

```python
pip install streamlit-option-menu
```
- ### plotly.express
  ##### - 반응적인 그래프를 그리기 위해 설치 및 업데이트.
```python
pip install plotly

pip install plotly --update
```

- ### matplotlib.pyplot
  ##### - 함수를 사용해 그래프사용하기 위해 설치.
```python
pip install matplotlib
```

# 📄 Dataset Columns
#### 1. carat : 캐럿이라 부르며, 다이아몬드의 크기가 아닌 중량을 의미합니다. 1캐럿에 0.20g입니다.

#### 2. cut : 연마라고 부르며, 커팅이라고도 합니다. *Good* 등급 이상의 것을 선택하는 것이 좋습니다.

#### 3. color : D ~ Z까지의 등급이 있습니다.  
> - DEF : 무색  
> - GHIJ : 무색에 가까움  
> - KLM : 희미한 노란색  
> - NOPQR : 매우 옅은 노란색  
> - S ~ Z : 옅은 노란색으로 구분됩니다.

#### 4. clarity : 투명도를 의미합니다.  
> - I1(최악), SI2, SI1, VS2, VS1, VVS2, VVS1, IF(최상)으로 구분합니다.

#### 5. depth : 깊이를 의미합니다. 깊이가 깊을수록 더 단단하다고 합니다.

#### 6. table : 다이아몬드에 윗부분, 표면에 평평한면을 의미합니다.

# 🗒️ Explanation
- ### app_home.py
✔️ 주제인 다이아몬드에 다루는 것을 알리는 페이지입니다.  

✔️각 페이지마다 어떤 것을 설명할 것인지 간략히 소개하는 페이지입니다.  

![app_home](https://user-images.githubusercontent.com/105832443/172625643-a26fda8f-58c7-4617-8c4f-5e80bc43365e.png)

- ### app_info.py
✔️ 데이터에 컬럼만 보면 이해할 수 없기 때문에 각 컬럼들이 어떤 의미를 가졌고, 무엇을 의미하는지 소개하는 페이지입니다.

✔️ 페이지에는 각 컬럼들에 데이터와 정보를 checkbox로 보기 편하게 구현했습니다.

![app_info](https://user-images.githubusercontent.com/105832443/172628323-d7199c64-fc22-4277-9214-755d099a4134.png)

![app_info2](https://user-images.githubusercontent.com/105832443/172628610-39ef0fc1-81c0-40ef-a8e2-3766ff11bb65.png)

- ### app_chart.py
✔️ 중요한 각 컬럼들에 데이터로 그린 그래프를 표현하는 페이지입니다.

✔️ 그래프는 *plotly.express* 라이브러리를 이용해 표현했고, 설명을 통해 그래프를 이해하기 쉽게 정리했습니다.

![app_Chart](https://user-images.githubusercontent.com/105832443/172630772-a06fac93-0877-48e1-8d2b-2e0e4f4e695c.png)

![app_Chart2](https://user-images.githubusercontent.com/105832443/172630789-e9757903-9082-4d28-84f5-7bc067645549.png)

- ### app_ml.py
✔️ 인공지능학습 시킨 결과를 보여주는 페이지입니다.

✔️ 인공지능 모델링은 ExtraTreeRegressor을 이용했습니다.  
> 정확도는 98%가 나왔습니다.

✔️ 실제값과 예측값을 scatter 그래프로 표현해 거의 근접함을 보여줬습니다.

![app_ml](https://user-images.githubusercontent.com/105832443/172637014-f8ecb7f2-a530-4c25-ad99-1f5bb7de015d.png)

![app_ml2](https://user-images.githubusercontent.com/105832443/172637060-d370bc5b-61ca-4555-9bac-a6e976fd3b4c.png)

# 💻 작업진행률
 ✔️ 1일차 : dataset 찾기 결과, seaborn 라이브러리에 있는 자체 dataset인 diamondse로 결정 및 dataset 정리. dataset 확인 및 그래프 작업

 ✔️ 2일차 : 인공지능 작업. 3개의 컬럼의 문자열 값이 있어 LabelEncoder로 숫자 치환 작업 사용한 모델은 ExtraTreesRegressor. 예측값은 scatter 그래프로 표현할 예정

 ✔️ 3일차 : streamlit 작업, 메뉴 구성 및 color 구성 조합 찾기, 웹 대시보드 일부 작업, app_home, app_info 중간까지 작업

 ✔️ 4일차 : app_info 작업 마무리, app_chart 및 app_ml부분까지 마무리 후, 지속적인 검토
