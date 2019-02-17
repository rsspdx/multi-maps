#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 06:10:29 2019

@author: rs
"""

import pandas as pd
import os

wd = os.path.expanduser('~/multi-maps/data')
os.chdir(wd)

gdpcap = pd.read_csv('gdp_per_capita.csv', index_col=0)

varnames = pd.read_csv('varnames.csv')
varnames = varnames.iloc[:, 1].tolist()
varnames.remove('gdp_per_capita')
vars = []
for var in varnames:
    vars.append({'name': var})
for i in range(len(vars)-1):
    vars[i]['file'] = vars[i]['name'] + '.csv'
    

varnames_resid = pd.read_csv('varnames_resid.csv')
varnames_resid = varnames_resid.iloc[:, 1].tolist()
varnames_resid.remove('gdp_per_capita')

vars_resid = []
for var in varnames_resid:
    vars_resid.append({'name': var})
for i in range(len(vars_resid)-1):
    vars_resid[i]['file'] = vars[i]['name'] + '.csv'
    
vars += vars_resid

for i in range(len(vars) - 1):
    gdpcap = gdpcap.merge(vars[i]['name'], on = ['country', 'country_code'])

gdpcap.to_csv('wdi_vars.csv')