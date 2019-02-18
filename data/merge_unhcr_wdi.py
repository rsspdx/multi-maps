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


asylum_idps_refugees = pd.read_csv('asylum_idps_refugees.csv')
recognized_total_decisions = pd.read_csv('recognized_total_decisions.csv')
