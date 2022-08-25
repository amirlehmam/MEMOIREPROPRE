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
m = mult.copy()
m.head(5)

m['Date1'] = d1 = pd.to_datetime(m['Date1'])
m['Date2'] = d2 = pd.to_datetime(m['Date2'])
m['Date1'] = m['Date1'].dt.strftime('%Y/%m/%d')
m['Date2'] = m['Date2'].dt.strftime('%Y/%m/%d')
# PANDA VERSION

#from datetime import datetime 

#m618 = m.copy()

#for i, col in enumerate(m618.columns[2:]):
    #df1 = pd.to_datetime(m618['Date1'])
    #df2 = pd.to_datetime(m618['Date2'])
    #m618[col] =  df2 + ((df2 - df1) * (1.618 ** i))

#m618['Date1'] = pd.to_datetime(m618['Date1'])
#m618['Date2'] = pd.to_datetime(m618['Date2'])

#m618['Date1'] = m618['Date1'].dt.strftime('%Y/%m/%d')
#m618['Date2'] = m618['Date2'].dt.strftime('%Y/%m/%d')
#m618['1'] = m618['1'].dt.strftime('%Y/%m/%d')
#m618['2'] = m618['2'].dt.strftime('%Y/%m/%d')
#m618['3'] = m618['3'].dt.strftime('%Y/%m/%d')
#m618['4'] = m618['4'].dt.strftime('%Y/%m/%d')
#m618['5'] = m618['5'].dt.strftime('%Y/%m/%d')
#m618['6'] = m618['6'].dt.strftime('%Y/%m/%d')
#m618['7'] = m618['7'].dt.strftime('%Y/%m/%d')
#m618['8'] = m618['8'].dt.strftime('%Y/%m/%d')
#m618['9'] = m618['9'].dt.strftime('%Y/%m/%d')
#m618['10'] = m618['10'].dt.strftime('%Y/%m/%d')

#m618
# Vectorization Full 618

op618 = (d2 - d1).dt.days.to_numpy().reshape(-1, 1) * (1.618 ** np.arange(1, 11)).reshape(1, -1)
m618 = op618.astype('timedelta64[D]') + d2.to_numpy().reshape(-1, 1) 

m618 = pd.DataFrame(m618, columns=['1', '2', '3', '4', '5','6','7','8','9', '10'])

m618['1'] = m618['1'].dt.strftime('%Y/%m/%d')
m618['2'] = m618['2'].dt.strftime('%Y/%m/%d')
m618['3'] = m618['3'].dt.strftime('%Y/%m/%d')
m618['4'] = m618['4'].dt.strftime('%Y/%m/%d')
m618['5'] = m618['5'].dt.strftime('%Y/%m/%d')
m618['6'] = m618['6'].dt.strftime('%Y/%m/%d')
m618['7'] = m618['7'].dt.strftime('%Y/%m/%d')
m618['8'] = m618['8'].dt.strftime('%Y/%m/%d')
m618['9'] = m618['9'].dt.strftime('%Y/%m/%d')
m618['10'] = m618['10'].dt.strftime('%Y/%m/%d')

# Vectorization Full 414

op414 = (d2 - d1).dt.days.to_numpy().reshape(-1, 1) * (1.414 ** np.arange(1, 11)).reshape(1, -1)
m414 = op414.astype('timedelta64[D]') + d2.to_numpy().reshape(-1, 1) 

m414 = pd.DataFrame(m414, columns=['1', '2', '3', '4', '5','6','7','8','9', '10'])

m414['1'] = m414['1'].dt.strftime('%Y/%m/%d')
m414['2'] = m414['2'].dt.strftime('%Y/%m/%d')
m414['3'] = m414['3'].dt.strftime('%Y/%m/%d')
m414['4'] = m414['4'].dt.strftime('%Y/%m/%d')
m414['5'] = m414['5'].dt.strftime('%Y/%m/%d')
m414['6'] = m414['6'].dt.strftime('%Y/%m/%d')
m414['7'] = m414['7'].dt.strftime('%Y/%m/%d')
m414['8'] = m414['8'].dt.strftime('%Y/%m/%d')
m414['9'] = m414['9'].dt.strftime('%Y/%m/%d')
m414['10'] = m414['10'].dt.strftime('%Y/%m/%d')
# Vectorization Full 732

op732 = (d2 - d1).dt.days.to_numpy().reshape(-1, 1) * (1.732 ** np.arange(1, 11)).reshape(1, -1)
m732 = op732.astype('timedelta64[D]') + d2.to_numpy().reshape(-1, 1) 

m732 = pd.DataFrame(m732, columns=['1', '2', '3', '4', '5','6','7','8','9', '10'])

m732['1'] = m732['1'].dt.strftime('%Y/%m/%d')
m732['2'] = m732['2'].dt.strftime('%Y/%m/%d')
m732['3'] = m732['3'].dt.strftime('%Y/%m/%d')
m732['4'] = m732['4'].dt.strftime('%Y/%m/%d')
m732['5'] = m732['5'].dt.strftime('%Y/%m/%d')
m732['6'] = m732['6'].dt.strftime('%Y/%m/%d')
m732['7'] = m732['7'].dt.strftime('%Y/%m/%d')
m732['8'] = m732['8'].dt.strftime('%Y/%m/%d')
m732['9'] = m732['9'].dt.strftime('%Y/%m/%d')
m732['10'] = m732['10'].dt.strftime('%Y/%m/%d')

multi = pd.concat([m618, m414, m732])

tae = datetime.strftime(datetime.now(), "%d/%m/%Y")
tx = pd.to_datetime(tae)
tx = pd.to_datetime(tx)

adpod = multi.copy()

good = adpod[1:].unstack().value_counts(ascending=True)

good = pd.DataFrame(good, columns=['Hit'])

good = good.reset_index()
good = good.rename_axis('E', axis=1)
good.columns = good.columns.str.replace('index', 'Date')
good = good.rename_axis(None, axis=1)

start_date = tx  - timedelta(days = 5)
end_date = tx + timedelta(days = 120)

good['Date'] = pd.to_datetime(good['Date'])

mask = (good['Date'] > start_date) & (good['Date'] <= end_date)
good = good.loc[mask]

# addp_hits.head(50)

mult_hits = good.sort_values(by=['Date'], ascending=True)
print(mult_hits.head(5))