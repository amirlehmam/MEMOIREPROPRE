from datetime import datetime
import pandas as pd
import numpy as np

import sklearn

import seaborn as sns
import matplotlib.pyplot as plt

from datetime import date
from datetime import datetime

import plotly.express as px

import os

# Retrieve the path to the current folders
current_path = os.getcwd()

# Get the path to the csv file folder - in this case the 'data' file
csv_path = os.path.join(current_path, 'data\\test')

# A EXPLIQUER ICI
for file in os.listdir(csv_path):
    fd = pd.read_csv(os.path.join(csv_path, file))
    globals()[file.rpartition(".")[0]] = fd

p_t = nega.copy()

p_t['Date'] = d = pd.to_datetime(p_t['Date'])
p_t['Date'] = p_t['Date'].dt.strftime('%Y/%m/%d')

twoday = datetime.strftime(datetime.now(), "%Y/%m/%d")
t = pd.to_datetime(twoday)

p_t['Elapsed'] = t - d
p_t['Elapsed'] = p_t['Elapsed'].dt.days.to_numpy()

p_t['Sqrt'] = p_t['Elapsed'] ** (1/2)
p_t['Sqrt'] = p_t['Sqrt'].round(2)
sq = p_t['Sqrt']

op13 = (((sq / 13).to_numpy().reshape(-1, 1) + (np.arange(1, 22)).reshape(1, -1)) ** 2)
pt13 = op13.astype('timedelta64[D]') + d.to_numpy().reshape(-1, 1)

pt13 = pd.DataFrame(pt13, columns=['1', '2', '3', '4', '5','6','7','8','9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'])
pt13['1'] = pt13['1'].dt.strftime('%Y/%m/%d')
pt13['2'] = pt13['2'].dt.strftime('%Y/%m/%d')
pt13['3'] = pt13['3'].dt.strftime('%Y/%m/%d')
pt13['4'] = pt13['4'].dt.strftime('%Y/%m/%d')
pt13['5'] = pt13['5'].dt.strftime('%Y/%m/%d')
pt13['6'] = pt13['6'].dt.strftime('%Y/%m/%d')
pt13['7'] = pt13['7'].dt.strftime('%Y/%m/%d')
pt13['8'] = pt13['8'].dt.strftime('%Y/%m/%d')
pt13['9'] = pt13['9'].dt.strftime('%Y/%m/%d')
pt13['10'] = pt13['10'].dt.strftime('%Y/%m/%d')
pt13['11'] = pt13['11'].dt.strftime('%Y/%m/%d')
pt13['12'] = pt13['12'].dt.strftime('%Y/%m/%d')
pt13['13'] = pt13['13'].dt.strftime('%Y/%m/%d')
pt13['14'] = pt13['14'].dt.strftime('%Y/%m/%d')
pt13['15'] = pt13['15'].dt.strftime('%Y/%m/%d')
pt13['16'] = pt13['16'].dt.strftime('%Y/%m/%d')
pt13['17'] = pt13['17'].dt.strftime('%Y/%m/%d')
pt13['18'] = pt13['18'].dt.strftime('%Y/%m/%d')
pt13['19'] = pt13['19'].dt.strftime('%Y/%m/%d')
pt13['20'] = pt13['20'].dt.strftime('%Y/%m/%d')
pt13['21'] = pt13['21'].dt.strftime('%Y/%m/%d')

op21 = (((sq / 21).to_numpy().reshape(-1, 1) + (np.arange(1, 22)).reshape(1, -1)) ** 2)
pt21 = op21.astype('timedelta64[D]') + d.to_numpy().reshape(-1, 1)

