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

## **II.2 GEO**
### **II.2.1 CUMUL GEO**
from datetime import datetime

today = datetime.strftime(datetime.now(), "%d/%m/%Y")

cumulative_1 = geo_cum.copy()
cumulative_2 = geo_cum.copy()
cumulative_3 = geo_cum.copy()
cumulative_4 = geo_cum.copy()
cumulative_5 = geo_cum.copy()
cumulative_6 = geo_cum.copy()
cumulative_7 = geo_cum.copy()
cumulative_8 = geo_cum.copy()
cumulative_9 = geo_cum.copy()
cumulative_10 = geo_cum.copy()
cumulative_11 = geo_cum.copy()
cumulative_12 = geo_cum.copy()
cumulative_13 = geo_cum.copy()

geo = geo.copy()
result_g = geo[geo.Date == today]

def cum_geo(df, date):
    today = datetime.strftime(datetime.now(), "%d/%m/%Y")
    return pd.DataFrame(
        {
            "Date": [date],
            "Moon": df["Moon"][df.Date == today].values
            - df["Moon"][df.Date == date].values,
            "Sun": df["Sun"][df.Date == today].values
            - df["Sun"][df.Date == date].values,
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
  filtered_dfs.append(cum_geo(df, date))

cumm_geo = pd.concat(filtered_dfs)
geol = pd.concat([result_g, cumm_geo])
geol = geol.round()

### **II.2.2 MOD30 & 360 GEO**
#### **MOD30**
# mod30 (donne qu'elle signe il est)

mod_g = pd.DataFrame({'Date': [today],

                                       'Moon': result_g['Moon'][result_g.Date == today].values
                                       % 30,

                                        'Sun': result_g['Sun'][result_g.Date == today].values
                                       % 30,

                                       'Mer': result_g['Mer'][result_g.Date == today].values
                                       % 30,
                                       
                                       'Ven': result_g['Ven'][result_g.Date == today].values
                                       % 30,

                                       'Mar': result_g['Mar'][result_g.Date == today].values
                                       % 30,

                                       'Jup': result_g['Jup'][result_g.Date == today].values
                                       % 30,
                                       
                                       'Sat': result_g['Sat'][result_g.Date == today].values
                                       % 30,

                                       'Ura': result_g['Ura'][result_g.Date == today].values
                                       % 30,

                                       'Nep': result_g['Nep'][result_g.Date == today].values
                                       % 30,
                                       
                                       'Plu': result_g['Plu'][result_g.Date == today].values
                                       % 30,

                                       })

mod_g = mod_g.round()
# rrr

# mod30 (donne qu'elle signe il est)

rrr_g = result_g.copy() # rrr

for col in rrr_g.columns[1:]:
     rrr_g= rrr_g.astype({col: "int64"})

rrr_g = pd.DataFrame({'Date': [today],

                                       'Moon': rrr_g['Moon'][rrr_g.Date == today].values
                                       ,

                                        'Sun': rrr_g['Sun'][rrr_g.Date == today].values
                                       ,

                                       'Mer': rrr_g['Mer'][rrr_g.Date == today].values
                                       ,
                                       
                                       'Ven': rrr_g['Ven'][rrr_g.Date == today].values
                                       ,

                                       'Mar': rrr_g['Mar'][rrr_g.Date == today].values
                                       ,

                                       'Jup': rrr_g['Jup'][rrr_g.Date == today].values
                                       ,
                                       
                                       'Sat': rrr_g['Sat'][rrr_g.Date == today].values
                                       ,

                                       'Ura': rrr_g['Ura'][rrr_g.Date == today].values
                                       ,

                                       'Nep': rrr_g['Nep'][rrr_g.Date == today].values
                                       ,
                                       
                                       'Plu': rrr_g['Plu'][rrr_g.Date == today].values
                                       ,

                                       })

rrr_g = rrr_g.round()

for i in rrr_g['Moon']: 
        if (0<=i<=29):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Moon'] = rrr_g['Moon'].replace(i, "Pi")

for i in rrr_g['Sun']: 
        if (0<=i<=29):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Sun'] = rrr_g['Sun'].replace(i, "Pi")

for i in rrr_g['Mer']: 
        if (0<=i<=29):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Mer'] = rrr_g['Mer'].replace(i, "Pi")

for i in rrr_g['Ven']: 
        if (0<=i<=29):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Ven'] = rrr_g['Ven'].replace(i, "Pi")

for i in rrr_g['Mar']: 
        if (0<=i<=29):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Mar'] = rrr_g['Mar'].replace(i, "Pi")

for i in rrr_g['Jup']: 
        if (0<=i<=29):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Jup'] = rrr_g['Jup'].replace(i, "Pi")

for i in rrr_g['Sat']: 
        if (0<=i<=29):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Sat'] = rrr_g['Sat'].replace(i, "Pi")

for i in rrr_g['Ura']: 
        if (0<=i<=29):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Ura'] = rrr_g['Ura'].replace(i, "Pi")

for i in rrr_g['Nep']: 
        if (0<=i<=29):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Nep'] = rrr_g['Nep'].replace(i, "Pi")

for i in rrr_g['Plu']: 
        if (0<=i<=29):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Ar")
        elif (30<=i<=59):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Ta")
        elif (60<=i<=89):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Ge")
        elif (90<=i<=119):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Ca")
        elif (120<=i<=149):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Le")
        elif (150<=i<=179):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Vi")
        elif (180<=i<=209):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Li")
        elif (209<=i<=239):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Sc")
        elif (240<=i<=269):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Sg")
        elif (270<=i<=299):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Cp")
        elif (300<=i<=329):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Aq")
        elif (330<=i<=359):
            rrr_g['Plu'] = rrr_g['Plu'].replace(i, "Pi")

mod_g = mod_g.round()

# STR

for col in mod_g.columns[1:]:
     mod_g = mod_g.astype({col: str})

for col in rrr_g.columns[1:]:
     rrr_g = rrr_g.astype({col: str})

mod0_g = pd.DataFrame({"Date": [today]})

# GROUPBY MANUALY

for col in mod_g.columns[1:]:
    mod0_g[col] = mod_g[col] + ' | ' + rrr_g[col] #.groupby('Date').agg('-'.join).reset_index()
    
#### **MOD360**
# BON CUM MOD/REV

gexx = geol.copy()

gexx['Moon'] = gexx['Moon'] / 360
gexx['Sun'] = gexx['Sun'] / 360
gexx['Mer'] = gexx['Mer'] / 360
gexx['Ven'] = gexx['Ven'] / 360
gexx['Mar'] = gexx['Mar'] / 360
gexx['Jup'] = gexx['Jup'] / 360
gexx['Sat'] = gexx['Sat'] / 360
gexx['Nep'] = gexx['Nep'] / 360
gexx['Plu'] = gexx['Plu'] / 360

gecc = geol.copy()

gecc['Moon'] = gecc['Moon'] % 360
gecc['Sun'] = gecc['Sun'] % 360
gecc['Mer'] = gecc['Mer'] % 360
gecc['Ven'] = gecc['Ven'] % 360
gecc['Mar'] = gecc['Mar'] % 360
gecc['Jup'] = gecc['Jup'] % 360
gecc['Sat'] = gecc['Sat'] % 360
gecc['Nep'] = gecc['Nep'] % 360
gecc['Plu'] = gecc['Plu'] % 360

gexx = gexx.iloc[1: , :]
gecc = gecc.iloc[1:, :]

# ROUNDDOWN

gexx = gexx.iloc[::, gexx.columns !='Date'].apply(np.floor)
gecc = gecc.iloc[::, gecc.columns !='Date'].apply(np.floor)

# STR

for col in gexx.columns[::]:
     gexx = gexx.astype({col: str})

for col in gecc.columns[::]:
     gecc = gecc.astype({col: str})

puant_g = pd.DataFrame({"Date": cumm_geo['Date']})

# GROUPBY MANUALY

for col in gexx.columns[::]:
    puant_g[col] = gexx[col] + ' | ' + gecc[col] #.groupby('Date').agg('-'.join).reset_index()
    
### **II.2.3 CONCAT**
#concat_geo = pd.concat([result_g, mod0_g, cumulative_1_g, mod_1_g, cumulative_2_g, mod_2_g, cumulative_3_g, mod_3_g, cumulative_4_g, mod_4_g, cumulative_6_g, mod_6_g, cumulative_7_g, mod_7_g, cumulative_8_g, mod_8_g, cumulative_9_g, mod_9_g, cumulative_10_g, mod_10_g, cumulative_11_g, mod_11_g, cumulative_12_g, mod_12_g, cumulative_13_g, mod_13_g, cumulative_14_g, mod_14_g])
geo_concat = pd.concat([result_g, mod0_g, cumm_geo, puant_g], join='inner')

print(geo_concat)