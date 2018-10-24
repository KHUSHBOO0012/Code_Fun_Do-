import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv("rainfall in india 1901-2015.csv").rename(columns=str.lower)

print(df.head())

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

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(16,8))
ax = fig.add_subplot(111)
df.groupby('subdivision').mean().sort_values(by='annual', ascending=False)['annual'].plot('bar', color='b',width=0.3,title='Subdivision wise Average Annual Rainfall', fontsize=20)
plt.xticks(rotation = 90)
plt.ylabel('Average Annual Rainfall (mm)')
ax.title.set_fontsize(30)
ax.xaxis.label.set_fontsize(20)
ax.yaxis.label.set_fontsize(20)
plt.show()

total_rainfall = df.groupby(['subdivision']).mean()
total_rainfall['subdivision'] = total_rainfall.index
total_rainfall_states=total_rainfall[['annual']]
print(total_rainfall_states.sort_values(by='annual',ascending=False))
