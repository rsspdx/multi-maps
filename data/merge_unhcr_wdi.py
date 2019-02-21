#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:07:07 2019

@author: rs
"""

import pandas as pd
import os
import statsmodels.api as sm

wd = os.path.expanduser('~/multi-maps/data')
os.chdir(wd)


gdpcap = pd.read_csv('gdp_per_capita.csv')
asylum_idps_refugees = pd.read_csv('asylum_idps_refugees.csv')
recognized_total_decisions = pd.read_csv('recognized_total_decisions.csv')
wdi_vars = pd.read_csv('wdi_vars.csv')
country_iso_2_iso_3 = pd.read_csv('country_iso_2_iso_3.csv')
happiness = pd.read_csv('happiness.2015.csv')
happiness.to_csv('happiness.csv')
ti_cpi = pd.read_csv('ti_cpi_2015.csv')
asylum_seekers = pd.read_csv('asylum_seekers.csv')
idps = pd.read_csv('idps.csv')
refugees = pd.read_csv('refugees.csv')
recognition_rate = pd.read_csv('recognition_rate.csv')

unhcr_vars = asylum_idps_refugees.merge(recognized_total_decisions, on='country')
unhcr_vars = unhcr_vars.merge(country_iso_2_iso_3, on='country')
unhcr_vars['country_code'] = unhcr_vars['iso_3']

refugees = refugees.merge(country_iso_2_iso_3, on='country')
refugees['country_code'] = refugees['iso_3']
refugees.to_csv('refugees.csv')

asylum_seekers = asylum_seekers.merge(country_iso_2_iso_3, on='country')
asylum_seekers['country_code'] = asylum_seekers['iso_3']
asylum_seekers.to_csv('asylum_seekers.csv')

idps = idps.merge(country_iso_2_iso_3, on='country')
idps['country_code'] = idps['iso_3']
idps.to_csv('idps.csv')

recognition_rate = recognition_rate.merge(country_iso_2_iso_3, on='country')
recognition_rate['country_code'] = recognition_rate['iso_3']
recognition_rate.to_csv('recognition_rate.csv')

wdi_vars = wdi_vars.merge(unhcr_vars, on='country_code')

wdi_vars['refugees_per_pop'] = wdi_vars['refugees'] / wdi_vars['population']
wdi_vars['asylum_seekers_per_pop'] = wdi_vars['asylum_seekers'] / wdi_vars['population']

wdi_vars = wdi_vars.merge(happiness, on='country_code')
wdi_vars = wdi_vars.merge(ti_cpi, on='country_code')

wdi_vars.to_csv('map_data.csv')

filenames = pd.DataFrame(wdi_vars.columns.tolist())
filenames.to_csv('map_data_varnames.csv')

newvars = ['asylum_seekers', 'idps', 'refugees', 'recognition_rate', 'happiness']
lowess = sm.nonparametric.lowess

for var in newvars:
    df = pd.read_csv(var + '.csv', index_col=0)
    df = df.merge(gdpcap, on='country_code')
    model = lowess(df[var], df['gdp_per_capita'], return_sorted=False)
    df[var + '_resid'] = df[var] - model
    df_resid = df.drop([var, 'gdp_per_capita'], axis=1)
    df.to_csv(var + '_resid.csv')
    