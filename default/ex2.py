'''
Created on 17 dic 2019

@author: zierp
'''
import pandas as pd
from cmath import nan

#Ex1
df = pd.read_csv('831394006_T_ONTIME.csv', parse_dates=['FL_DATE'])

#Ex2 
print(df.info())

#Ex3 [ remove cancelled flights]
df = df[df.CANCELLED != 1]

#Ex4
dictCarrier = {}
dictDelay = {}
"""Drop all useless columns and rows containing NaN"""
df.fillna(0.0, inplace=True)

for carrier, delay in zip(df.UNIQUE_CARRIER, df.ARR_DELAY):
    if carrier not in dictCarrier.keys():
        dictCarrier[carrier] = 1
        dictDelay[carrier] = delay
    else:
        dictCarrier[carrier] = dictCarrier[carrier] + 1
        dictDelay[carrier] = dictDelay[carrier] + delay

"""Print all result"""
print("\nFlights for Carrier")
for key in dictCarrier.keys():
    print(key, "# of flights: ",dictCarrier[key]," - Mean delay: ",(dictDelay[key]/dictCarrier[key])," minutes.")
    
#Ex5