pt21 = pd.DataFrame(pt21, columns=['1', '2', '3', '4', '5','6','7','8','9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'])
pt21['1'] = pt21['1'].dt.strftime('%Y/%m/%d')
pt21['2'] = pt21['2'].dt.strftime('%Y/%m/%d')
pt21['3'] = pt21['3'].dt.strftime('%Y/%m/%d')
pt21['4'] = pt21['4'].dt.strftime('%Y/%m/%d')
pt21['5'] = pt21['5'].dt.strftime('%Y/%m/%d')
pt21['6'] = pt21['6'].dt.strftime('%Y/%m/%d')
pt21['7'] = pt21['7'].dt.strftime('%Y/%m/%d')
pt21['8'] = pt21['8'].dt.strftime('%Y/%m/%d')
pt21['9'] = pt21['9'].dt.strftime('%Y/%m/%d')
pt21['10'] = pt21['10'].dt.strftime('%Y/%m/%d')
pt21['11'] = pt21['11'].dt.strftime('%Y/%m/%d')
pt21['12'] = pt21['12'].dt.strftime('%Y/%m/%d')
pt21['13'] = pt21['13'].dt.strftime('%Y/%m/%d')
pt21['14'] = pt21['14'].dt.strftime('%Y/%m/%d')
pt21['15'] = pt21['15'].dt.strftime('%Y/%m/%d')
pt21['16'] = pt21['16'].dt.strftime('%Y/%m/%d')
pt21['17'] = pt21['17'].dt.strftime('%Y/%m/%d')
pt21['18'] = pt21['18'].dt.strftime('%Y/%m/%d')
pt21['19'] = pt21['19'].dt.strftime('%Y/%m/%d')
pt21['20'] = pt21['20'].dt.strftime('%Y/%m/%d')
pt21['21'] = pt21['21'].dt.strftime('%Y/%m/%d')

op34 = (((sq / 34).to_numpy().reshape(-1, 1) + (np.arange(1, 22)).reshape(1, -1)) ** 2)
pt34 = op34.astype('timedelta64[D]') + d.to_numpy().reshape(-1, 1)

pt34 = pd.DataFrame(pt34, columns=['1', '2', '3', '4', '5','6','7','8','9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'])
pt34['1'] = pt34['1'].dt.strftime('%Y/%m/%d')
pt34['2'] = pt34['2'].dt.strftime('%Y/%m/%d')
pt34['3'] = pt34['3'].dt.strftime('%Y/%m/%d')
pt34['4'] = pt34['4'].dt.strftime('%Y/%m/%d')
pt34['5'] = pt34['5'].dt.strftime('%Y/%m/%d')
pt34['6'] = pt34['6'].dt.strftime('%Y/%m/%d')
pt34['7'] = pt34['7'].dt.strftime('%Y/%m/%d')
pt34['8'] = pt34['8'].dt.strftime('%Y/%m/%d')
pt34['9'] = pt34['9'].dt.strftime('%Y/%m/%d')
pt34['10'] = pt34['10'].dt.strftime('%Y/%m/%d')
pt34['11'] = pt34['11'].dt.strftime('%Y/%m/%d')
pt34['12'] = pt34['12'].dt.strftime('%Y/%m/%d')
pt34['13'] = pt34['13'].dt.strftime('%Y/%m/%d')
pt34['14'] = pt34['14'].dt.strftime('%Y/%m/%d')
pt34['15'] = pt34['15'].dt.strftime('%Y/%m/%d')
pt34['16'] = pt34['16'].dt.strftime('%Y/%m/%d')
pt34['17'] = pt34['17'].dt.strftime('%Y/%m/%d')
pt34['18'] = pt34['18'].dt.strftime('%Y/%m/%d')
pt34['19'] = pt34['19'].dt.strftime('%Y/%m/%d')
pt34['20'] = pt34['20'].dt.strftime('%Y/%m/%d')
pt34['21'] = pt34['21'].dt.strftime('%Y/%m/%d')

op55 = (((sq / 55).to_numpy().reshape(-1, 1) + (np.arange(1, 22)).reshape(1, -1)) ** 2)
pt55 = op55.astype('timedelta64[D]') + d.to_numpy().reshape(-1, 1)

