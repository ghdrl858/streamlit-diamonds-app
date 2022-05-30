# streamlit-diamonds-app

- 사이드바 메뉴 구성 : home, info, chart, ml
 - home : 이 웹 대시보드가 무엇인지 간단한 소개글 및 시각화 화면 구성

 - info : diamonds dataset은 컬럼에 의미가 해석하지 않는 이상 햇갈린다.
          그래서 info 메뉴를 만들어서 각 컬럼에 의미를 해석 정리하고 보는 사람들이 이해할 수
          있는 페이지를 만들 예정.
          ex) selectbox로 해당 컬럼 선택 -> 체크박스로 설명글 및 예시 이미지 출력
              예시 이미지는 찾기 어렵거나 없을 수도 있으니 가능한 컬럼은 넣도록하자.

 - chart : color 컬럼, cut 컬럼, price 컬럼,  clarity 컬럼에 대한 그래프 출력
           미리 colab에서 정리한 데이터 인용

 - ml : 인공지능 학습시킨 예측값과 히트맵을 이용해서 시각화 작업 진행