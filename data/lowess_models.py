#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 20:17:17 2019

@author: rs
"""

import pandas as pd
import os
import statsmodels.api as sm
import matplotlib.pyplot as plt

wd = os.path.expanduser('~/data/geo/multi-maps/data')
os.chdir(wd)

gdpcap = pd.read_csv('gdp_per_capita.csv', index_col=0)
lowess = sm.nonparametric.lowess

varnames = pd.read_csv('varnames.csv')
varnames = varnames.iloc[:, 1].tolist()
varnames.remove('gdp_per_capita')
vars = []
for var in varnames:
    vars.append({'name': var})
for i in range(len(vars)-1):
    vars[i]['file'] = vars[i]['name'] + '.csv'

for i in range(len(vars)-1):
    df = pd.read_csv(vars[i]['file'], index_col=0)
    df = df.merge(gdpcap, on=['country', 'country_code'])
    df = df.dropna()
    model = lowess(df[vars[i]['name']], df.gdp_per_capita, return_sorted=False)
    df[vars[i]['name'] + '_resid'] = df[vars[i]['name']] - model
    df = df.drop(columns = [vars[i]['name'], 'gdp_per_capita'])
    df.to_csv(vars[i]['name'] + '_resid.csv')
    
