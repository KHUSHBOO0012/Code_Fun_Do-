import warnings
warnings.simplefilter('ignore')
import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv("rainfall in india 1901-2015.csv").rename(columns=str.lower)

#print(df.head())

sub_div=df['subdivision'].unique()
num=len(sub_div)
#print(num)
#print(sub_div)

no_cols=df.columns
#cols=[15,16,17,18]#remove col of month range
#df= df.drop(df.columns[cols],axis=1)
#print(df.head())

#for imputing missing value with average of that subdivision value
new_df=pd.DataFrame()
for sub in sub_div:
    new_df1=df.loc[df['subdivision']==sub]
    new_df1=new_df1.fillna(new_df1.mean())
    new_df=new_df.append(new_df1)

df=new_df
#df.info()

total_rainfall = df.groupby(['subdivision']).mean()
total_rainfall['subdivision'] = total_rainfall.index
total_rainfall_states=total_rainfall[['annual']]
print(total_rainfall_states.sort_values(by='annual',ascending=False))

import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [16,9]
fig, ax = plt.subplots()
x = ['ARUNACHAL PRADESH','COASTAL KARNATAKA','KONKAN & GOA','ANDAMAN & NICOBAR ISLANDS','KERALA','SUB HIMALAYAN WEST BENGAL & SIKKIM','ASSAM & MEGHALAYA','NAGA MANI MIZO TRIPURA','LAKSHADWEEP','GANGETIC WEST BENGAL','UTTARAKHAND','ORISSA','CHHATTISGARH','JHARKHAND','HIMACHAL PRADESH','EAST MADHYA PRADESH','BIHAR','JAMMU & KASHMIR','VIDARBHA','COASTAL ANDHRA PRADESH','SOUTH INTERIOR KARNATAKA','EAST UTTAR PRADESH','TELANGANA','WEST MADHYA PRADESH','TAMIL NADU','GUJARAT REGION','MADHYA MAHARASHTRA',
'WEST UTTAR PRADESH','MATATHWADA','RAYALSEEMA','NORTH INTERIOR KARNATAKA','EAST RAJASTHAN','PUNJAB','HARYANA DELHI & CHANDIGARH','SAURASHTRA & KUTCH','WEST RAJASTHAN']

y=[3418.857143,3408.409649,2977.686087,2927.439423,2925.487826,2752.217391,2580.695652,2433.619130,1590.886408,1490.487826,1465.696522,1458.169565,1371.728696,1309.303478,1260.345217,1205.000000,1197.633913,1139.684211,1095.459130,1052.904348,1040.391304,979.213043,953.378261,944.358772,943.713043,918.230435,880.233043,827.114783,790.692174,766.206087,717.795652,655.215652,593.535652,530.496522,495.161739,292.673043]

for i in range(1):
    bars = ax.bar(x, y, color='b',width=0.3,label='$ red = danger $' ) 
for i in range(0,len(x)):
    if (y[i]> 2000):
        bars[i].set_color('r')
plt.title("Subdivision wise Average Annual Rainfall")
plt.xticks(rotation = 90)
plt.ylabel('Average Annual Rainfall (mm)')
ax.title.set_fontsize(20)
ax.xaxis.label.set_fontsize(20)
ax.yaxis.label.set_fontsize(20)
ax.legend()
plt.show()
