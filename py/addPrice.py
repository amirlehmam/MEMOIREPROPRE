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
## 1. Code

kek_p = helio.copy()
hexxx = helio[helio.Date == "31/10/2008"]
pa = priceadd.copy()

outp = pd.DataFrame()

for col in pa.columns:
    outp[col] = pa[col]

    if col not in ("Date", "Price"):
        
        for row, _ in helio.iterrows():
            date = helio["Date"][row]
            dates_list = pa["Date"].to_list()

            if date in dates_list:
                row_index = dates_list.index(date)
                outp[col][row_index] = helio[col][row]

output = outp.copy()

print(outp)
# PA_1000

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

pa1k = output.copy()
pa1k.Price = pa1k.Price / 1000 # <- change here

# Add price to all planets

for i in pa1k.columns[2:]:
    pa1k[i] = pa1k[i] + pa1k.Price

# if > 360 then -360 so it can stay within the circle 

for i in pa1k.columns[2:]:
    for num, j in enumerate(pa1k[i]):
        j = float(j)
        if j > 360:
            x = j - 360
            pa1k[i].iloc[num] = x

# for loop to catch which degrees is situated at which date in the future/past

for planets in pa1k.columns[2:]:
    for num, i in enumerate(pa1k[planets]):
        df_copy = helio.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            pa1k[planets].iloc[num] = Date_ok
        else:
            pa1k[planets].iloc[num] = " "

# PA_100

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

pa100 = output.copy()
pa100.Price = pa100.Price / 100 # <- change here

# Add price to all planets

for i in pa100.columns[2:]:
    pa100[i] = pa100[i] + pa100.Price

# if > 360 then -360 so it can stay within the circle 

for i in pa100.columns[2:]:
    for num, j in enumerate(pa100[i]):
        j = float(j)
        if j > 360:
            x = j - 360
            pa100[i].iloc[num] = x

# for loop to catch which degrees is situated at which date in the future/past

for planets in pa100.columns[2:]:
    for num, i in enumerate(pa100[planets]):
        df_copy = helio.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            pa100[planets].iloc[num] = Date_ok
        else:
            pa100[planets].iloc[num] = " "

# PA_10

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

pa10 = output.copy()
pa10.Price = pa10.Price / 10 # <- change here

# Add price to all planets

for i in pa10.columns[2:]:
    pa10[i] = pa10[i] + pa10.Price

# if > 360 then -360 so it can stay within the circle 

for i in pa10.columns[2:]:
    for num, j in enumerate(pa10[i]):
        j = float(j)
        if j > 360:
            x = j - 360
            pa10[i].iloc[num] = x

# for loop to catch which degrees is situated at which date in the future/past

for planets in pa10.columns[2:]:
    for num, i in enumerate(pa10[planets]):
        df_copy = helio.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            pa10[planets].iloc[num] = Date_ok
        else:
            pa10[planets].iloc[num] = " "

# PA_1

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

pa1 = output.copy()
pa1.Price = pa1.Price / 1 # <- change here

# Add price to all planets

for i in pa1.columns[2:]:
    pa1[i] = pa1[i] + pa1.Price

# if > 360 then -360 so it can stay within the circle 

for i in pa1.columns[2:]:
    for num, j in enumerate(pa1[i]):
        j = float(j)
        if j > 360:
            x = j - 360
            pa1[i].iloc[num] = x

# for loop to catch which degrees is situated at which date in the future/past

for planets in pa1.columns[2:]:
    for num, i in enumerate(pa1[planets]):
        df_copy = helio.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            pa1[planets].iloc[num] = Date_ok
        else:
            pa1[planets].iloc[num] = " "

# PA_24:

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

pa24 = output.copy()
pa24.Price = pa24.Price / 24 # <- change here

# Add price to all planets

for i in pa24.columns[2:]:
    pa24[i] = pa24[i] + pa24.Price

# if > 360 then -360 so it can stay within the circle 

for i in pa24.columns[2:]:
    for num, j in enumerate(pa24[i]):
        j = float(j)
        if j > 360:
            x = j - 360
            pa24[i].iloc[num] = x

# for loop to catch which degrees is situated at which date in the future/past

for planets in pa24.columns[2:]:
    for num, i in enumerate(pa24[planets]):
        df_copy = helio.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            pa24[planets].iloc[num] = Date_ok
        else:
            pa24[planets].iloc[num] = " "

# PA_263:

# Copy price + Initialization of divisions
# (1000,100,10,1,24,etc...)

pa263 = output.copy()
pa263.Price = pa263.Price / 263 # <- change here

# Add price to all planets

for i in pa263.columns[2:]:
    pa263[i] = pa263[i] + pa263.Price

# if > 360 then -360 so it can stay within the circle 

for i in pa263.columns[2:]:
    for num, j in enumerate(pa263[i]):
        j = float(j)
        if j > 360:
            x = j - 360
            pa263[i].iloc[num] = x

# for loop to catch which degrees is situated at which date in the future/past

for planets in pa263.columns[2:]:
    for num, i in enumerate(pa263[planets]):
        df_copy = helio.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            pa263[planets].iloc[num] = Date_ok
        else:
            pa263[planets].iloc[num] = " "

# PA_1440:

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

pa1440 = output.copy()
pa1440.Price = pa1440.Price / 1440 # <- change here

# Add price to all planets

for i in pa1440.columns[2:]:
    pa1440[i] = pa1440[i] + pa1440.Price

# if > 360 then -360 so it can stay within the circle 

for i in pa1440.columns[2:]:
    for num, j in enumerate(pa1440[i]):
        j = float(j)
        if j > 360:
            x = j - 360
            pa1440[i].iloc[num] = x

# for loop to catch which degrees is situated at which date in the future/past

for planets in pa1440.columns[2:]:
    for num, i in enumerate(pa1440[planets]):
        df_copy = helio.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            pa1440[planets].iloc[num] = Date_ok
        else:
            pa1440[planets].iloc[num] = " "

#### **HIT addP**
total_p = pd.concat([pa1k, pa100, pa10, pa1, pa24, pa263, pa1440])

adpod = total_p.copy()
adpod = adpod.drop(['Price'], axis=1)

good = adpod[1:].unstack().value_counts(ascending=True)

good = pd.DataFrame(good, columns=['Hit'])

good = good.reset_index()
good = good.rename_axis('E', axis=1)
good.columns = good.columns.str.replace('index', 'Date')
good = good.rename_axis(None, axis=1)

start_date = "10/08/2022"
end_date = "31/12/2025"

mask = (good['Date'] > start_date) & (good['Date'] <= end_date)
good = good.loc[mask]

# addp_hits.head(50)

good = good.sort_values(by=['Date'], ascending=True)

good['Date'] = good['Date'].apply(pd.to_datetime)

start_date = "10/08/2022"
end_date = "31/12/2025"

mask = (good['Date'] > start_date) & (good['Date'] <= end_date)
good = good.loc[mask]

# addp_hits.head(50)

good = good.sort_values(by=['Date'], ascending=True)
dz_ADDP = good.head(30)
dz_ADDP.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','addPrice.csv'), index= False)