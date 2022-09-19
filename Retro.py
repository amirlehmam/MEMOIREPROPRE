# Libraries

import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime
from datetime import timedelta
import plotly.express as px
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

# fillna
Moon = Moon.copy()
Moon.fillna(0, inplace=True)

lat_moon_changes = lat_moon_changes.copy()
lat_moon_changes.fillna(0, inplace=True)

planet_node = planet_node.copy()
planet_node.fillna(0, inplace=True)

twoday = datetime.strftime(datetime.now(), "%Y/%m/%d")
t = pd.to_datetime(twoday)
t = pd.to_datetime(t)

## 1. Code
#*0 = 0 || 1 = True || 2 = Return*
r_h = retrohits.copy()
r_h = r_h.fillna(0)

r_h['Date'] = pd.to_datetime(r_h['Date'])
r_h['Hit'] = r_h['Merc'] + r_h['Ven'] + r_h['Mar'] + r_h['Jup'] + r_h['Sat'] + r_h['Ura'] + r_h['Nep'] + r_h['Plu']
r_h = r_h.drop(['Merc', 'Ven', 'Mar', 'Jup', 'Sat', 'Ura', 'Nep', 'Plu'], axis=1)

r_h['Date'] = pd.to_datetime(r_h['Date'])  

start_date = t  - timedelta(days = 1)
end_date = t + timedelta(days = 120)

mask = (r_h['Date'] > start_date) & (r_h['Date'] <= end_date)

rh_hits = r_h.loc[mask]
rh_hits = rh_hits.sort_values(by=['Date'], ascending = True)

dz_Retro = rh_hits.head(30)
dz_Retro.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','Retro.csv'), index= False)