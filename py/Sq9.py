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

print(sq9g)