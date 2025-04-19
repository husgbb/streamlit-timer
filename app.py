import streamlit as st
import time
import datetime

# 스타일 설정 - 타이머 글자를 크게, 중앙에 배치
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.timer-display {
    font-size: 10vw !important; /* 뷰포트 너비의 10%로 설정 */
    text-align: center !important;
    font-weight: bold !important;
    margin: 0 auto !important;
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    height: 75vh !important; /* 뷰포트 높이의 75% */
    width: 75% !important; /* 너비의 75% */
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# 전체 페이지를 세 개의 열로 나눔 (1:3:1 비율)
col1, col2, col3 = st.columns([1, 3, 1])

with col2:  # 가운데 컬럼에 타이머 배치
    y = st.empty()

    # 버튼을 세 개의 열로 나눔 (1:1:1 비율)
    c1, c2, c3 = st.columns([1, 1, 1])
    
    start = c1.button("시작", key=1)
    stop = c2.button("정지", key=2)
    reset = c3.button("리셋", key=3)

    if 'start_time' not in st.session_state:
        st.session_state['start_time'] = None

    if st.session_state['start_time'] is None:
        dt_str = "0:00:00"
        #st.markdown(f"<h1 style='text-align: center;'>{dt_str}</h1>", unsafe_allow_html=True)

    if start:
        st.session_state['start_time'] = datetime.datetime.now()
        with y:
            while True:
                now = datetime.datetime.now()
                td = now - st.session_state['start_time']
                td_str = str(td).split(".")[0]
                st.markdown(f"<h1 style='text-align: center;'>{dt_str}</h1>", unsafe_allow_html=True)
                time.sleep(1)

    if stop:
        if st.session_state['start_time'] is not None:
            now = datetime.datetime.now()
            td = now - st.session_state['start_time']
            td_str = str(td).split(".")[0]
            with y:
                st.markdown(f"<h1 style='text-align: center;'>{dt_str}</h1>", unsafe_allow_html=True)

    if reset:
        st.session_state['start_time'] = None
        dt_str = "0:00:00"
        st.markdown(f"<h1 style='text-align: center;'>{dt_str}</h1>", unsafe_allow_html=True)