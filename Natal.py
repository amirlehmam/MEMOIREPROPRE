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

# FillNA
Moon = Moon.copy()
Moon.fillna(0, inplace=True)
lat_moon_changes = lat_moon_changes.copy()
lat_moon_changes.fillna(0, inplace=True)
planet_node = planet_node.copy()
planet_node.fillna(0, inplace=True)

# **XV. Natal**

today = datetime.strftime(datetime.now(), "%d/%m/%Y")
t = pd.to_datetime(today)
t = pd.to_datetime(t)

cumulative_1 = helio_cum.copy()
cumulative_2 = helio_cum.copy()
cumulative_3 = helio_cum.copy()
cumulative_4 = helio_cum.copy()
cumulative_5 = helio_cum.copy()
cumulative_6 = helio_cum.copy()
cumulative_7 = helio_cum.copy()
cumulative_8 = helio_cum.copy()
cumulative_9 = helio_cum.copy()
cumulative_10 = helio_cum.copy()
cumulative_11 = helio_cum.copy()
cumulative_12 = helio_cum.copy()
cumulative_13 = helio_cum.copy()

helio = helio.copy()
test = helio_cum.copy()

result = helio[helio.Date == today]

def cum_hel(df, date):
    today = datetime.strftime(datetime.now(), "%d/%m/%Y")
    return pd.DataFrame(
        {
            "Date": [date],
            "Earth": df["Earth"][df.Date == today].values
            - df["Earth"][df.Date == date].values,
            "Mer": df["Mer"][df.Date == today].values
            - df["Mer"][df.Date == date].values,
            "Ven": df["Ven"][df.Date == today].values
            - df["Ven"][df.Date == date].values,
            "Mar": df["Mar"][df.Date == today].values
            - df["Mar"][df.Date == date].values,
            "Jup": df["Jup"][df.Date == today].values
            - df["Jup"][df.Date == date].values,
            "Sat": df["Sat"][df.Date == today].values
            - df["Sat"][df.Date == date].values,
            "Ura": df["Ura"][df.Date == today].values
            - df["Ura"][df.Date == date].values,
            "Nep": df["Nep"][df.Date == today].values
            - df["Nep"][df.Date == date].values,
            "Plu": df["Plu"][df.Date == today].values
            - df["Plu"][df.Date == date].values,
        }
    )

filtered_dfs = []

data = [
  (cumulative_1, '31/10/2008'),
  (cumulative_2, '03/01/2009'),
  (cumulative_3, '22/05/2010'),
  (cumulative_4, '29/11/2013'),
  (cumulative_5, '17/12/2017'),
  (cumulative_6, '15/12/2018'),
  (cumulative_7, '26/06/2019'),
  (cumulative_8, '12/03/2020'),
  (cumulative_9, '25/04/2021'),
  (cumulative_10, '20/07/2021'),
  (cumulative_11, '20/10/2021'),
  (cumulative_12, '10/11/2021'),
  (cumulative_13, '18/06/2022'),
]

for i, (df, date) in enumerate(data):
  filtered_dfs.append(cum_hel(df, date))

cumm_hel = pd.concat(filtered_dfs)
hel = pd.concat([result, cumm_hel])
hel = hel.round()

## 1. Code
### NATAL

# 31/10/2008

helcunn = helio_cum.copy() # DF WHERE I GET THE DATES (df_2)
helcunn = helcunn.round()

helcunn['Date'] = pd.to_datetime(helcunn['Date'], format="%d/%m/%Y")
date_filter = "01/01/2000"
date_filter = pd.to_datetime(date_filter)

helcunn = helcunn[helcunn['Date'] > date_filter]

s_d = "31/10/2008"
nat = natal.copy()
nat_h = nat.copy()

nat_h.Degrees = nat_h.Planets.map(helio.set_index("Date").loc[s_d])
nat_h.Start_Date = nat_h.Planets.map(helio_cum.set_index("Date").loc[s_d])
nat_h.Now = nat_h.Planets.map(helio_cum.set_index("Date").loc[today])
nat_h.Cycles = (nat_h.Now - nat_h.Start_Date) / nat_h.Degrees

nat_h['Cycles'] = nat_h['Cycles'].iloc[::].apply(np.floor)

nat_h['0'] = (nat_h.Cycles * nat_h.Degrees) + nat_h.Start_Date
nat_h['1'] = ((nat_h.Cycles + 1) * (nat_h.Degrees)) + nat_h.Start_Date
nat_h['2'] = ((nat_h.Cycles + 2) * (nat_h.Degrees)) + nat_h.Start_Date
nat_h['3'] = ((nat_h.Cycles + 3) * (nat_h.Degrees)) + nat_h.Start_Date
nat_h['4'] = ((nat_h.Cycles + 4) * (nat_h.Degrees)) + nat_h.Start_Date
nat_h['5'] = ((nat_h.Cycles + 5) * (nat_h.Degrees)) + nat_h.Start_Date
nat_h['6'] = ((nat_h.Cycles + 6) * (nat_h.Degrees)) + nat_h.Start_Date
nat_h['7'] = ((nat_h.Cycles + 7) * (nat_h.Degrees)) + nat_h.Start_Date
nat_h['8'] = ((nat_h.Cycles + 8) * (nat_h.Degrees)) + nat_h.Start_Date
nat_h['9'] = ((nat_h.Cycles + 9) * (nat_h.Degrees)) + nat_h.Start_Date

