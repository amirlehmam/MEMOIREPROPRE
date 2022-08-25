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
fbb = pd.DataFrame()
helio_cum = helio_cum.copy()
fibs = fibs.copy()

for col in fibs.columns:
    fbb[col] = fibs[col]

    if col not in ("Date"):
        
        for row, _ in helio_cum.iterrows():
            date = helio_cum["Date"][row]
            dates_list = fibs["Date"].to_list()

            if date in dates_list:
                row_index = dates_list.index(date)
                fbb[col][row_index] = helio_cum[col][row]

dfs = []

for i in range(len(fbb["Date"]) - 1):
    new_df = fbb.copy()[i:]
    for k in new_df:
        if k == "Date":
            continue
        for j in range(i + 1, len(fbb[k])):
            new_df[k][j] = (float(new_df[k][i]) + ((float(new_df[k][j]) - float(new_df[k][i])) * 1.618))
        new_df[k][i] = 0
    dfs.append(new_df)

for df in dfs:
    print(df)
test = pd.concat(dfs)
test = test.round()
fbb1 = test.copy()

# for loop to catch which degrees is situated at which date in the future/past

for planets in fbb1.columns[1:]:
    for num, i in enumerate(fbb1[planets]):
        df_copy = helio_cum.round()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fbb1[planets].iloc[num] = Date_ok
        else:
            fbb1[planets].iloc[num] = " "

adpod = fbb1.copy()

gdeg = adpod[1:].unstack().value_counts(ascending=True)

gdeg = pd.DataFrame(gdeg, columns=['Hit'])

gdeg = gdeg.reset_index()
gdeg = gdeg.rename_axis('E', axis=1)
gdeg.columns = gdeg.columns.str.replace('index', 'Date')
gdeg = gdeg.rename_axis(None, axis=1)

gdeg = gdeg.sort_values(by=['Date'], ascending=True)
gdeg.drop(gdeg.head(1).index,inplace=True) # drop first n rows

gdeg['Date'] = gdeg['Date'].apply(pd.to_datetime)

start_date = t  - timedelta(days = 5)
end_date = t + timedelta(days = 120)

mask = (gdeg['Date'] > start_date) & (gdeg['Date'] <= end_date)
gdeg = gdeg.loc[mask]

fib_hits = gdeg.sort_values(by=['Date'], ascending=True)
print(fib_hits.head(5))