# Libraries

import pandas as pd 
import plotly.express as px
import streamlit as st 
import numpy as np
from datetime import date
from datetime import datetime
from datetime import timedelta
import os

# RECUP LA DATA
# Retrieve the path to the current folders
current_path = os.getcwd()

# Get the path to the csv file folder - in this case the 'data' file
csv_path = os.path.join(current_path, 'data\\test')

# A EXPLIQUER ICI
for file in os.listdir(csv_path):
    fd = pd.read_csv(os.path.join(csv_path, file))
    globals()[file.rpartition(".")[0]] = fd

twoday = datetime.strftime(datetime.now(), "%Y/%m/%d")
t = pd.to_datetime(twoday)
t = pd.to_datetime(t)

today = datetime.strftime(datetime.now(), "%d/%m/%Y")

st.set_page_config(page_title="ASTROTOOL")
st.write("ASTROTOOL")

m1 = Nat.copy()
m2 = Spi.copy()
m3 = TrNa.copy()
m4 = TrTr.copy()
m5 = addPrice.copy()
m6 = Fib.copy()

o1,o2,o3,o4,o5,o6 = st.tabs(["Natural Square", "Spiral", "TrNa", "TrTr", "addPrice", "Fib"])

with o1:
    col1, col2 = st.columns([1,3.33])

    with col1:
        st.dataframe(m1.style.background_gradient(cmap='Blues'))
    with col2:
        fig1 = px.bar(m1, x='Date', y='Hit')
        st.plotly_chart(fig1, use_container_width=True)

with o2:
    col1, col2 = st.columns([1,3.33])

    with col1:
        st.dataframe(m2.style.background_gradient(cmap='Blues'))
    with col2:
        fig2 = px.bar(m2, x='Date', y='Hit')
        st.plotly_chart(fig2, use_container_width=True)

with o3:
    col1, col2 = st.columns([1,2.9])

    with col1:
        st.dataframe(m3.style.background_gradient(cmap='Blues'))
    with col2:
        fig3 = px.bar(m3, x='Date', y='Points')
        st.plotly_chart(fig3, use_container_width=True)

with o4:
    col1, col2 = st.columns([1,2.9])

    with col1:
        st.dataframe(m4.style.background_gradient(cmap='Blues'))
    with col2:
        fig4 = px.bar(m4, x='Date', y='Points')
        st.plotly_chart(fig4, use_container_width=True)

with o5:
    col1, col2 = st.columns([1,3.33])

    with col1:
        st.dataframe(m5.style.background_gradient(cmap='Blues'))
    with col2:
        fig5 = px.bar(m5, x='Date', y='Hit')
        st.plotly_chart(fig5, use_container_width=True)

with o6:
    col1, col2 = st.columns([1,3.33])

    with col1:
        st.dataframe(m6.style.background_gradient(cmap='Blues'))
    with col2:
        fig6 = px.bar(m6, x='Date', y='Hit')
        st.plotly_chart(fig6, use_container_width=True)