nat_h['0'] = nat_h['0'].round()
nat_h['1'] = nat_h['1'].round()
nat_h['2'] = nat_h['2'].round()
nat_h['3'] = nat_h['3'].round()
nat_h['4'] = nat_h['4'].round()
nat_h['5'] = nat_h['5'].round()
nat_h['6'] = nat_h['6'].round()
nat_h['7'] = nat_h['7'].round()
nat_h['8'] = nat_h['8'].round()
nat_h['9'] = nat_h['9'].round()

nat_test = nat_h.copy() # DF WHERE I WANT TO REPLACE DEGREES VALUES BY THEIR CORRESPONDING DATES (df_1)

dates              = helcunn.melt(id_vars="Date", var_name="Planets")
numeric_cols       = nat_test.columns[nat_test.columns.str.fullmatch("\d+")]
pairs              = nat_test.set_index("Planets").filter(numeric_cols).stack().droplevel(-1).reset_index(name="value")
mapper             = pd.merge_asof(pairs.astype({"value": float}).sort_values("value"),
                                   dates.astype({"value": float}).sort_values("value"),
                                   on="value",
                                   direction="forward").set_index("value")["Date"]

nat_test[numeric_cols] = nat_test[numeric_cols].replace(mapper)

nat_test

# 03/01/2009

helcunn = helio_cum.copy() # DF WHERE I GET THE DATES (df_2)
helcunn = helcunn.round()

helcunn['Date'] = pd.to_datetime(helcunn['Date'])
date_filter = "01/01/2000"
date_filter = pd.to_datetime(date_filter)

helcunn = helcunn[helcunn['Date'] > date_filter]

s_d1 = "03/01/2009"
nat = natal.copy()
nat_2 = nat.copy()

nat_2.Degrees = nat_2.Planets.map(helio.set_index("Date").loc[s_d1])
nat_2.Start_Date = nat_2.Planets.map(helio_cum.set_index("Date").loc[s_d1])
nat_2.Now = nat_2.Planets.map(helio_cum.set_index("Date").loc[today])
nat_2.Cycles = (nat_2.Now - nat_2.Start_Date) / nat_2.Degrees

nat_2['Cycles'] = nat_2['Cycles'].iloc[::].apply(np.floor)

nat_2['0'] = (nat_2.Cycles * nat_2.Degrees) + nat_2.Start_Date
nat_2['1'] = ((nat_2.Cycles + 1) * (nat_2.Degrees)) + nat_2.Start_Date
nat_2['2'] = ((nat_2.Cycles + 2) * (nat_2.Degrees)) + nat_2.Start_Date
nat_2['3'] = ((nat_2.Cycles + 3) * (nat_2.Degrees)) + nat_2.Start_Date
nat_2['4'] = ((nat_2.Cycles + 4) * (nat_2.Degrees)) + nat_2.Start_Date
nat_2['5'] = ((nat_2.Cycles + 5) * (nat_2.Degrees)) + nat_2.Start_Date
nat_2['6'] = ((nat_2.Cycles + 6) * (nat_2.Degrees)) + nat_2.Start_Date
nat_2['7'] = ((nat_2.Cycles + 7) * (nat_2.Degrees)) + nat_2.Start_Date
nat_2['8'] = ((nat_2.Cycles + 8) * (nat_2.Degrees)) + nat_2.Start_Date
nat_2['9'] = ((nat_2.Cycles + 9) * (nat_2.Degrees)) + nat_2.Start_Date

nat_2['0'] = nat_2['0'].round()
nat_2['1'] = nat_2['1'].round()
nat_2['2'] = nat_2['2'].round()
nat_2['3'] = nat_2['3'].round()
nat_2['4'] = nat_2['4'].round()
nat_2['5'] = nat_2['5'].round()
nat_2['6'] = nat_2['6'].round()
nat_2['7'] = nat_2['7'].round()
nat_2['8'] = nat_2['8'].round()
nat_2['9'] = nat_2['9'].round()

nat_test2 = nat_2.copy() # DF WHERE I WANT TO REPLACE DEGREES VALUES BY THEIR CORRESPONDING DATES (df_1)

dates              = helcunn.melt(id_vars="Date", var_name="Planets")
numeric_cols       = nat_test2.columns[nat_test2.columns.str.fullmatch("\d+")]
pairs              = nat_test2.set_index("Planets").filter(numeric_cols).stack().droplevel(-1).reset_index(name="value")
mapper             = pd.merge_asof(pairs.astype({"value": float}).sort_values("value"),
                                   dates.astype({"value": float}).sort_values("value"),
                                   on="value",
                                   direction="forward").set_index("value")["Date"]

nat_test2[numeric_cols] = nat_test2[numeric_cols].replace(mapper)

nat_test2

# 22/05/2010

helcunn = helio_cum.copy() # DF WHERE I GET THE DATES (df_2)
helcunn = helcunn.round()

