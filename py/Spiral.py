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

# Match every dates to cols
from datetime import datetime
from datetime import timedelta

Spiral = Spiral.copy()

for col in Spiral.columns[1:]:
    Spiral[col] = ((pd.to_datetime(Spiral['Date']) + pd.to_timedelta(f'{col} days'))
               .dt.strftime('%d/%m/%Y'))

dx = Spiral[1:].unstack().value_counts(ascending=False)

dx = pd.DataFrame(dx, columns=['Hit'])

dx = dx.reset_index()
dx = dx.rename_axis('E', axis=1)
dx.columns = dx.columns.str.replace('index', 'Date')
dx = dx.rename_axis(None, axis=1)

dx['Date'] = pd.to_datetime(dx['Date'])  

dayyy = datetime.strftime(datetime.now(), "%Y/%m/%d")
t = pd.to_datetime(dayyy)
t = pd.to_datetime(t)

start_date = t  - timedelta(days = 5)
end_date = t + timedelta(days = 120)

mask = (dx['Date'] > start_date) & (dx['Date'] <= end_date)
Spiral_hits = dx.loc[mask]
Spiral_hits = Spiral_hits.sort_values(by=['Date'])

print(Spiral_hits.head(5))