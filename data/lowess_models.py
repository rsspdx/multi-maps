#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 20:17:17 2019

@author: rs
"""

import pandas as pd
import os
import statsmodels.api as sm

wd = os.path.expanduser('~/multi-maps/data')
os.chdir(wd)

gdpcap = pd.read_csv('gdp_per_capita.csv', index_col=False)
lowess = sm.nonparametric.lowess

varnames = pd.read_csv('varnames.csv')
varnames = varnames.iloc[:, 1].tolist()
varnames.remove('gdp_per_capita')
varnames.remove('population')

vars = []
for var in varnames:
    vars.append({'name': var})
for i in range(len(vars)):
    vars[i]['file'] = vars[i]['name'] + '.csv'

lowess = sm.nonparametric.lowess

for i in range(len(vars)):
    df = pd.read_csv(vars[i]['file'], index_col=False)
    df = df.merge(gdpcap, on=['country', 'country_code'])
    df = df.dropna()
    model = lowess(df[vars[i]['name']], df.gdp_per_capita, return_sorted=False)
    df[vars[i]['name'] + '_resid'] = df[vars[i]['name']] - model
    df = df.drop(columns = [vars[i]['name'], 'gdp_per_capita'])
    df = df.merge(gdpcap, on=['country', 'country_code'], how='outer')
    df = df.drop('gdp_per_capita', 1)
    df.to_csv(vars[i]['name'] + '_resid.csv')
    
varnames_resid = pd.DataFrame(varnames)
varnames_resid.to_csv('varnames_resid.csv')
