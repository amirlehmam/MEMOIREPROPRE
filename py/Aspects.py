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
# HELIO ASPECT TrTr - MADE BY US AUTOMATICALY FINDS INTO DATA

#ha = helio_asp
#col = []
#cols = ha.columns[1:]
#df = ha[cols]
#Date = list[ha['Date']]

#for columns in df.columns:

    #globals()["liste_%s"%columns] = []

    #for row, i in enumerate(df[columns]):
        #if (i >= 0 and i <= 0.03) or (i >= 3.75 and i <= 3.755) or (i >= 7.5 and i <= 7.55) or (i >= 15 and i <= 15.15) or (i >= 22.5 and i <= 22.55) or (i >= 30 and i <= 30.15) or (i >= 36 and i <= 36.15) or (i >= 45 and i <= 45.15) or (i >= 60 and i <= 60.15) or (i >= 72 and i <= 72.15) or (i >= 90 and i <= 90.15) or (i >= 120 and i <= 120.15) or (i >= 135 and i <= 135.15) or (i >= 144 and i <= 144.15) or (i >= 150 and i <= 150.15) or (i >= 180 and i <= 180.15):
            #globals()["liste_%s"%columns].append(i)
        #else:
            #globals()["liste_%s"%columns].append(" ")

#flu = helio_asp[['Date']].copy()
#dict = {'Sun_Mer': liste_Sun_Mer, 'Sun_Ven': liste_Sun_Ven, 'Sun_Mar': liste_Sun_Mar, 'Sun_Jup': liste_Sun_Jup, 'Sun_Sat': liste_Sun_Sat, 'Sun_Ura': liste_Sun_Ura, 'Sun_Nep': liste_Sun_Nep, 'Sun_Plu': liste_Sun_Plu, 'Mer_Ven': liste_Mer_Ven, 'Mer_Mar': liste_Mer_Mar, 'Mer_Jup': liste_Mer_Jup, 'Mer_Sat': liste_Mer_Sat, 'Mer_Ura': liste_Mer_Ura, 'Mer_Nep': liste_Mer_Nep, 'Mer_Plu': liste_Mer_Plu, 'Ven_Mar': liste_Ven_Mar, 'Ven_Jup': liste_Ven_Jup, 'Ven_Sat': liste_Ven_Sat, 'Ven_Ura': liste_Ven_Ura, 'Ven_Nep': liste_Ven_Nep, 'Ven_Plu': liste_Ven_Plu, 'Mar_Jup': liste_Mar_Jup, 'Mar_Sat': liste_Mar_Sat, 'Mar_Ura': liste_Mar_Ura, 'Mar_Nep': liste_Mar_Nep, 'Mar_Plu': liste_Mar_Plu, 'Jup_Sat': liste_Jup_Sat, 'Jup_Ura': liste_Jup_Ura, 'Jup_Nep': liste_Jup_Nep, 'Jup_Plu': liste_Jup_Plu, 'Sat_Ura': liste_Sat_Ura, 'Sat_Nep': liste_Sat_Nep, 'Sat_Plu': liste_Sat_Plu, 'Ura_Nep': liste_Ura_Nep, 'Ura_Plu': liste_Ura_Plu, 'Nep_Plu': liste_Nep_Plu} 
#dfObj = pd.DataFrame(dict)
#flu = helio_asp[['Date']].copy()
#concat_asp = pd.concat([flu, dfObj], axis=1)

#asp_con = concat_asp[concat_asp.Date == today]
#asp_con.round()
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

# GEO ASPECTS TrTr

#ga = geo_asp_good

#col = []
#cols = ha.columns[1:]
#df = ga[cols]
#Date = list[ga['Date']]

#for columns in df.columns:

    #globals()["lizte_%s"%columns] = []

    #for row, i in enumerate(df[columns]):
        #if (i >= 0 and i <= 0.03) or (i >= 3.75 and i <= 3.755) or (i >= 7.5 and i <= 7.59) or (i >= 15 and i <= 15.15) or (i >= 22.5 and i <= 22.55) or (i >= 30 and i <= 30.15) or (i >= 36 and i <= 36.15) or (i >= 45 and i <= 45.15) or (i >= 60 and i <= 60.15) or (i >= 72 and i <= 72.15) or (i >= 90 and i <= 90.15) or (i >= 120 and i <= 120.15) or (i >= 135 and i <= 135.15) or (i >= 144 and i <= 144.15) or (i >= 150 and i <= 150.15) or (i >= 180 and i <= 180.15):
        #    globals()["lizte_%s"%columns].append(i)
        #else:
          #  globals()["lizte_%s"%columns].append(" ")

#flu1 = geo_asp_good[['Date']].copy()
#dict = {'Sun_Mer': lizte_Sun_Mer, 'Sun_Ven': lizte_Sun_Ven, 'Sun_Mar': lizte_Sun_Mar, 'Sun_Jup': lizte_Sun_Jup, 'Sun_Sat': lizte_Sun_Sat, 'Sun_Ura': lizte_Sun_Ura, 'Sun_Nep': lizte_Sun_Nep, 'Sun_Plu': lizte_Sun_Plu, 'Mer_Ven': lizte_Mer_Ven, 'Mer_Mar': lizte_Mer_Mar, 'Mer_Jup': lizte_Mer_Jup, 'Mer_Sat': lizte_Mer_Sat, 'Mer_Ura': lizte_Mer_Ura, 'Mer_Nep': lizte_Mer_Nep, 'Mer_Plu': lizte_Mer_Plu, 'Ven_Mar': lizte_Ven_Mar, 'Ven_Jup': lizte_Ven_Jup, 'Ven_Sat': lizte_Ven_Sat, 'Ven_Ura': lizte_Ven_Ura, 'Ven_Nep': lizte_Ven_Nep, 'Ven_Plu': lizte_Ven_Plu, 'Mar_Jup': lizte_Mar_Jup, 'Mar_Sat': lizte_Mar_Sat, 'Mar_Ura': lizte_Mar_Ura, 'Mar_Nep': lizte_Mar_Nep, 'Mar_Plu': lizte_Mar_Plu, 'Jup_Sat': lizte_Jup_Sat, 'Jup_Ura': lizte_Jup_Ura, 'Jup_Nep': lizte_Jup_Nep, 'Jup_Plu': lizte_Jup_Plu, 'Sat_Ura': lizte_Sat_Ura, 'Sat_Nep': lizte_Sat_Nep, 'Sat_Plu': lizte_Sat_Plu, 'Ura_Nep': lizte_Ura_Nep, 'Ura_Plu': lizte_Ura_Plu, 'Nep_Plu': lizte_Nep_Plu}
#dfObj = pd.DataFrame(dict)
#concat_asp_g = pd.concat([flu1, dfObj], axis=1)

#geo_con = concat_asp_g[concat_asp_g.Date == today]
#geo_con.round()

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