pt55 = pd.DataFrame(pt55, columns=['1', '2', '3', '4', '5','6','7','8','9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'])
pt55['1'] = pt55['1'].dt.strftime('%Y/%m/%d')
pt55['2'] = pt55['2'].dt.strftime('%Y/%m/%d')
pt55['3'] = pt55['3'].dt.strftime('%Y/%m/%d')
pt55['4'] = pt55['4'].dt.strftime('%Y/%m/%d')
pt55['5'] = pt55['5'].dt.strftime('%Y/%m/%d')
pt55['6'] = pt55['6'].dt.strftime('%Y/%m/%d')
pt55['7'] = pt55['7'].dt.strftime('%Y/%m/%d')
pt55['8'] = pt55['8'].dt.strftime('%Y/%m/%d')
pt55['9'] = pt55['9'].dt.strftime('%Y/%m/%d')
pt55['10'] = pt55['10'].dt.strftime('%Y/%m/%d')
pt55['11'] = pt55['11'].dt.strftime('%Y/%m/%d')
pt55['12'] = pt55['12'].dt.strftime('%Y/%m/%d')
pt55['13'] = pt55['13'].dt.strftime('%Y/%m/%d')
pt55['14'] = pt55['14'].dt.strftime('%Y/%m/%d')
pt55['15'] = pt55['15'].dt.strftime('%Y/%m/%d')
pt55['16'] = pt55['16'].dt.strftime('%Y/%m/%d')
pt55['17'] = pt55['17'].dt.strftime('%Y/%m/%d')
pt55['18'] = pt55['18'].dt.strftime('%Y/%m/%d')
pt55['19'] = pt55['19'].dt.strftime('%Y/%m/%d')
pt55['20'] = pt55['20'].dt.strftime('%Y/%m/%d')
pt55['21'] = pt55['21'].dt.strftime('%Y/%m/%d')

op89 = (((sq / 89).to_numpy().reshape(-1, 1) + (np.arange(1, 22)).reshape(1, -1)) ** 2)
pt89 = op89.astype('timedelta64[D]') + d.to_numpy().reshape(-1, 1)

pt89 = pd.DataFrame(pt89, columns=['1', '2', '3', '4', '5','6','7','8','9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21'])
pt89['1'] = pt89['1'].dt.strftime('%Y/%m/%d')
pt89['2'] = pt89['2'].dt.strftime('%Y/%m/%d')
pt89['3'] = pt89['3'].dt.strftime('%Y/%m/%d')
pt89['4'] = pt89['4'].dt.strftime('%Y/%m/%d')
pt89['5'] = pt89['5'].dt.strftime('%Y/%m/%d')
pt89['6'] = pt89['6'].dt.strftime('%Y/%m/%d')
pt89['7'] = pt89['7'].dt.strftime('%Y/%m/%d')
pt89['8'] = pt89['8'].dt.strftime('%Y/%m/%d')
pt89['9'] = pt89['9'].dt.strftime('%Y/%m/%d')
pt89['10'] = pt89['10'].dt.strftime('%Y/%m/%d')
pt89['11'] = pt89['11'].dt.strftime('%Y/%m/%d')
pt89['12'] = pt89['12'].dt.strftime('%Y/%m/%d')
pt89['13'] = pt89['13'].dt.strftime('%Y/%m/%d')
pt89['14'] = pt89['14'].dt.strftime('%Y/%m/%d')
pt89['15'] = pt89['15'].dt.strftime('%Y/%m/%d')
pt89['16'] = pt89['16'].dt.strftime('%Y/%m/%d')
pt89['17'] = pt89['17'].dt.strftime('%Y/%m/%d')
pt89['18'] = pt89['18'].dt.strftime('%Y/%m/%d')
pt89['19'] = pt89['19'].dt.strftime('%Y/%m/%d')
pt89['20'] = pt89['20'].dt.strftime('%Y/%m/%d')
pt89['21'] = pt89['21'].dt.strftime('%Y/%m/%d')

pt_hits = pd.concat([pt13, pt21, pt34, pt55, pt89])

adpod = pt_hits.copy()

good = adpod[1:].unstack().value_counts(ascending=True)

good = pd.DataFrame(good, columns=['Hit'])

good = good.reset_index()
good = good.rename_axis('E', axis=1)
good.columns = good.columns.str.replace('index', 'Date')
good = good.rename_axis(None, axis=1)

start_date = "10/08/2022"
end_date = "31/12/2022"

mask = (good['Date'] > start_date) & (good['Date'] <= end_date)
good = good.loc[mask]

# addp_hits.head(50)

good = good.sort_values(by=['Date'], ascending=True)

good['Date'] = good['Date'].apply(pd.to_datetime)

start_date = "2022/08/20"
end_date = "2022/12/31"

mask = (good['Date'] > start_date) & (good['Date'] <= end_date)
good = good.loc[mask]

# addp_hits.head(50)

pt_hit = good.sort_values(by=['Date'], ascending=True)
print(pt_hit)

fig = px.bar(pt_hit, x='Date', y='Hit')
fig.show()