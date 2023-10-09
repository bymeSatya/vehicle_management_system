import streamlit as st
import pandas
import requests
# import setuptools
#import snowflake.connector

#streamlit.title('User Login')

import time

st.set_page_config()
count_down = st.number_input("Enter")
ph = st.empty()
cnt_down(count_down)
def cnt_down(count_down):
    N = count_down*60
    for secs in range(N,0,-1):
        mm, ss = secs//60, secs%60
        ph.metric("Countdown", f"{mm:02d}:{ss:02d}")
        time.sleep(1)

