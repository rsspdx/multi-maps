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

# open gdp_per_capita, get other varnames
gdpcap = pd.read_csv('gdp_per_capita.csv', index_col=0)

varnames = pd.read_csv('varnames.csv')
varnames = varnames.iloc[:, 1].tolist()
varnames.remove('gdp_per_capita')

vars = []
for var in varnames:
    vars.append({'name': var})
for i in range(len(vars)):
    vars[i]['file'] = vars[i]['name'] + '.csv'
    

varnames_resid = pd.read_csv('varnames_resid.csv')
varnames_resid = varnames_resid.iloc[:, 1].tolist()
for i in range(len(varnames_resid)):
    varnames_resid[i] = {'name': varnames_resid[i] + '_resid'}
    varnames_resid[i]['file'] = varnames_resid[i]['name'] + '.csv'
    

vars += varnames_resid

# open files
files = []
for i in range(len(vars)):
    files.append(pd.read_csv(vars[i]['name'] + '.csv', index_col=False))

for i in range(len(files)):
    gdpcap = gdpcap.merge(files[i], on = ['country', 'country_code'])
    
gdpcap.to_csv('wdi_vars.csv')