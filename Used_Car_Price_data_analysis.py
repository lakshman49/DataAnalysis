# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 22:41:43 2018

@author: Lakshman
"""

import pandas as pd

url="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"
df = pd.read_csv(url,header=None)
Headers=["symboling","normalized-losses","make","fuel-type","aspiration","num-of-doors","body-style","drive-wheels","engine-location", "wheel-base","length","width","height","curb-weight","engine-type","num-of-cylinders","engine-size","fuel-system","bore","stroke","compression-ratio","horsepower","peak-rpm","city-mpg","highway-mpg","price",]
df.columns=Headers
df.to_csv('C:/Users/Lakshman/Desktop/ML/TestPrograms/automobile.csv')
df.head(5)
df.tail(5)
df.dtypes
df.describe(include='all')
df.info
df.summary()

