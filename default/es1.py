'''
Created on 12 dic 2019

@author: zierp
'''
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing.label import LabelEncoder

# Load CSV file
poisID = []
with open('ny_municipality_pois_id.csv') as file:
    for row in csv.reader(file):
        poisID.append(row[0])

# Load TSV file
dataset = []
with open("pois_all_info", encoding='utf-8') as file: 
    for row in csv.reader(file, delimiter="\t", quotechar='"'):
        if row[0] in poisID: # I take only New York point of interest
            temp = []
            for el in row:
                temp.append(el)
        
            dataset.append(temp)
# delete fieldnames        
dataset.pop(0)

"""Exercise 3
There are four possible categories of POIs:
amenity, shop, public_transport and highway"""

amenity = []
shop = []
public_transport = []
highway = []

"""
for row in dataset:
    if row[4] != '':
        amenity.append(row[4])
    if row[5] != '':
        shop.append(row[5])
    if row[6] != '':
        public_transport.append(row[6])
    if row[7] != '':
        highway.append(row[7])


#Encoding
le = LabelEncoder()
a = le.fit_transform(amenity)
s = le.fit_transform(shop)
pt = le.fit_transform(public_transport)
h = le.fit_transform(highway)

# Plot histograms
plt.hist(a)
plt.title('Amenity')
plt.show()

plt.hist(s)
plt.title('Shop')
plt.show()

plt.hist(pt)
plt.title('Public transport')
plt.show()

plt.hist(h)
plt.title('Highway')
plt.show()
"""

"""Exercise 4"""
def plot_POIS(category):
    Xlong = [] #3
    ylat = [] #2
    if category=='amenity':
        for row in dataset:
            if row[4] != '':
                Xlong.append(float(row[3]))
                ylat.append(float(row[2]))
    if category=='shop':
        for row in dataset:
            if row[4] != '':
                Xlong.append(float(row[3]))
                ylat.append(float(row[2]))
    if category=='public_transport':
        for row in dataset:
            if row[4] != '':
                Xlong.append(float(row[3]))
                ylat.append(float(row[2]))
    if category=='highway':
        for row in dataset:
            if row[4] != '':
                Xlong.append(float(row[3]))
                ylat.append(float(row[2]))
                                
    img = plt.imread('New_York_City_Map.PNG')
    fig, ax = plt.subplots(figsize=(10,8))   #interval of the axis
    plt.imshow(img, extent=[ min(Xlong)-0.01, max(Xlong)+0.01, min(ylat)-0.01, max(ylat)+0.01 ])
    plt.scatter(x=Xlong, y=ylat)
    plt.show()
    
def plot_POIS_ALL():
    XlongAmenity = [] 
    ylatAmenity = [] 
    XlongShop = [] 
    ylatShop = [] 
    XlongPublicT = [] 
    ylatPublicT = [] 
    XlongHighway = [] 
    ylatHighway = [] 
    
    minLat = min(float(row[2]) for row in dataset)
    maxLat = max(float(row[2]) for row in dataset)
    minLong = min(float(row[3]) for row in dataset)
    maxLong = max(float(row[3]) for row in dataset)
    
    for row in dataset:
        if row[4] != '':
            XlongAmenity.append(float(row[3]))
            ylatAmenity.append(float(row[2]))

        if row[5] != '':
            XlongShop.append(float(row[3]))
            ylatShop.append(float(row[2]))
                
        if row[6] != '':
            XlongPublicT.append(float(row[3]))
            ylatPublicT.append(float(row[2]))

        if row[7] != '':
            XlongHighway.append(float(row[3]))
            ylatHighway.append(float(row[2]))
                                
    img = plt.imread('New_York_City_Map.PNG')
    fig, ax = plt.subplots(figsize=(10,8))   #interval of the axis
    plt.imshow(img, extent=[ minLong-0.01, maxLong+0.01, minLat-0.01, maxLat+0.01 ])
    plt.scatter(x=XlongAmenity, y=ylatAmenity, c='b', s=5)
    plt.scatter(x=XlongShop, y=ylatShop, c='y', s=5)
    plt.scatter(x=XlongPublicT, y=ylatPublicT, c='r', s=5)
    plt.scatter(x=XlongHighway, y=ylatHighway, c='g', s=5)
    plt.show()

#plot_POIS ('amenity' or 'shop' or 'public_transport' or 'highway')
#plot_POIS('amenity')
plot_POIS_ALL()        

"""Exercise 5"""