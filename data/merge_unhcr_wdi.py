#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 10:07:07 2019

@author: rs
"""

import pandas as pd
import os

wd = os.path.expanduser('~/multi-maps/data')
os.chdir(wd)


asylum_idps_refugees = pd.read_csv('asylum_idps_refugees.csv', index_col=0)
recognized_total_decisions = pd.read_csv('recognized_total_decisions.csv', index_col=0)
wdi_vars = pd.read_csv('wdi_vars.csv', index_col=0)
country_iso_2_iso_3 = pd.read_csv('country_iso_2_iso_3.csv', index_col=0)

unhcr_vars = asylum_idps_refugees.merge(recognized_total_decisions, on='country')
unhcr_vars = unhcr_vars.merge(country_iso_2_iso_3, on='country')

wdi_vars = wdi_vars.merge(unhcr_vars, left_on=['country', 'country_code'], right_on=['country', 'iso_3'])
wdi_vars.to_csv('map_data.csv')