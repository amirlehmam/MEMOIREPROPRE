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
today = pd.to_datetime(twoday)
today = pd.to_datetime(today)

# **III. ASPECTS TABLE & TOOLS.py**
### **III.1 Aspects H/G TrTr & TrNa**
#### **III.1.1 HELIO TrTr & TrNa**

# H_TrTr

TrTr = TrTr.copy()
helio_ap = TrTr[TrTr["Type"] == "Helio"]
helio_TrTr = helio_ap[helio_ap.Date == today]
helio_TrTr = helio_TrTr.set_index('Date')

# H_TrNa

TrNa = TrNa.copy()
helio_TrNa = TrNa[TrNa["Type"] == "Helio"]
helio_TrNa = helio_TrNa[helio_TrNa.Date == today]
helio_TrNa = helio_TrNa.set_index('Date')

#### **III.1.2 GEO TrTr & TrNa**
# G_TrTr

geo_ap = TrTr[TrTr["Type"] == "Geo"]
geo_TrTr = geo_ap[geo_ap.Date == today]
geo_TrTr = geo_TrTr.set_index('Date')

# G_TrNa

geo_TrNa = TrNa[TrNa["Type"] == "Geo"]
geo_TrNa = geo_TrNa[geo_TrNa.Date == today]
geo_TrNa = geo_TrNa.set_index('Date')

### **III.2 Retro**

#*(0 = rien | 1 = RETRO | 2 = RETURN)*
# Remove the nan and fill the empty string
retro = retro.copy()
retro.fillna('')
retro = retro.replace(np.nan,'',regex = True)
retro1 = retro[retro.Date == today]

### **III.3 Declinations**
# dec_lat

selected_date = today
lat_moon_changes = lat_moon_changes.copy()
dec_lat = pd.DataFrame({'Date': [selected_date],
                                       'Dec/Lat': lat_moon_changes['LatChanges'][lat_moon_changes.Date == today].values
                                       + lat_moon_changes['MoonChanges'][lat_moon_changes.Date == selected_date].values,
                                       })

### **III.4 GEO TOOLS**
# GEO TOOLS

declinations = declinations.copy()
latitudes = latitudes.copy()
Moon = Moon.copy()
planet_node = planet_node.copy()
samedec_samelat = samedec_samelat.copy()

tools_con = pd.concat([declinations, lat_moon_changes, latitudes, Moon, planet_node, samedec_samelat])
tools = pd.DataFrame({'Date': [today],

                                       'New Moon': Moon['NewMoon'][Moon.Date == today].values,

                                       'Full Moon': Moon['FullMoon'][Moon.Date == today].values,

                                       'Node': planet_node['Planet Node'][planet_node.Date == today].values,

                                       'Same Dec': samedec_samelat['Same Dec'][samedec_samelat.Date == today].values,        

                                       'Same Lat': samedec_samelat['Same Lat'][samedec_samelat.Date == today].values,

                                       'Lat Changes': lat_moon_changes['LatChanges'][lat_moon_changes.Date == today].values,    

                                       'Moon Changes': lat_moon_changes['MoonChanges'][lat_moon_changes.Date == today].values,

                                       'Lat Changes': lat_moon_changes['LatChanges'][lat_moon_changes.Date == today].values,       
                                                                                                             
})

tools.fillna('')
tools = tools.replace(0, np.nan)
tools = tools.replace(np.nan,'',regex = True)


dz_TrTr_Asp = helio_TrTr
dz_TrTr_Asp.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','aspects_h_tr.csv'), index = False)

dz_TrNa_Asp = helio_TrNa
dz_TrNa_Asp.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','aspects_h_na.csv'), index = False)

dz_Gtr_Asp = geo_TrTr
dz_Gtr_Asp.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','aspects_g_tr.csv'), index = False)

dz_Gna_Asp = geo_TrNa
dz_Gna_Asp.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','aspects_g_na.csv'), index = False)

dz_Retr = retro[retro.Date == today]
dz_Retr.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','retro_asp.csv'), index= False)

dz_dec_lat = dec_lat[dec_lat.Date == today]
dz_dec_lat.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','dec_lat.csv'), index= False)

dz_tools = tools[tools.Date == today]
dz_tools.to_csv(os.path.join('STREAMLIT//streamlit//streamlit//data','tools.csv'), index= False)