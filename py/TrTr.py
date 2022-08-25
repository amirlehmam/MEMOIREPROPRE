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

b = points_tr.copy()

b.fillna(0, inplace=True)

b_h = b[b["Type"] == "Helio"]
b_g = b[b["Type"] == "Geo"]

b_h = b_h.drop(['Type'], axis = 1)
b_g = b_g.drop(['Type'], axis = 1)
b_con = pd.concat([b_h, b_g])

b_con['Date'] = pd.to_datetime(b_con['Date'])  

start_date = t  - timedelta(days = 5)
end_date = t + timedelta(days = 120)

mask = (b_con['Date'] > start_date) & (b_con['Date'] <= end_date)
b_hits = b_con.loc[mask]
b_hits = b_hits.sort_values(by=['Date'], ascending = True)
b_trtr = b_hits

print(b_trtr.head(5))

fig = px.bar(b_trtr, x='Date', y='Points')
fig.show()