helcunn['Date'] = pd.to_datetime(helcunn['Date'])
date_filter = "2000/01/01"
date_filter = pd.to_datetime(date_filter)

helcunn = helcunn[helcunn['Date'] > date_filter]

s_d2 = "22/05/2010"
nat = natal.copy()
nat_3 = nat.copy()

nat_3.Degrees = nat_3.Planets.map(helio.set_index("Date").loc[s_d2])
nat_3.Start_Date = nat_3.Planets.map(helio_cum.set_index("Date").loc[s_d2])
nat_3.Now = nat_3.Planets.map(helio_cum.set_index("Date").loc[today])
nat_3.Cycles = (nat_3.Now - nat_3.Start_Date) / nat_3.Degrees

nat_3['Cycles'] = nat_3['Cycles'].iloc[::].apply(np.floor)

nat_3['0'] = (nat_3.Cycles * nat_3.Degrees) + nat_3.Start_Date
nat_3['1'] = ((nat_3.Cycles + 1) * (nat_3.Degrees)) + nat_3.Start_Date
nat_3['2'] = ((nat_3.Cycles + 2) * (nat_3.Degrees)) + nat_3.Start_Date
nat_3['3'] = ((nat_3.Cycles + 3) * (nat_3.Degrees)) + nat_3.Start_Date
nat_3['4'] = ((nat_3.Cycles + 4) * (nat_3.Degrees)) + nat_3.Start_Date
nat_3['5'] = ((nat_3.Cycles + 5) * (nat_3.Degrees)) + nat_3.Start_Date
nat_3['6'] = ((nat_3.Cycles + 6) * (nat_3.Degrees)) + nat_3.Start_Date
nat_3['7'] = ((nat_3.Cycles + 7) * (nat_3.Degrees)) + nat_3.Start_Date
nat_3['8'] = ((nat_3.Cycles + 8) * (nat_3.Degrees)) + nat_3.Start_Date
nat_3['9'] = ((nat_3.Cycles + 9) * (nat_3.Degrees)) + nat_3.Start_Date

nat_3['0'] = nat_3['0'].round()
nat_3['1'] = nat_3['1'].round()
nat_3['2'] = nat_3['2'].round()
nat_3['3'] = nat_3['3'].round()
nat_3['4'] = nat_3['4'].round()
nat_3['5'] = nat_3['5'].round()
nat_3['6'] = nat_3['6'].round()
nat_3['7'] = nat_3['7'].round()
nat_3['8'] = nat_3['8'].round()
nat_3['9'] = nat_3['9'].round()

nat_test3 = nat_3.copy() # DF WHERE I WANT TO REPLACE DEGREES VALUES BY THEIR CORRESPONDING DATES (df_1)

dates              = helcunn.melt(id_vars="Date", var_name="Planets")
numeric_cols       = nat_test3.columns[nat_test3.columns.str.fullmatch("\d+")]
pairs              = nat_test3.set_index("Planets").filter(numeric_cols).stack().droplevel(-1).reset_index(name="value")
mapper             = pd.merge_asof(pairs.astype({"value": float}).sort_values("value"),
                                   dates.astype({"value": float}).sort_values("value"),
                                   on="value",
                                   direction="forward").set_index("value")["Date"]

nat_test3[numeric_cols] = nat_test3[numeric_cols].replace(mapper)

nat_test3
# 17/12/2017

helcunn = helio_cum.copy() # DF WHERE I GET THE DATES (df_2)
helcunn = helcunn.round()

helcunn['Date'] = pd.to_datetime(helcunn['Date'])
date_filter = "2000/01/01"
date_filter = pd.to_datetime(date_filter)

helcunn = helcunn[helcunn['Date'] > date_filter]

s_d3 = "17/12/2017"
nat = natal.copy()
nat_4 = nat.copy()

nat_4.Degrees = nat_4.Planets.map(helio.set_index("Date").loc[s_d3])
nat_4.Start_Date = nat_4.Planets.map(helio_cum.set_index("Date").loc[s_d3])
nat_4.Now = nat_4.Planets.map(helio_cum.set_index("Date").loc[today])
nat_4.Cycles = (nat_4.Now - nat_4.Start_Date) / nat_4.Degrees

nat_4['Cycles'] = nat_4['Cycles'].iloc[::].apply(np.floor)

nat_4['0'] = (nat_4.Cycles * nat_4.Degrees) + nat_4.Start_Date
nat_4['1'] = ((nat_4.Cycles + 1) * (nat_4.Degrees)) + nat_4.Start_Date
nat_4['2'] = ((nat_4.Cycles + 2) * (nat_4.Degrees)) + nat_4.Start_Date
nat_4['3'] = ((nat_4.Cycles + 3) * (nat_4.Degrees)) + nat_4.Start_Date
nat_4['4'] = ((nat_4.Cycles + 4) * (nat_4.Degrees)) + nat_4.Start_Date
nat_4['5'] = ((nat_4.Cycles + 5) * (nat_4.Degrees)) + nat_4.Start_Date
nat_4['6'] = ((nat_4.Cycles + 6) * (nat_4.Degrees)) + nat_4.Start_Date
nat_4['7'] = ((nat_4.Cycles + 7) * (nat_4.Degrees)) + nat_4.Start_Date
nat_4['8'] = ((nat_4.Cycles + 8) * (nat_4.Degrees)) + nat_4.Start_Date
nat_4['9'] = ((nat_4.Cycles + 9) * (nat_4.Degrees)) + nat_4.Start_Date

