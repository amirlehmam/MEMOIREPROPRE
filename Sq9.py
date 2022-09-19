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

sq9 = SQ9.copy()

q = sq9['Sq9']
sq9['0'] = d = pd.to_datetime(sq9['0'])

op1 = ((q).to_numpy().reshape(-1, 1) * (np.arange(1, 8)).reshape(1, -1))
sq9g = op1.astype('timedelta64[D]') + d.to_numpy().reshape(-1, 1)

sq9g = pd.DataFrame(sq9g, columns=['45', '90', '135', '180', '225','270','315'])

adpod = sq9g.copy()

dzea2 = adpod[1:].unstack().value_counts(ascending=True)

dzea2 = pd.DataFrame(dzea2, columns=['Hit'])

dzea2 = dzea2.reset_index()
dzea2 = dzea2.rename_axis('E', axis=1)
dzea2.columns = dzea2.columns.str.replace('index', 'Date')
dzea2 = dzea2.rename_axis(None, axis=1)

dzea2 = dzea2.sort_values(by=['Date'], ascending=True)

dzea2['Date'] = dzea2['Date'].apply(pd.to_datetime)

start_date = t  - timedelta(days = 1)
end_date = t + timedelta(days = 120)

mask = (dzea2['Date'] > start_date) & (dzea2['Date'] <= end_date)
dzea2 = dzea2.loc[mask]

# addp_hits.head(50)

ggggg = dzea2.sort_values(by=['Date'], ascending=True)
dz_Sq9 = ggggg.head(30)
dz_Sq9.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','Sq9.csv'), index= False)