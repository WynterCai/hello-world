# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 11:12:43 2019

@author: ThinkPad
"""
from sp_functions import get_stock_data
import pandas as pd

df_x = get_stock_data('C:/Users/ThinkPad/Desktop/Autumn/FIN6102/Computing/Lesson2/FF_Three_Factor_Monthly.csv)
df_y = get_stock_data

start
start = pd.to.datetime()
df_x =df_x.loc[start:end]
df_y =df_y.loc[start:end]
assert (df_x.index == df_index).all()

factors  = df_x.iloc[:,:3].values
pf = df_x.iloc[]
port_return =df_y.iloc[:,0].values
