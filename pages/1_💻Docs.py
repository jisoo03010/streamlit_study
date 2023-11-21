
# 데이터 관련 dashboard및 다양한 기능을 프로토타입으로 빠르게 구현하고 배포까지 할 수 있는 툴임
#  https://wonyoungseo.medium.com/kr-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9B%B9%EC%96%B4%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EB%A7%9B%EB%B3%B4%EA%B8%B0-feat-streamlit-846937a7438d
from time import sleep

import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image

#  페이지 기본 설정 
st.set_page_config(
    page_icon="⚙️",
    page_title="지수의 스르팀릿 배포하기",
    layout="wide"
)
# 로딩바 구현하기
with st.spinner(text="페이지 로딩중..."):
    sleep(2)
# st.title('Streamlit Tutorial')
# ## Header/Subheader

# 페이지 헤더, 서브헤더 제목 설정
st.header('Hello World🤝')
st.subheader('스트림릿 기능 맛보기')
st.markdown('**스트림릿** 기능 맛보기')
# ## Text
# st.text("Hello Streamlit! 이 글은 튜토리얼 입니다.")

img = Image.open("files/catimg.png")
st.image(img, width=400, caption="이것은 고양이 사진입니다.")

cols = st.columns((1, 1, 2))
cols[0].metric("10/11", "15 °C", "2")
cols[0].metric("10/12", "17 °C", "2 °F")
cols[0].metric("10/13", "15 °C", "2")
cols[1].metric("10/14", "17 °C", "2 °F")
cols[1].metric("10/15", "14 °C", "-3 °F")
cols[1].metric("10/16", "13 °C", "-1 °F")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
# 컬럼 나머지 부분에 라인차트 생성
cols[2].line_chart(chart_data)