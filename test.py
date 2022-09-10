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

today = datetime.strftime(datetime.now(), "%d/%m/%Y")

today = datetime.strftime(datetime.now(), "%d/%m/%Y")

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

# mod30 (donne qu'elle signe il est)

mod = pd.DataFrame({'Date': [today],

                                       'Earth': helio['Earth'][helio.Date == today].values
                                       % 30,

                                       'Mer': helio['Mer'][helio.Date == today].values
                                       % 30,
                                       
                                       'Ven': helio['Ven'][helio.Date == today].values
                                       % 30,

                                       'Mar': helio['Mar'][helio.Date == today].values
                                       % 30,

                                       'Jup': helio['Jup'][helio.Date == today].values
                                       % 30,
                                       
                                       'Sat': helio['Sat'][helio.Date == today].values
                                       % 30,

                                       'Ura': helio['Ura'][helio.Date == today].values
                                       % 30,

                                       'Nep': helio['Nep'][helio.Date == today].values
                                       % 30,
                                       
                                       'Plu': helio['Plu'][helio.Date == today].values
                                       % 30,

                                       })


mod = mod.round()

# rrr

result2 = result.copy() # rrr

for col in result2.columns[1:]:
     result2= result2.astype({col: "int64"})

for col in result2.columns[1:]:
     result2= result2.astype({col: "int64"})

rrr = pd.DataFrame({'Date': [today],

                                       'Earth': helio['Earth'][helio.Date == today].values,

                                       'Mer': helio['Mer'][helio.Date == today].values,
                                       
                                       'Ven': helio['Ven'][helio.Date == today].values,

                                       'Mar': helio['Mar'][helio.Date == today].values,

                                       'Jup': helio['Jup'][helio.Date == today].values,
                                       
                                       'Sat': helio['Sat'][helio.Date == today].values,

                                       'Ura': helio['Ura'][helio.Date == today].values,

                                       'Nep': helio['Nep'][helio.Date == today].values,
                                       
                                       'Plu': helio['Plu'][helio.Date == today].values,

                                       })

rrr = rrr.round()

