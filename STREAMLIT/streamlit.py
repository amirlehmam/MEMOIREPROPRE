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

o1,o2,o3,o4,o5,o6 = st.tabs(["Nat", "Spi", "TrNa", "TrTr", "addPrice", "Fib"])

with o1:
    st.dataframe(m1.style.background_gradient(cmap='Blues'))

    fig1 = px.bar(m1, x='Date', y='Hit')
    st.plotly_chart(fig1, use_container_width=True)

with o2:
    st.dataframe(m2.style.background_gradient(cmap='Blues'))

with o3:
    st.dataframe(m3.style.background_gradient(cmap='Blues'))

with o4:
    st.dataframe(m4.style.background_gradient(cmap='Blues'))

with o5:
    st.dataframe(m5.style.background_gradient(cmap='Blues'))

with o6:
    st.dataframe(m6.style.background_gradient(cmap='Blues'))