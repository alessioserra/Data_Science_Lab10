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
    plt.scatter(x=XlongAmenity, y=ylatAmenity, c='b', s=3)
    plt.scatter(x=XlongShop, y=ylatShop, c='y', s=3)
    plt.scatter(x=XlongPublicT, y=ylatPublicT, c='r', s=3)
    plt.scatter(x=XlongHighway, y=ylatHighway, c='g', s=3)
    plt.show()

#plot_POIS ('amenity' or 'shop' or 'public_transport' or 'highway')
#plot_POIS('amenity')
#plot_POIS_ALL()        

"""Exercise 5"""
def split_into_Celles(n):
    
    result = []
    
    minLat = min(float(row[2]) for row in dataset)
    maxLat = max(float(row[2]) for row in dataset)
    minLong = min(float(row[3]) for row in dataset)
    maxLong = max(float(row[3]) for row in dataset)
    
    #size of every interval
    LongInterval = (maxLong-minLong)/n 
    LatInterval = (maxLat-minLat)/n
    
    #Take all coordinates of dataset
    X = [float(row[3]) for row in dataset]
    y = [float(row[2]) for row in dataset]
    
    result = []
    
    for x,y in zip(X,y):
        temp = []
        for i in range(1,n+1):
            if minLong + (i-1)*(LongInterval) < x < minLong + (i*LongInterval) and minLat + (i-1)*(LatInterval) < y < minLat + (i*LatInterval):
                temp.append(x)
                temp.append(y)
                temp.append(i)
                result.append(temp)
    
    print("Split done")
    
    x1 = []
    y1 = []
    
    for row in result:
        if row[2]==1:
            x1.append(row[0])
            y1.append(row[1])
    
    x2 = []
    y2 = []
    
    for row in result:
        if row[2]==2:
            x2.append(row[0])
            y2.append(row[1])
            
    x3 = []
    y3 = []
    
    for row in result:
        if row[2]==3:
            x3.append(row[0])
            y3.append(row[1])
    
    x4 = []
    y4 = []
    
    for row in result:
        if row[2]==4:
            x4.append(row[0])
            y4.append(row[1])
    
    img = plt.imread('New_York_City_Map.PNG')
    fig, ax = plt.subplots(figsize=(10,8))   #interval of the axis
    plt.imshow(img, extent=[ minLong-0.01, maxLong+0.01, minLat-0.01, maxLat+0.01 ])
    plt.scatter(x=x1, y=y1, c='b', s=3)
    plt.scatter(x=x2, y=y2, c='r', s=3)
    plt.scatter(x=x3, y=y3, c='g', s=3)
    plt.scatter(x=x4, y=y4, c='y', s=3)
    plt.show()
    
    return "OK"

print(split_into_Celles(4))
    