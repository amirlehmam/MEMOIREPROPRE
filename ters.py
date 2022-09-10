import pandas as pd
import numpy as np
from datetime import date
from datetime import datetime
from datetime import timedelta
import plotly.express as px
import os

z = pd.read_csv('fuctue.csv')
z = z.round(2)

print(z)

