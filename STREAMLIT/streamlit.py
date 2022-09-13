# Libraries

import pandas as pd 
import plotly.express as px
import streamlit as st
import numpy as np
from datetime import date
from datetime import datetime
from datetime import timedelta
import streamlit_authenticator as stauth
import database as db
from PIL import Image
import os

# RECUP LA DATA
# Retrieve the path to the current folders
current_path = os.getcwd()

# Get the path to the csv file folder - in this case the 'data' file
csv_path = os.path.join(current_path, 'data')

# A EXPLIQUER ICI
for file in os.listdir(csv_path):
    fd = pd.read_csv(os.path.join(csv_path, file))
    globals()[file.rpartition(".")[0]] = fd

twoday = datetime.strftime(datetime.now(), "%Y/%m/%d")
t = pd.to_datetime(twoday)
t = pd.to_datetime(t)

today = datetime.strftime(datetime.now(), "%d/%m/%Y")

# LOGO
st.set_page_config(page_title="ASTROTOOL", layout="wide")
logo = Image.open(r'logo.png')

col1, col2, col3 = st.columns([8, 7, 2])

with col1:
    st.write(' ')

with col2:
    st.image(logo)

with col3:
    st.write(' ')

# --- USER AUTHENTIFICATION ---

users = db.fetch_all_users()

usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
hashed_passwords = [user["password"] for user in users]

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "astrotool_dashboard", "abcdef", cookie_expiry_days=30)

names, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username / Password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

# --- DASHBOARD ---

