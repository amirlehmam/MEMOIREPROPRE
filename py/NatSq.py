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
NatSq = NatSq.copy()
NatSq = NatSq.drop(['Type'], axis=1)

# Match every dates to cols

for col in NatSq.columns[1:]:
    NatSq[col] = ((pd.to_datetime(NatSq['Date']) + pd.to_timedelta(f'{col} days'))
               .dt.strftime('%Y/%m/%d'))

dx = NatSq[1:].unstack().value_counts(ascending=False)

dx = pd.DataFrame(dx, columns=['Hit'])

dx = dx.reset_index()
dx = dx.rename_axis('E', axis=1)
dx.columns = dx.columns.str.replace('index', 'Date')
dx = dx.rename_axis(None, axis=1)

dx['Date'] = pd.to_datetime(dx['Date'])  

start_date = t  - timedelta(days = 5)
end_date = t + timedelta(days = 120)

mask = (dx['Date'] > start_date) & (dx['Date'] <= end_date)
NatSq_hits = dx.loc[mask]
NatSq_hits = NatSq_hits.sort_values(by=['Date'])

print(NatSq_hits.head(5))

fig = px.bar(NatSq_hits, x='Date', y='Hit')
fig.show()