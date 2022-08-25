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

x = points_na.copy()

twoday = datetime.strftime(datetime.now(), "%Y/%m/%d")
t = pd.to_datetime(twoday)
t = pd.to_datetime(t)

x.fillna(0, inplace=True)

x_h = x[x["Type"] == "Helio"]
x_g = x[x["Type"] == "Geo"]

x_h = x_h.drop(['Type'], axis = 1)
x_h = x_h.drop(['Angle'], axis = 1)
x_h = x_h.drop(['Pair'], axis = 1)

x_g = x_g.drop(['Type'], axis = 1)
x_g = x_g.drop(['Angle'], axis = 1)
x_g = x_g.drop(['Pair'], axis = 1)

x_con = pd.concat([x_h, x_g])

x_con['Date'] = pd.to_datetime(x_con['Date'])  
start_date = t  - timedelta(days = 5)
end_date = t + timedelta(days = 120)

mask = (x_con['Date'] > start_date) & (x_con['Date'] <= end_date)

x_hits = x_con.loc[mask]
x_hits = x_hits.sort_values(by=['Date'], ascending = True)
x_hi = x_con.loc[mask]
x_hi = x_hi.sort_values(by=['Date'], ascending = True)

print(x_hi.head(5))

fig = px.bar(x_hi, x='Date', y='Points')
fig.show()