nat_4['0'] = nat_4['0'].round()
nat_4['1'] = nat_4['1'].round()
nat_4['2'] = nat_4['2'].round()
nat_4['3'] = nat_4['3'].round()
nat_4['4'] = nat_4['4'].round()
nat_4['5'] = nat_4['5'].round()
nat_4['6'] = nat_4['6'].round()
nat_4['7'] = nat_4['7'].round()
nat_4['8'] = nat_4['8'].round()
nat_4['9'] = nat_4['9'].round()

nat_test4 = nat_4.copy() # DF WHERE I WANT TO REPLACE DEGREES VALUES BY THEIR CORRESPONDING DATES (df_1)

dates              = helcunn.melt(id_vars="Date", var_name="Planets")
numeric_cols       = nat_test4.columns[nat_test4.columns.str.fullmatch("\d+")]
pairs              = nat_test4.set_index("Planets").filter(numeric_cols).stack().droplevel(-1).reset_index(name="value")
mapper             = pd.merge_asof(pairs.astype({"value": float}).sort_values("value"),
                                   dates.astype({"value": float}).sort_values("value"),
                                   on="value",
                                   direction="forward").set_index("value")["Date"]

nat_test4[numeric_cols] = nat_test4[numeric_cols].replace(mapper)

nat_test4
# 12/03/2020

helcunn = helio_cum.copy() # DF WHERE I GET THE DATES (df_2)
helcunn = helcunn.round()

helcunn['Date'] = pd.to_datetime(helcunn['Date'])
date_filter = "2000/01/01"
date_filter = pd.to_datetime(date_filter)

helcunn = helcunn[helcunn['Date'] > date_filter]

s_d4 = "12/03/2020"
nat = natal.copy()
nat_5 = nat.copy()

nat_5.Degrees = nat_5.Planets.map(helio.set_index("Date").loc[s_d4])
nat_5.Start_Date = nat_5.Planets.map(helio_cum.set_index("Date").loc[s_d4])
nat_5.Now = nat_5.Planets.map(helio_cum.set_index("Date").loc[today])
nat_5.Cycles = (nat_5.Now - nat_5.Start_Date) / nat_5.Degrees

nat_5['Cycles'] = nat_5['Cycles'].iloc[::].apply(np.floor)

nat_5['0'] = (nat_5.Cycles * nat_5.Degrees) + nat_5.Start_Date
nat_5['1'] = ((nat_5.Cycles + 1) * (nat_5.Degrees)) + nat_5.Start_Date
nat_5['2'] = ((nat_5.Cycles + 2) * (nat_5.Degrees)) + nat_5.Start_Date
nat_5['3'] = ((nat_5.Cycles + 3) * (nat_5.Degrees)) + nat_5.Start_Date
nat_5['4'] = ((nat_5.Cycles + 4) * (nat_5.Degrees)) + nat_5.Start_Date
nat_5['5'] = ((nat_5.Cycles + 5) * (nat_5.Degrees)) + nat_5.Start_Date
nat_5['6'] = ((nat_5.Cycles + 6) * (nat_5.Degrees)) + nat_5.Start_Date
nat_5['7'] = ((nat_5.Cycles + 7) * (nat_5.Degrees)) + nat_5.Start_Date
nat_5['8'] = ((nat_5.Cycles + 8) * (nat_5.Degrees)) + nat_5.Start_Date
nat_5['9'] = ((nat_5.Cycles + 9) * (nat_5.Degrees)) + nat_5.Start_Date

nat_5['0'] = nat_5['0'].round()
nat_5['1'] = nat_5['1'].round()
nat_5['2'] = nat_5['2'].round()
nat_5['3'] = nat_5['3'].round()
nat_5['4'] = nat_5['4'].round()
nat_5['5'] = nat_5['5'].round()
nat_5['6'] = nat_5['6'].round()
nat_5['7'] = nat_5['7'].round()
nat_5['8'] = nat_5['8'].round()
nat_5['9'] = nat_5['9'].round()

nat_test5 = nat_5.copy() # DF WHERE I WANT TO REPLACE DEGREES VALUES BY THEIR CORRESPONDING DATES (df_1)

dates              = helcunn.melt(id_vars="Date", var_name="Planets")
numeric_cols       = nat_test5.columns[nat_test5.columns.str.fullmatch("\d+")]
pairs              = nat_test5.set_index("Planets").filter(numeric_cols).stack().droplevel(-1).reset_index(name="value")
mapper             = pd.merge_asof(pairs.astype({"value": float}).sort_values("value"),
                                   dates.astype({"value": float}).sort_values("value"),
                                   on="value",
                                   direction="forward").set_index("value")["Date"]

