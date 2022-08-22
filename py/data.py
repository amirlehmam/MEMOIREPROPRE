# Libraries

import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime
import plotly.express as px
import os

# Retrieve the path to the current folders
current_path = os.getcwd()

# Get the path to the csv file folder - in this case the 'data' file
csv_path = os.path.join(current_path, 'data\\test')

# A EXPLIQUER ICI
for file in os.listdir(csv_path):
    fd = pd.read_csv(os.path.join(csv_path, file))
    globals()[file.rpartition(".")[0]] = fd
    
Moon = Moon.copy()
Moon.fillna(0, inplace=True)

lat_moon_changes = lat_moon_changes.copy()
lat_moon_changes.fillna(0, inplace=True)

planet_node = planet_node.copy()
planet_node.fillna(0, inplace=True)