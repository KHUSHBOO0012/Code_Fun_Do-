
# coding: utf-8



import warnings
warnings.simplefilter('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import datetime
from sklearn.svm import SVR
from sklearn import linear_model
import sys 

pd.options.mode.chained_assignment = None 

df = pd.read_csv("rainfall in india 1901-2015.csv")
states = df["SUBDIVISION"].unique()
print(states)
statename = sys.argv[1]





def state(statename):
    dfg = df.loc[df['SUBDIVISION'] ==statename]
    year_start = df["YEAR"][0]
    dfg.drop(["SUBDIVISION","ANNUAL","Jan-Feb", "Mar-May" ,"Jun-Sep" ,"Oct-Dec"],axis =1,inplace = True)
    dfg.fillna(dfg.mean())
    return dfg 
dfg = state(statename)




x  = dfg.shape[0]
k = dfg.index.values[0]
for i in range(k+1, x+k):
    if dfg["YEAR"][i-1] + 1 == dfg["YEAR"][i]:
        i+=1
        continue
    else : 
        dfg =  dfg.append(dfg.mean().astype(int),ignore_index=True)
        dfg["YEAR"][dfg.shape[0]-1]= dfg["YEAR"][i-1] + 1
        j=2
        while(dfg["YEAR"][dfg.shape[0]-1] != dfg["YEAR"][i] -1):
            dfg =  dfg.append(dfg.mean().astype(int),ignore_index=True)
            dfg["YEAR"][dfg.shape[0]-1]= dfg["YEAR"][i-1] + j
            j+=1
        i+=1
        
      





dfg.sort_values("YEAR",inplace =True)
    
# print(dfg.head(10))            
# print(dfg.tail(10))




for i in range(k,dfg["YEAR"].shape[0]+k):
    date_string =  str(dfg["YEAR"][i])+'-01'
    date = np.array( date_string,dtype = np.datetime64)
    date  + np.arange(12)
    if(i == k):
        final = np.array(date + np.arange(12))
    else:
        final =  np.concatenate((final,date  + np.arange(12)),axis = 0)
# dfg.tail()





dfg.drop(columns =["YEAR"],inplace =True)
dfg = dfg.values
dfg = dfg.reshape(dfg.shape[0]*dfg.shape[1],1)
dfg = pd.DataFrame(dfg)
dfg.head()
dfg["dates"] = final
dfg.columns = ["rainfall","dates"]
# print(dfg.head())
dfg.sort_values("dates",inplace =True)
dfg.set_index("dates", inplace = True)
def data_set(dataframe):
    ''' 

    splitting into test ,training and cross validation datasets
    in ratio of 8:1:1
    '''
    length = len(dataframe.iloc[:,0])
    train_end = round(length * 0.80)
    test_end = round(length * 0.90)
    return [
            dataframe.iloc[:train_end : ],
            dataframe.iloc[train_end:, :]

           ]
dfg1 ,dfg2  = data_set(dfg)





def features(df):
    

     
    df['MAV3'] = (df.iloc[:,0]).rolling(window =3).mean() # moving day average for 3-month periods
    df['MAV5'] = (df.iloc[:,0]).rolling(window =5).mean() # moving day average for 5-month periods
    df['t-6']  = df["rainfall"].shift(-6)
    df['t-5']  = df["rainfall"].shift(-5)
    df['t-4']  = df["rainfall"].shift(-4)
    df['t-3']  = df["rainfall"].shift(-3)
    df['t-2']  = df["rainfall"].shift(-2)
    df['t-1']  = df["rainfall"].shift(-1)
    
    
    
    df =df.fillna(df.mean()) 
    
    
    X = df.loc[:,"t-6":'t-1']
    y =  pd.DataFrame(df,columns = ["rainfall"] )   
    return [X,y]

X,y = features(dfg)
# y.head()



x_train,y_train = features(dfg1)
x_test,y_test = features(dfg2)
model =linear_model.LinearRegression(normalize=True)
model.fit(x_train,y_train)
predictions =model.predict(x_test.values)
y_test['rainfall'].plot()
plt.legend(loc=4) 
y_test['predictions'] = predictions
y_test["predictions"].plot(color ='r')
 
plt.xlabel('Rainfall')
plt.ylabel('Year')
plt.show()