nat_test5[numeric_cols] = nat_test5[numeric_cols].replace(mapper)

nat_test5
# 25/04/2021

helcunn = helio_cum.copy() # DF WHERE I GET THE DATES (df_2)
helcunn = helcunn.round()

helcunn['Date'] = pd.to_datetime(helcunn['Date'])
date_filter = "2000/01/01"
date_filter = pd.to_datetime(date_filter)

helcunn = helcunn[helcunn['Date'] > date_filter]

s_d5 = "25/04/2021"
nat = natal.copy()
nat_6 = nat.copy()

nat_6.Degrees = nat_6.Planets.map(helio.set_index("Date").loc[s_d5])
nat_6.Start_Date = nat_6.Planets.map(helio_cum.set_index("Date").loc[s_d5])
nat_6.Now = nat_6.Planets.map(helio_cum.set_index("Date").loc[today])
nat_6.Cycles = (nat_6.Now - nat_6.Start_Date) / nat_6.Degrees

nat_6['Cycles'] = nat_6['Cycles'].iloc[::].apply(np.floor)

nat_6['0'] = (nat_6.Cycles * nat_6.Degrees) + nat_6.Start_Date
nat_6['1'] = ((nat_6.Cycles + 1) * (nat_6.Degrees)) + nat_6.Start_Date
nat_6['2'] = ((nat_6.Cycles + 2) * (nat_6.Degrees)) + nat_6.Start_Date
nat_6['3'] = ((nat_6.Cycles + 3) * (nat_6.Degrees)) + nat_6.Start_Date
nat_6['4'] = ((nat_6.Cycles + 4) * (nat_6.Degrees)) + nat_6.Start_Date
nat_6['5'] = ((nat_6.Cycles + 5) * (nat_6.Degrees)) + nat_6.Start_Date
nat_6['6'] = ((nat_6.Cycles + 6) * (nat_6.Degrees)) + nat_6.Start_Date
nat_6['7'] = ((nat_6.Cycles + 7) * (nat_6.Degrees)) + nat_6.Start_Date
nat_6['8'] = ((nat_6.Cycles + 8) * (nat_6.Degrees)) + nat_6.Start_Date
nat_6['9'] = ((nat_6.Cycles + 9) * (nat_6.Degrees)) + nat_6.Start_Date

nat_6['0'] = nat_6['0'].round()
nat_6['1'] = nat_6['1'].round()
nat_6['2'] = nat_6['2'].round()
nat_6['3'] = nat_6['3'].round()
nat_6['4'] = nat_6['4'].round()
nat_6['5'] = nat_6['5'].round()
nat_6['6'] = nat_6['6'].round()
nat_6['7'] = nat_6['7'].round()
nat_6['8'] = nat_6['8'].round()
nat_6['9'] = nat_6['9'].round()

nat_test6 = nat_6.copy() # DF WHERE I WANT TO REPLACE DEGREES VALUES BY THEIR CORRESPONDING DATES (df_1)

dates              = helcunn.melt(id_vars="Date", var_name="Planets")
numeric_cols       = nat_test6.columns[nat_test6.columns.str.fullmatch("\d+")]
pairs              = nat_test6.set_index("Planets").filter(numeric_cols).stack().droplevel(-1).reset_index(name="value")
mapper             = pd.merge_asof(pairs.astype({"value": float}).sort_values("value"),
                                   dates.astype({"value": float}).sort_values("value"),
                                   on="value",
                                   direction="forward").set_index("value")["Date"]

nat_test6[numeric_cols] = nat_test6[numeric_cols].replace(mapper)

nat_test6
# 10/11/2021

helcunn = helio_cum.copy() # DF WHERE I GET THE DATES (df_2)
helcunn = helcunn.round()

helcunn['Date'] = pd.to_datetime(helcunn['Date'])
date_filter = "2000/01/01"
date_filter = pd.to_datetime(date_filter)

helcunn = helcunn[helcunn['Date'] > date_filter]

s_d6 = "10/11/2021"
nat = natal.copy()
nat_7 = nat.copy()

nat_7.Degrees = nat_7.Planets.map(helio.set_index("Date").loc[s_d6])
nat_7.Start_Date = nat_7.Planets.map(helio_cum.set_index("Date").loc[s_d6])
nat_7.Now = nat_7.Planets.map(helio_cum.set_index("Date").loc[today])
nat_7.Cycles = (nat_7.Now - nat_7.Start_Date) / nat_7.Degrees

nat_7['Cycles'] = nat_7['Cycles'].iloc[::].apply(np.floor)

nat_7['0'] = (nat_7.Cycles * nat_7.Degrees) + nat_7.Start_Date
nat_7['1'] = ((nat_7.Cycles + 1) * (nat_7.Degrees)) + nat_7.Start_Date
nat_7['2'] = ((nat_7.Cycles + 2) * (nat_7.Degrees)) + nat_7.Start_Date
nat_7['3'] = ((nat_7.Cycles + 3) * (nat_7.Degrees)) + nat_7.Start_Date
nat_7['4'] = ((nat_7.Cycles + 4) * (nat_7.Degrees)) + nat_7.Start_Date
nat_7['5'] = ((nat_7.Cycles + 5) * (nat_7.Degrees)) + nat_7.Start_Date
nat_7['6'] = ((nat_7.Cycles + 6) * (nat_7.Degrees)) + nat_7.Start_Date
nat_7['7'] = ((nat_7.Cycles + 7) * (nat_7.Degrees)) + nat_7.Start_Date
nat_7['8'] = ((nat_7.Cycles + 8) * (nat_7.Degrees)) + nat_7.Start_Date
nat_7['9'] = ((nat_7.Cycles + 9) * (nat_7.Degrees)) + nat_7.Start_Date

