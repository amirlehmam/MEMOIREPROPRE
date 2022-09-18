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

futdat = FutureDate.copy()
helio_cum = helio_cum.copy()

fdd = pd.DataFrame()

for col in futdat.columns:
    fdd[col] = futdat[col]

    if col not in ("Date", "Price"):
        
        for row, _ in helio_cum.iterrows():
            date = helio_cum["Date"][row]
            dates_list = futdat["Date"].to_list()

            if date in dates_list:
                row_index = dates_list.index(date)
                fdd[col][row_index] = helio_cum[col][row]

# FD15

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 15

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd15 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd15.columns[1:]:
    for num, i in enumerate(fd15[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd15[planets].iloc[num] = Date_ok
        else:
            fd15[planets].iloc[num] = " "

# FD30

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 30

fd30 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd30.columns[1:]:
    for num, i in enumerate(fd30[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd30[planets].iloc[num] = Date_ok
        else:
            fd30[planets].iloc[num] = " "

# FD45

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 45

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd45 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd45.columns[1:]:
    for num, i in enumerate(fd45[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd45[planets].iloc[num] = Date_ok
        else:
            fd45[planets].iloc[num] = " "

# FD60

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 60

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd60 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd60.columns[1:]:
    for num, i in enumerate(fd60[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd60[planets].iloc[num] = Date_ok
        else:
            fd60[planets].iloc[num] = " "

# FD72

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 72

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd72 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd72.columns[1:]:
    for num, i in enumerate(fd72[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd72[planets].iloc[num] = Date_ok
        else:
            fd72[planets].iloc[num] = " "

# FD90

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 90

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd90 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd90.columns[1:]:
    for num, i in enumerate(fd90[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd90[planets].iloc[num] = Date_ok
        else:
            fd90[planets].iloc[num] = " "

# FD120

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 120

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd120 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd120.columns[1:]:
    for num, i in enumerate(fd120[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd120[planets].iloc[num] = Date_ok
        else:
            fd120[planets].iloc[num] = " "

# FD144

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 144

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd144 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd144.columns[1:]:
    for num, i in enumerate(fd144[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd144[planets].iloc[num] = Date_ok
        else:
            fd144[planets].iloc[num] = " "

# FD180

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 180

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd180 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd180.columns[1:]:
    for num, i in enumerate(fd180[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd180[planets].iloc[num] = Date_ok
        else:
            fd180[planets].iloc[num] = " "

# FD360

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 360

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd360 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd360.columns[1:]:
    for num, i in enumerate(fd360[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd360[planets].iloc[num] = Date_ok
        else:
            fd360[planets].iloc[num] = " "

# FD720

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 720

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd720 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd720.columns[1:]:
    for num, i in enumerate(fd720[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd720[planets].iloc[num] = Date_ok
        else:
            fd720[planets].iloc[num] = " "

# FD1080

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 1080

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd1080 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd1080.columns[1:]:
    for num, i in enumerate(fd1080[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd1080[planets].iloc[num] = Date_ok
        else:
            fd1080[planets].iloc[num] = " "

# FD1440

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 1440

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd1440 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd1440.columns[1:]:
    for num, i in enumerate(fd1440[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd1440[planets].iloc[num] = Date_ok
        else:
            fd1440[planets].iloc[num] = " "

# FD1800

output = pd.DataFrame()

output["Date"] = fdd["Date"]

for col in fdd.columns[1:]:
    output[col] = fdd[col].astype("float64") + 1800

# Copy price + Initialization of divides (1000,100,10,1,24,etc...)

fd1800 = output

# for loop to catch which degrees is situated at which date in the future/past

for planets in fd1800.columns[1:]:
    for num, i in enumerate(fd1800[planets]):
        df_copy = helio_cum.copy()
        target = df_copy[df_copy[planets] == float(i)]

        Date = []

        for date in target['Date']:
            Date.append(date)

        if len(Date) > 0:
            Date_ok = Date[-1]
            fd1800[planets].iloc[num] = Date_ok
        else:
            fd1800[planets].iloc[num] = " "

future_dates = pd.concat([fd15, fd30, fd45, fd60, fd72, fd90, fd120, fd144, fd180, fd360, fd720, fd1080, fd1440, fd1800])

adpod = future_dates.copy()

gfd = adpod[1:].unstack().value_counts(ascending=True)

gfd = pd.DataFrame(gfd, columns=['Hit'])

gfd = gfd.reset_index()
gfd = gfd.rename_axis('E', axis=1)
gfd.columns = gfd.columns.str.replace('index', 'Date')
gfd = gfd.rename_axis(None, axis=1)

gfd.drop(gfd.tail(1).index,inplace=True)

gfd['Date'] = pd.to_datetime(gfd['Date'])

start_date = t  - timedelta(days = 1)
end_date = t + timedelta(days = 120)

mask = (gfd['Date'] > start_date) & (gfd['Date'] <= end_date)
gfd = gfd.loc[mask]

gfd['Date'] = pd.to_datetime(gfd['Date'])

# addp_hits.head(50)

gfdE = gfd.sort_values(by=['Date'], ascending=True)
gfdE
lathit = lathit.copy()

ex = pd.concat([gfdE, lathit])
dz_FD = ex.head(30)
dz_FD.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','FutureDate.csv'), index= False)
dz_FD