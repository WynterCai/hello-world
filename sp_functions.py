# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 10:12:22 2019

@author: ThinkPad
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

def get_stock_data(path,columns=None):
    df = pd.read_csv(path)
    df = df.iloc[start:end]
    df = df.set_index('Date')
    df.index = pd.to_datetime(df.index)
    if columns is None:
        return df
    else:
        return df[columns]

if __name__=="__main__":
sp = get_stock_data("data/S&P500.csv",columns=["Adj Close"])
nky = get_stock_data("data/NEY225.csv",columns=["Adj Close"])
ax = plt.gca()
ax.plot(sp,color="orange")
ax.legend(["SP"])