for i in rrr['Earth']: 
        if (0<=i<=29):
            rrr['Earth'] = rrr['Earth'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr['Earth'] = rrr['Earth'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr['Earth'] = rrr['Earth'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr['Earth'] = rrr['Earth'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr['Earth'] = rrr['Earth'].replace(i, "Le")
        elif (150<=i<=179):
            rrr['Earth'] = rrr['Earth'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr['Earth'] = rrr['Earth'].replace(i, "Li")
        elif (209<=i<=239):
            rrr['Earth'] = rrr['Earth'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr['Earth'] = rrr['Earth'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr['Earth'] = rrr['Earth'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr['Earth'] = rrr['Earth'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr['Earth'] = rrr['Earth'].replace(i, "Pi")

for i in rrr['Mer']: 
        if (0<=i<=29):
            rrr['Mer'] = rrr['Mer'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr['Mer'] = rrr['Mer'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr['Mer'] = rrr['Mer'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr['Mer'] = rrr['Mer'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr['Mer'] = rrr['Mer'].replace(i, "Le")
        elif (150<=i<=179):
            rrr['Mer'] = rrr['Mer'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr['Mer'] = rrr['Mer'].replace(i, "Li")
        elif (209<=i<=239):
            rrr['Mer'] = rrr['Mer'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr['Mer'] = rrr['Mer'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr['Mer'] = rrr['Mer'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr['Mer'] = rrr['Mer'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr['Mer'] = rrr['Mer'].replace(i, "Pi")

for i in rrr['Ven']: 
        if (0<=i<=29):
            rrr['Ven'] = rrr['Ven'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr['Ven'] = rrr['Ven'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr['Ven'] = rrr['Ven'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr['Ven'] = rrr['Ven'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr['Ven'] = rrr['Ven'].replace(i, "Le")
        elif (150<=i<=179):
            rrr['Ven'] = rrr['Ven'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr['Ven'] = rrr['Ven'].replace(i, "Li")
        elif (209<=i<=239):
            rrr['Ven'] = rrr['Ven'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr['Ven'] = rrr['Ven'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr['Ven'] = rrr['Ven'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr['Ven'] = rrr['Ven'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr['Ven'] = rrr['Ven'].replace(i, "Pi")

for i in rrr['Mar']: 
        if (0<=i<=29):
            rrr['Mar'] = rrr['Mar'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr['Mar'] = rrr['Mar'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr['Mar'] = rrr['Mar'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr['Mar'] = rrr['Mar'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr['Mar'] = rrr['Mar'].replace(i, "Le")
        elif (150<=i<=179):
            rrr['Mar'] = rrr['Mar'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr['Mar'] = rrr['Mar'].replace(i, "Li")
        elif (209<=i<=239):
            rrr['Mar'] = rrr['Mar'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr['Mar'] = rrr['Mar'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr['Mar'] = rrr['Mar'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr['Mar'] = rrr['Mar'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr['Mar'] = rrr['Mar'].replace(i, "Pi")

for i in rrr['Jup']: 
        if (0<=i<=29):
            rrr['Jup'] = rrr['Jup'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr['Jup'] = rrr['Jup'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr['Jup'] = rrr['Jup'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr['Jup'] = rrr['Jup'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr['Jup'] = rrr['Jup'].replace(i, "Le")
        elif (150<=i<=179):
            rrr['Jup'] = rrr['Jup'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr['Jup'] = rrr['Jup'].replace(i, "Li")
        elif (209<=i<=239):
            rrr['Jup'] = rrr['Jup'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr['Jup'] = rrr['Jup'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr['Jup'] = rrr['Jup'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr['Jup'] = rrr['Jup'].replace(i, "Aq")
        elif (330<=i<=360):
            rrr['Jup'] = rrr['Jup'].replace(i, "Pi")

for i in rrr['Sat']: 
        if (0<=i<=29):
            rrr['Sat'] = rrr['Sat'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr['Sat'] = rrr['Sat'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr['Sat'] = rrr['Sat'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr['Sat'] = rrr['Sat'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr['Sat'] = rrr['Sat'].replace(i, "Le")
        elif (150<=i<=179):
            rrr['Sat'] = rrr['Sat'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr['Sat'] = rrr['Sat'].replace(i, "Li")
        elif (209<=i<=239):
            rrr['Sat'] = rrr['Sat'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr['Sat'] = rrr['Sat'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr['Sat'] = rrr['Sat'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr['Sat'] = rrr['Sat'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr['Sat'] = rrr['Sat'].replace(i, "Pi")

for i in rrr['Ura']: 
        if (0<=i<=29):
            rrr['Ura'] = rrr['Ura'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr['Ura'] = rrr['Ura'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr['Ura'] = rrr['Ura'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr['Ura'] = rrr['Ura'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr['Ura'] = rrr['Ura'].replace(i, "Le")
        elif (150<=i<=179):
            rrr['Ura'] = rrr['Ura'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr['Ura'] = rrr['Ura'].replace(i, "Li")
        elif (209<=i<=239):
            rrr['Ura'] = rrr['Ura'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr['Ura'] = rrr['Ura'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr['Ura'] = rrr['Ura'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr['Ura'] = rrr['Ura'].replace(i, "Aq")
        elif (330<=i<=360):
            rrr['Ura'] = rrr['Ura'].replace(i, "Pi")

for i in rrr['Nep']: 
        if (0<=i<=29):
            rrr['Nep'] = rrr['Nep'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr['Nep'] = rrr['Nep'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr['Nep'] = rrr['Nep'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr['Nep'] = rrr['Nep'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr['Nep'] = rrr['Nep'].replace(i, "Le")
        elif (150<=i<=179):
            rrr['Nep'] = rrr['Nep'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr['Nep'] = rrr['Nep'].replace(i, "Li")
        elif (209<=i<=239):
            rrr['Nep'] = rrr['Nep'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr['Nep'] = rrr['Nep'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr['Nep'] = rrr['Nep'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr['Nep'] = rrr['Nep'].replace(i, "Aq")
        elif (330<=i<=360):
            rrr['Nep'] = rrr['Nep'].replace(i, "Pi")

for i in rrr['Plu']: 
        if (0<=i<=29):
            rrr['Plu'] = rrr['Plu'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr['Plu'] = rrr['Plu'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr['Plu'] = rrr['Plu'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr['Plu'] = rrr['Plu'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr['Plu'] = rrr['Plu'].replace(i, "Le")
        elif (150<=i<=179):
            rrr['Plu'] = rrr['Plu'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr['Plu'] = rrr['Plu'].replace(i, "Li")
        elif (209<=i<=239):
            rrr['Plu'] = rrr['Plu'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr['Plu'] = rrr['Plu'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr['Plu'] = rrr['Plu'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr['Plu'] = rrr['Plu'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr['Plu'] = rrr['Plu'].replace(i, "Pi")

mod = mod.round()

# STR

for col in mod.columns[1:]:
     mod = mod.astype({col: str})

for col in rrr.columns[1:]:
     rrr = rrr.astype({col: str})

mod0 = pd.DataFrame({"Date": [today]})

# GROUPBY MANUALY

for col in mod.columns[1:]:
    mod0[col] = mod[col] + ' | ' + rrr[col] #.groupby('Date').agg('-'.join).reset_index()
    
# BON CUM MOD/REV

hexx = hel.copy()

hexx['Earth'] = hexx['Earth'] / 360
hexx['Mer'] = hexx['Mer'] / 360
hexx['Ven'] = hexx['Ven'] / 360
hexx['Mar'] = hexx['Mar'] / 360
hexx['Jup'] = hexx['Jup'] / 360
hexx['Sat'] = hexx['Sat'] / 360
hexx['Nep'] = hexx['Nep'] / 360
hexx['Plu'] = hexx['Plu'] / 360

hecc = hel.copy()

hecc['Earth'] = hecc['Earth'] % 360
hecc['Mer'] = hecc['Mer'] % 360
hecc['Ven'] = hecc['Ven'] % 360
hecc['Mar'] = hecc['Mar'] % 360
hecc['Jup'] = hecc['Jup'] % 360
hecc['Sat'] = hecc['Sat'] % 360
hecc['Nep'] = hecc['Nep'] % 360
hecc['Plu'] = hecc['Plu'] % 360

hexx = hexx.iloc[1: , :]
hecc = hecc.iloc[1:, :]

# ROUNDDOWN

hexx = hexx.iloc[::, hexx.columns !='Date'].apply(np.floor)
hecc = hecc.iloc[::, hecc.columns !='Date'].apply(np.floor)

# STR

for col in hexx.columns[::]:
     hexx = hexx.astype({col: str})

for col in hecc.columns[::]:
     hecc = hecc.astype({col: str})

puant = pd.DataFrame({"Date": cumm_hel['Date']})

# GROUPBY MANUALY

for col in hexx.columns[::]:
    puant[col] = hexx[col] + ' | ' + hecc[col] #.groupby('Date').agg('-'.join).reset_index()
    
helio_concat = pd.concat([cumm_hel, puant], axis=0)
helio_concat.Date = pd.to_datetime(helio_concat.Date)
helio_concat = helio_concat.sort_values("Date", ignore_index=True)
helio_concat.Date = helio_concat.Date.dt.strftime("%d/%m/%Y")

hcc = pd.concat([result, mod0, helio_concat])

ex = hcc.copy()
print(ex)