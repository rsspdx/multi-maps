#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:07:07 2019

@author: rs
"""

import pandas as pd
import os
import statsmodels.api as sm

wd = os.path.expanduser('~/multi-maps/data_v2')
os.chdir(wd)


gdpcap = pd.read_csv('gdp_per_capita.csv')
asylum_idps_refugees = pd.read_csv('asylum_idps_refugees.csv')
recognized_total_decisions = pd.read_csv('recognized_total_decisions.csv')
wdi_vars = pd.read_csv('wdi_vars.csv')
country_iso_2_iso_3 = pd.read_csv('country_iso_2_iso_3.csv')
happiness = pd.read_csv('happiness.2015.csv', index_col=False)
happiness.to_csv('happiness.csv')
ti_cpi = pd.read_csv('ti_cpi_2015.csv', index_col=False)
ti_cpi = ti_cpi.drop('country', 1)
ti_cpi.to_csv('ti_cpi.csv')
asylum_seekers = pd.read_csv('asylum_seekers.csv', index_col=False)
idps = pd.read_csv('idps.csv')
refugees = pd.read_csv('refugees.csv', index_col=False)
recognition_rate = pd.read_csv('recognition_rate.csv', index_col=False)

unhcr_vars = asylum_idps_refugees.merge(recognized_total_decisions, on='country')
unhcr_vars = unhcr_vars.merge(country_iso_2_iso_3, on='country')
unhcr_vars['country_code'] = unhcr_vars['iso_3']

refugees = refugees.merge(country_iso_2_iso_3, on='country')
refugees = refugees.drop('country', 1)
refugees['country_code'] = refugees['iso_3']
refugees.to_csv('refugees.csv')

asylum_seekers = asylum_seekers.merge(country_iso_2_iso_3, on='country')
asylum_seekers = asylum_seekers.drop('country', 1)
asylum_seekers['country_code'] = asylum_seekers['iso_3']
asylum_seekers.to_csv('asylum_seekers.csv')

idps = idps.merge(country_iso_2_iso_3, on='country')
idps = idps.drop('country', 1)
idps['country_code'] = idps['iso_3']
idps.to_csv('idps.csv')

recognition_rate = recognition_rate.merge(country_iso_2_iso_3, on='country')
recognition_rate['country_code'] = recognition_rate['iso_3']
recognition_rate = recognition_rate.drop('country', 1)
recognition_rate.to_csv('recognition_rate.csv')

wdi_vars = wdi_vars.merge(unhcr_vars, on='country_code')

wdi_vars['refugees_per_pop'] = wdi_vars['refugees'] / wdi_vars['population']
wdi_vars['asylum_seekers_per_pop'] = wdi_vars['asylum_seekers'] / wdi_vars['population']

wdi_vars = wdi_vars.merge(happiness, on='country_code')
wdi_vars = wdi_vars.merge(ti_cpi, on='country_code')


filenames = pd.DataFrame(wdi_vars.columns.tolist())
filenames.to_csv('map_data_varnames.csv')

newvars = ['asylum_seekers', 'idps', 'refugees', 'recognition_rate', 'happiness', 'ti_cpi']
lowess = sm.nonparametric.lowess

for var in newvars:
    df = pd.read_csv(var + '.csv', index_col=False)
    df = df.merge(gdpcap, on='country_code')
    model = lowess(df[var], df['gdp_per_capita'], return_sorted=False)
    df = df.drop('gdp_per_capita', 1)
    df.to_csv(var + '.csv')
    df[var + '_resid'] = df[var] - model
#    wdi_vars.merge(df_resid, on='country_code')
    df.to_csv(var + '_resid.csv')
    
# a kludge to fix the 'country' variable in asylum_seekers, ti_cpi, and happiness
asylum_seekers = pd.read_csv('asylum_seekers.csv')
asylum_seekers['country'] = asylum_seekers['country_x']
asylum_seekers.to_csv('asylum_seekers.csv')

happiness = pd.read_csv('happiness.csv')
happiness['country'] = happiness['country_x']
happiness.to_csv('happiness.csv')

asylum_seekers_resid = pd.read_csv('asylum_seekers_resid.csv')
asylum_seekers_resid['country'] = asylum_seekers_resid['country_x']
asylum_seekers_resid.to_csv('asylum_seekers_resid.csv')

happiness_resid = pd.read_csv('happiness_resid.csv')
happiness_resid['country'] = happiness_resid['country_x']
happiness_resid.to_csv('happiness_resid.csv')

ti_cpi = ti_cpi.merge(gdpcap, on='country_code')
ti_cpi = ti_cpi.drop('gdp_per_capita', 1)
ti_cpi.to_csv('ti_cpi.csv')

wdi_vars.to_csv('map_data.csv')

    

    





















