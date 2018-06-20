#Humberto Campos
import pandas as pd
import matplotlib.pyplot as plt

dc = pd.read_csv('dictionary.csv', sep=",",index_col='Country')
ds = pd.read_csv('summer.csv', sep=",",index_col='Country')
dw = pd.read_csv('winter.csv', sep=",",index_col='Country')


#pregunta 1
dc_GDP_per_Capita = dc['GDP per Capita']
#dc_GDP_per_Capita.sort_values(by=['GDP per Capita'])
dc_GDP_per_Capita.plot()
plt.show()



#pregunta 2
ds_Medal = ds['Medal']
Medal_counts = ds_Medal.groupby('Country').size()
Medal_counts.plot(kind='bar')
plt.show()


#pregunta 3
ds_Medal = ds[['Medal']].copy()
ds_rank = ds_Medal.groupby(['Country','Medal']).size()
ds_rank.plot(kind='bar')
plt.show()

#pregunta 4
ds_Medal = ds[['Medal']].copy()
dw_Medal = dw[['Medal']].copy()
fr=[ds_Medal,dw_Medal]
d_rank = pd.concat(fr)
d_rank = d_rank.groupby(['Country','Medal']).size()
d_rank.plot(kind='bar')
plt.show()