nat_7['0'] = nat_7['0'].round()
nat_7['1'] = nat_7['1'].round()
nat_7['2'] = nat_7['2'].round()
nat_7['3'] = nat_7['3'].round()
nat_7['4'] = nat_7['4'].round()
nat_7['5'] = nat_7['5'].round()
nat_7['6'] = nat_7['6'].round()
nat_7['7'] = nat_7['7'].round()
nat_7['8'] = nat_7['8'].round()
nat_7['9'] = nat_7['9'].round()

nat_test7 = nat_7.copy() # DF WHERE I WANT TO REPLACE DEGREES VALUES BY THEIR CORRESPONDING DATES (df_1)

dates              = helcunn.melt(id_vars="Date", var_name="Planets")
numeric_cols       = nat_test7.columns[nat_test7.columns.str.fullmatch("\d+")]
pairs              = nat_test7.set_index("Planets").filter(numeric_cols).stack().droplevel(-1).reset_index(name="value")
mapper             = pd.merge_asof(pairs.astype({"value": float}).sort_values("value"),
                                   dates.astype({"value": float}).sort_values("value"),
                                   on="value",
                                   direction="forward").set_index("value")["Date"]

nat_test7[numeric_cols] = nat_test7[numeric_cols].replace(mapper)

nat_test7
# 18/06/2022

helcunn = helio_cum.copy() # DF WHERE I GET THE DATES (df_2)
helcunn = helcunn.round()

helcunn['Date'] = pd.to_datetime(helcunn['Date'])
date_filter = "2000/01/01"
date_filter = pd.to_datetime(date_filter)

helcunn = helcunn[helcunn['Date'] > date_filter]

s_d7 = "18/06/2022"
nat = natal.copy()
nat_8 = nat.copy()

nat_8.Degrees = nat_8.Planets.map(helio.set_index("Date").loc[s_d7])
nat_8.Start_Date = nat_8.Planets.map(helio_cum.set_index("Date").loc[s_d7])
nat_8.Now = nat_8.Planets.map(helio_cum.set_index("Date").loc[today])
nat_8.Cycles = (nat_8.Now - nat_8.Start_Date) / nat_8.Degrees

nat_8['Cycles'] = nat_8['Cycles'].iloc[::].apply(np.floor)

nat_8['0'] = (nat_8.Cycles * nat_8.Degrees) + nat_8.Start_Date
nat_8['1'] = ((nat_8.Cycles + 1) * (nat_8.Degrees)) + nat_8.Start_Date
nat_8['2'] = ((nat_8.Cycles + 2) * (nat_8.Degrees)) + nat_8.Start_Date
nat_8['3'] = ((nat_8.Cycles + 3) * (nat_8.Degrees)) + nat_8.Start_Date
nat_8['4'] = ((nat_8.Cycles + 4) * (nat_8.Degrees)) + nat_8.Start_Date
nat_8['5'] = ((nat_8.Cycles + 5) * (nat_8.Degrees)) + nat_8.Start_Date
nat_8['6'] = ((nat_8.Cycles + 6) * (nat_8.Degrees)) + nat_8.Start_Date
nat_8['7'] = ((nat_8.Cycles + 7) * (nat_8.Degrees)) + nat_8.Start_Date
nat_8['8'] = ((nat_8.Cycles + 8) * (nat_8.Degrees)) + nat_8.Start_Date
nat_8['9'] = ((nat_8.Cycles + 9) * (nat_8.Degrees)) + nat_8.Start_Date

nat_8['0'] = nat_8['0'].round()
nat_8['1'] = nat_8['1'].round()
nat_8['2'] = nat_8['2'].round()
nat_8['3'] = nat_8['3'].round()
nat_8['4'] = nat_8['4'].round()
nat_8['5'] = nat_8['5'].round()
nat_8['6'] = nat_8['6'].round()
nat_8['7'] = nat_8['7'].round()
nat_8['8'] = nat_8['8'].round()
nat_8['9'] = nat_8['9'].round()

nat_test8 = nat_8.copy() # DF WHERE I WANT TO REPLACE DEGREES VALUES BY THEIR CORRESPONDING DATES (df_1)

dates              = helcunn.melt(id_vars="Date", var_name="Planets")
numeric_cols       = nat_test8.columns[nat_test8.columns.str.fullmatch("\d+")]
pairs              = nat_test8.set_index("Planets").filter(numeric_cols).stack().droplevel(-1).reset_index(name="value")
mapper             = pd.merge_asof(pairs.astype({"value": float}).sort_values("value"),
                                   dates.astype({"value": float}).sort_values("value"),
                                   on="value",
                                   direction="forward").set_index("value")["Date"]