if authentication_status:

    st.markdown(f"Welcome aboard {names}, enjoy our Alpha Version!")

    m = fluchart.copy()

    hm = helio_main.copy()
    gm = geo_main.copy()

    m1 = NatSq.copy()
    m2 = Spi.copy()
    m3 = TrTr.copy()
    m4 = TrNa.copy()
    m5 = addPrice.copy()
    m6 = Fib.copy()
    m7 = FutureDate.copy()
    m8 = Mult.copy()
    m9 = Natal.copy()
    m10 = PriceTime.copy()
    m11 = Retro.copy()
    m12 = Sq9.copy()

    mn1 = aspects_h_tr.copy()
    mn2 = aspects_h_na.copy()
    mn3 = aspects_g_tr.copy()
    mn4 = aspects_g_na.copy()
    mn5 = dec_lat.copy()
    mn6 = retro_asp.copy()
    mn6.fillna(' ', inplace=True)
    mn7 = tools.copy()
    mn7.fillna(' ', inplace=True)

    # ONGLETS

    main,chart,Method = st.tabs(["Main", "Chart","Method"])

    with main:

        h1,h2,h3=st.tabs(["Helio", "Geo", "Tools"])

        with h1:

            col0,col00 = st.columns([6,4])
            with col0:
                st.dataframe(hm.style.background_gradient(cmap='Blues'))
            with col00:
                st.markdown("**Aspects TrTr & TrNa**")
                st.dataframe(mn1.style.background_gradient(cmap='Blues'))
                st.dataframe(mn2.style.background_gradient(cmap='Blues'))

        with h2:

            col0,col00 = st.columns([6.618,3])
            with col0:
                st.dataframe(gm.style.background_gradient(cmap='Blues'))
            with col00:
                st.markdown("**Aspects TrTr & TrNa**")
                st.dataframe(mn3.style.background_gradient(cmap='Blues'))
                st.dataframe(mn4.style.background_gradient(cmap='Blues'))
        
        with h3:

            col5, col9 = st.columns([6,4])
            with col5:
                st.markdown("**Retro**")
                st.dataframe(mn6.style.background_gradient(cmap='Blues'))
            with col9:
                st.markdown("**Declination/Latitude**")
                st.dataframe(mn5.style.background_gradient(cmap='Blues'))

            st.markdown("**Moon/Node/Dec/Lat**")
            col7, col8 = st.columns([12,0.2])
            with col7:
                st.dataframe(mn7.style.background_gradient(cmap='Blues'))

    with chart:
        fig0 = px.bar(m, x='Date', y='EP', color='EP', color_continuous_scale=px.colors.sequential.Cividis,
                height=500, width=3200)
        st.plotly_chart(fig0, use_container_width=True)

    with Method:
        
        o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12=st.tabs(["NatSq", "Spiral", "TrTr", "TrNa", "addPrice", "Fib", "FutDates", "Mult", "Natal", "PriceTime", "Retro", "Sq9"])
        
        with o1:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m1.style.background_gradient(cmap='Blues'))
            with col2:
                fig1 = px.bar(m1, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="NatSq | Hits Chart")
                st.plotly_chart(fig1, use_container_width=True)

        with o2:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m2.style.background_gradient(cmap='Blues'))
            with col2:
                fig2 = px.bar(m2, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Spiral | Hits Chart")
                st.plotly_chart(fig2, use_container_width=True)

        with o3:
            col1, col2 = st.columns([1,2.9])

            with col1:
                st.dataframe(m3.style.background_gradient(cmap='Blues'))
            with col2:
                fig3 = px.bar(m3, x='Date', y='Points',
                        title="TrTr | Hits Chart")
                st.plotly_chart(fig3, use_container_width=True)

        with o4:
            col1, col2 = st.columns([1,2.9])

            with col1:
                st.dataframe(m4.style.background_gradient(cmap='Blues'))
            with col2:
                fig4 = px.bar(m4, x='Date', y='Points',
                        title="TrNa | Hits Chart")
                st.plotly_chart(fig4, use_container_width=True)

        with o5:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m5.style.background_gradient(cmap='Blues'))
            with col2:
                fig5 = px.bar(m5, x='Date', y='Hit', title="addPrice | Hits Chart")
                st.plotly_chart(fig5, use_container_width=True)

        with o6:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m6.style.background_gradient(cmap='Blues'))
            with col2:
                fig6 = px.bar(m6, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Fib | Hits Chart")
                st.plotly_chart(fig6, use_container_width=True)

        with o7:
            col1, col2 = st.columns([2,3.80])

            with col1:
                st.dataframe(m7.style.background_gradient(cmap='Blues'))
            with col2:
                fig7 = px.bar(m7, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="FutDates | Hits Chart")
                st.plotly_chart(fig7, use_container_width=True)

        with o8:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m8.style.background_gradient(cmap='Blues'))
            with col2:
                fig8 = px.bar(m8, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Mult | Hits Chart")
                st.plotly_chart(fig8, use_container_width=True)

        with o9:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m9.style.background_gradient(cmap='Blues'))
            with col2:
                fig9 = px.bar(m9, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Natal | Hits Chart")
                st.plotly_chart(fig9, use_container_width=True)

        with o10:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m10.style.background_gradient(cmap='Blues'))
            with col2:
                fig10 = px.bar(m10, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="PriceTime | Hits Chart")
                st.plotly_chart(fig10, use_container_width=True)

        with o11:
            col1, col2 = st.columns([1,2.8])

            with col1:
                st.dataframe(m11.style.background_gradient(cmap='Blues'))
            with col2:
                fig11 = px.bar(m11, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Retro | Hits Chart")
                st.plotly_chart(fig11, use_container_width=True)

        with o12:
            col1, col2 = st.columns([1,3.33])

            with col1:
                st.dataframe(m12.style.background_gradient(cmap='Blues'))
            with col2:
                fig12 = px.bar(m12, x='Date', y='Hit', color='Hit', color_continuous_scale=px.colors.sequential.Blues,
                        title="Sq9 | Hits Chart")
                st.plotly_chart(fig12, use_container_width=True)

    col1, col2, col3 = st.columns([8, 7, 2])
    with col1:
        st.write(' ')
    with col2:
        authenticator.logout("Logout", "main")
    with col3:
        st.write(' ')