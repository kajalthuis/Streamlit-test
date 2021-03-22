# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 12:59:56 2021

@author: KALT
"""

import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello World')

st.write("""Tessts""")

"""
##  My first app
Here's our first attempt at using data to create a table:
"""

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    st.line_chart(chart_data)
    
option = st.sidebar.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected:', option