nat_test8[numeric_cols] = nat_test8[numeric_cols].replace(mapper)

nat_test8
nat = pd.concat([nat_test, nat_test2, nat_test3, nat_test4, nat_test5, nat_test6, nat_test7, nat_test8])
nat = nat.drop(columns=['Planets', 'Degrees', 'Start_Date', 'Now', 'Cycles'])
### Revs

revgui = hel.copy()

revgui['Earth'] = revgui['Earth'] / 360
revgui['Mer'] = revgui['Mer'] / 360
revgui['Ven'] = revgui['Ven'] / 360
revgui['Mar'] = revgui['Mar'] / 360
revgui['Jup'] = revgui['Jup'] / 360
revgui['Sat'] = revgui['Sat'] / 360
revgui['Nep'] = revgui['Nep'] / 360
revgui['Plu'] = revgui['Plu'] / 360

revgui = revgui.iloc[::, revgui.columns !='Date'].apply(np.floor)
revgui = revgui.drop(columns=['Sat', 'Ura', 'Nep', 'Plu'])
revgui = revgui.iloc[1: , :]

# 31/10/2008

import datetime

starting_date = datetime.datetime.strptime("31/10/2008", "%d/%m/%Y")

input1 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [13, 57, 22, 7, 1],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output1 = pd.DataFrame()

for col in input1.columns[0:3]:
    output1[col] = input1[col]

for col in input1.columns[3:]:
    output1[col] = input1[col]
    for row, _ in input1.iterrows():
        delta = f'{int(input1["Days"][row] * (input1["Rev"][row] + int(col)))} days'
        output1[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output1
# 03/01/2009

import datetime

starting_date = datetime.datetime.strptime("03/01/2009", "%d/%m/%Y")

input2 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [13, 56, 22, 7, 1],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output2 = pd.DataFrame()

for col in input2.columns[0:3]:
    output2[col] = input2[col]

for col in input2.columns[3:]:
    output2[col] = input2[col]
    for row, _ in input2.iterrows():
        delta = f'{int(input2["Days"][row] * (input2["Rev"][row] + int(col)))} days'
        output2[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output2
# 22/05/2010

import datetime

starting_date = datetime.datetime.strptime("22/05/2010", "%d/%m/%Y")

input3 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [12, 51, 20, 6, 1],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output3 = pd.DataFrame()

for col in input3.columns[0:3]:
    output3[col] = input3[col]

for col in input3.columns[3:]:
    output3[col] = input3[col]
    for row, _ in input3.iterrows():
        delta = f'{int(input3["Days"][row] * (input3["Rev"][row] + int(col)))} days'
        output3[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output3
# 29/11/2013

import datetime

starting_date = datetime.datetime.strptime("29/11/2013", "%d/%m/%Y")

input4 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [8, 36, 14, 4, 0.72],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output4 = pd.DataFrame()

for col in input4.columns[0:3]:
    output4[col] = input4[col]

for col in input4.columns[3:]:
    output4[col] = input4[col]
    for row, _ in input4.iterrows():
        delta = f'{int(input4["Days"][row] * (input4["Rev"][row] + int(col)))} days'
        output4[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output4
# 29/11/2013

import datetime

starting_date = datetime.datetime.strptime("29/11/2013", "%d/%m/%Y")

input4 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [8, 36, 14, 4, 0.72],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output4 = pd.DataFrame()

for col in input4.columns[0:3]:
    output4[col] = input4[col]

for col in input4.columns[3:]:
    output4[col] = input4[col]
    for row, _ in input4.iterrows():
        delta = f'{int(input4["Days"][row] * (input4["Rev"][row] + int(col)))} days'
        output4[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output4
# 17/12/2017

import datetime

starting_date = datetime.datetime.strptime("17/12/2017", "%d/%m/%Y")

input5 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [4, 19, 7, 2, 0.40],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output5 = pd.DataFrame()

for col in input5.columns[0:3]:
    output5[col] = input5[col]

for col in input5.columns[3:]:
    output5[col] = input5[col]
    for row, _ in input5.iterrows():
        delta = f'{int(input5["Days"][row] * (input5["Rev"][row] + int(col)))} days'
        output5[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output5
# 15/12/2018

import datetime

starting_date = datetime.datetime.strptime("15/12/2018", "%d/%m/%Y")

input6 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [3, 15, 6, 2, 0.32],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output6 = pd.DataFrame()

for col in input6.columns[0:3]:
    output6[col] = input6[col]

for col in input6.columns[3:]:
    output6[col] = input6[col]
    for row, _ in input6.iterrows():
        delta = f'{int(input6["Days"][row] * (input6["Rev"][row] + int(col)))} days'
        output6[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output6
# 26/06/2019

import datetime

starting_date = datetime.datetime.strptime("26/06/2019", "%d/%m/%Y")

input7 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [3, 13, 5, 1.71, 0.28],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output7 = pd.DataFrame()

for col in input7.columns[0:3]:
    output7[col] = input7[col]

for col in input7.columns[3:]:
    output7[col] = input7[col]
    for row, _ in input7.iterrows():
        delta = f'{int(input7["Days"][row] * (input7["Rev"][row] + int(col)))} days'
        output7[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output7
# 12/03/2020

import datetime

starting_date = datetime.datetime.strptime("12/03/2020", "%d/%m/%Y")

input8 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [2, 10, 4, 1.38, 0.22],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output8 = pd.DataFrame()

for col in input8.columns[0:3]:
    output8[col] = input8[col]

for col in input8.columns[3:]:
    output8[col] = input8[col]
    for row, _ in input8.iterrows():
        delta = f'{int(input8["Days"][row] * (input8["Rev"][row] + int(col)))} days'
        output8[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output8
# 25/04/2021

import datetime

starting_date = datetime.datetime.strptime("25/04/2021", "%d/%m/%Y")

input9 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [1, 5, 2, 0.73, 0.12],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output9 = pd.DataFrame()

for col in input9.columns[0:3]:
    output9[col] = input9[col]

for col in input9.columns[3:]:
    output9[col] = input9[col]
    for row, _ in input9.iterrows():
        delta = f'{int(input9["Days"][row] * (input9["Rev"][row] + int(col)))} days'
        output9[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output9
# 20/07/2021

import datetime

starting_date = datetime.datetime.strptime("20/07/2021", "%d/%m/%Y")

input10 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [1, 4, 1.85, 0.63, 0.10],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output10 = pd.DataFrame()

for col in input10.columns[0:3]:
    output10[col] = input10[col]

for col in input10.columns[3:]:
    output10[col] = input10[col]
    for row, _ in input10.iterrows():
        delta = f'{int(input10["Days"][row] * (input10["Rev"][row] + int(col)))} days'
        output10[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output10
# 20/10/2021

import datetime

starting_date = datetime.datetime.strptime("20/10/2021", "%d/%m/%Y")

input11 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [1, 3.64, 1.45, 0.52, 0.08],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output11 = pd.DataFrame()

for col in input11.columns[0:3]:
    output11[col] = input11[col]

for col in input11.columns[3:]:
    output11[col] = input11[col]
    for row, _ in input11.iterrows():
        delta = f'{int(input11["Days"][row] * (input11["Rev"][row] + int(col)))} days'
        output11[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output11
# 10/11/2021

import datetime

starting_date = datetime.datetime.strptime("10/11/2021", "%d/%m/%Y")

input12 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [1, 3.34, 1.35, 0.49, 0.07],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output12 = pd.DataFrame()

for col in input12.columns[0:3]:
    output12[col] = input12[col]

for col in input12.columns[3:]:
    output12[col] = input12[col]
    for row, _ in input12.iterrows():
        delta = f'{int(input12["Days"][row] * (input12["Rev"][row] + int(col)))} days'
        output12[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output12
# 18/06/2022

import datetime

starting_date = datetime.datetime.strptime("18/06/2022", "%d/%m/%Y")

input13 = pd.DataFrame({"Planets": ["Earth", "Mer", "Ven", "Mar", "Jup"],
                       "Days": [365.2425, 88, 225, 687, 4330.6],
                       "Rev": [1, 0.97, 0.38, 0.14, 0.02],
                       "0": "",
                       "1": "",
                       "2": "",
                       "3": ""
                       })
                       
output13 = pd.DataFrame()

for col in input13.columns[0:3]:
    output13[col] = input13[col]

for col in input13.columns[3:]:
    output13[col] = input13[col]
    for row, _ in input13.iterrows():
        delta = f'{int(input13["Days"][row] * (input13["Rev"][row] + int(col)))} days'
        output13[col][row] = (starting_date + pd.to_timedelta(delta)).strftime('%d/%m/%Y')

output13
revgood = pd.concat([output1, output2, output3, output4, output5, output6, output7, output8, output9, output10, output11, output12, output13])
revgood = revgood.drop(columns=['Planets', 'Days', 'Rev'])
naters = pd.concat([nat, revgood])

flugg1 = naters.copy()

gdeg2 = flugg1.unstack().value_counts(ascending=True)

gdeg2 = pd.DataFrame(gdeg2, columns=['Hit'])

gdeg2 = gdeg2.reset_index()
gdeg2 = gdeg2.rename_axis('E', axis=1)
gdeg2.columns = gdeg2.columns.str.replace('index', 'Date')
gdeg2 = gdeg2.rename_axis(None, axis=1)

#deg = gdeg2.sort_values(by=['Date'], ascending=True)
gdeg2.drop(gdeg2.head(1).index,inplace=True) # drop first n rows

gdeg2['Date'] = gdeg2['Date'].apply(pd.to_datetime, format = "%d/%m/%Y")

start_date = t  - timedelta(days = 1)
end_date = t + timedelta(days = 360)

mask = (gdeg2['Date'] > start_date) & (gdeg2['Date'] <= end_date)
gdeg2 = gdeg2.loc[mask]

naters_hits = gdeg2.sort_values(by=['Date'], ascending=True)
dz_Natal = naters_hits.head(30)
dz_Natal.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','Natal.csv'), index= False)