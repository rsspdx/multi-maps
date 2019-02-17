#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 16:01:16 2019

@author: rs
"""

#!/usr/bin/env pygeo
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  4 07:09:57 2019

@author: rs
"""

import requests
import os
import pandas as pd

wd = os.path.expanduser('~/data/geo/multi-maps/data')
os.chdir(wd)



# unhcr data
#unhcr_data_dictionary = [
## persons of concern
#    {'name' : 'persons_of_concern',
#     'url' : 'http://popstats.unhcr.org/en/persons_of_concern.csv',
#     'long_name' : 'Persons of concern',
#     'source' : 'UNHCR, Population Statistics',
#     'short_name' : 'Persons of concern'
#     },
#
## asylum seekers
#     {'name' : 'asylum_seekers',
#      'url' : 'http://popstats.unhcr.org/en/asylum_seekers.csv',
#      'long_name' : 'Asylum seekers',
#      'source' : 'UNHCR, Population Statistics',
#      'short_name' : 'Asylum seekers'
#      },
#     
## refugees
#     {'name' : 'refugees',
#      'url' : 'http://popstats.unhcr.org/en/time_series.csv',
#      'long_name' : 'Refugees',
#      'source' : 'UNHCR, Population Statistics',
#      'short_name' : 'Refugees'
#      }
#]

# download UNHCR data - Population Statistics - Persons of Concern
poc = requests.get('http://popstats.unhcr.org/en/persons_of_concern.csv')
# decode it to a string
poc_string = poc.content.decode('utf-8', errors='ignore')[188:]
# remove commas from two country names
poc_string = poc_string.replace('"China, Hong Kong SAR"', 'China HK')
poc_string = poc_string.replace('"China, Macao SAR"', 'China Macao')
# split it to a list, split rows by commas
poc_string = poc_string.split('\r\n')
poc_list = []
for i in range(len(poc_string)-1):
    poc_list.append(poc_string[i].split(','))
# get first row as varnames
header = poc_list[0]
# zip varnames together with the data to create a spreadsheet-like list of dicts
poc_dict_list = []
for i in range(len(poc_list)-1):
    poc_dict_list.append(dict(zip(header, poc_list[i])))
# turn it into a pandas data frame
poc_df = pd.DataFrame(poc_dict_list)
# keep year 2015 only
poc_df_2015 = poc_df[poc_df['Year'] == '2015']
poc_df_2015.to_csv('poc_2015.csv')
# give the variables usable names
poc_df_2015 = poc_df_2015.rename(index=str, columns={
        'Asylum-seekers (pending cases)' : 'asylum_seekers',
        'Country / territory of asylum/residence' : 'country',
        'Internally displaced persons (IDPs)' : 'idps',
        'Origin' : 'country_of_origin',
        'Others of concern' : 'others_of_concern',
        'Refugees (incl. refugee-like situations)' : 'refugees',
        'Returned IDPs' : 'returned_idps',
        'Returned refugees' : 'returned_refugees',
        'Stateless persons' : 'stateless_persons',
        'Total Population' : 'total_population',
        'Year' : 'year'
        })
    
# get sums of asylum_seekers, idps, refugees -- first need to convert these to ints
poc_df_2015.asylum_seekers = poc_df_2015.asylum_seekers[poc_df_2015.asylum_seekers != ''].astype('int32')
poc_df_2015.idps = poc_df_2015.idps[poc_df_2015.idps != ''].astype('int32')
poc_df_2015.refugees = poc_df_2015.refugees[poc_df_2015.refugees != ''].astype('int32')

asylum_seekers = poc_df_2015.groupby('country').asylum_seekers.sum()
idps = poc_df_2015.groupby('country').idps.sum()
refugees = poc_df_2015.groupby('country').refugees.sum()

#merge asylum_seekers, idps, refugees to a single data set
asylum_seekers = pd.DataFrame(asylum_seekers)
idps = pd.DataFrame(idps)
refugees = pd.DataFrame(refugees)

asylum_idps_refugees = asylum_seekers.merge(idps, on='country')
asylum_idps_refugees = asylum_idps_refugees.merge(refugees, on='country')
asylum_idps_refugees.to_csv('asylum_idps_refugees.csv')

# download UNHCR data - Population Statistics - Asylum Seekers
asylum = requests.get('http://popstats.unhcr.org/en/asylum_seekers.csv')
# decode it to a string
asylum_string = asylum.content.decode('utf-8', errors='ignore')[197:]
# remove commas from two country names
asylum_string = asylum_string.replace('"China, Hong Kong SAR"', 'China HK')
asylum_string = asylum_string.replace('"China, Macao SAR"', 'China Macao')
# split it to a list, split rows by commas
asylum_string = asylum_string.split('\r\n')
asylum_list = []
for i in range(len(asylum_string)-1):
    asylum_list.append(asylum_string[i].split(','))
# get first row as varnames
header = asylum_list[0]
# zip varnames together with data to create a spreadsheet-like list of dicts
asylum_dict_list = []
for i in range(len(asylum_list)-1):
    asylum_dict_list.append(dict(zip(header, asylum_list[i])))
# turn it into a pandas data frame
asylum_df = pd.DataFrame(asylum_dict_list)
# keep year 2015 only
asylum_df_2015 = asylum_df[asylum_df['Year'] == '2015']
asylum_df_2015.to_csv('asylum_csv_2015.csv')
# give the variables usable names
asylum_df_2015 = asylum_df_2015.rename(index=str, columns={
        'Applied during year' : 'applied_during_year',
        'Country / territory of asylum/residence' : 'country',
        'Origin' : 'country_of_origin',
        'Otherwise closed' : 'otherwise_closed',
        'RSD Procedure type / level' : 'rsd_procedure_type',
        'Rejected' : 'rejected',
        'Tota pending start-year' : 'total_pending_start_year',
        'Total decisions' : 'total_decisions',
        'Total pending end-year' : 'total_pending_end_year',
        'Year' : 'year',
        'of which UNHCR-assisted' : 'of_which_unhcr_assisted',
        'statistics.filter.decisions_other' : 'decisions_other',
        'statistics.filter.decisions_recognized' : 'recognized'
        })
# get sums of recognized and total_decisions -- first need to convert these to int
asylum_df_2015.total_decisions = asylum_df_2015.total_decisions[asylum_df_2015.total_decisions != ''].astype('int32')
asylum_df_2015.recognized = asylum_df_2015.recognized[asylum_df_2015.recognized != ''].astype('int32')

recognized_2015 = asylum_df_2015.groupby('country').recognized.sum()
total_decisions_2015 = asylum_df_2015.groupby('country').total_decisions.sum()

# merge recognzed with total decisions
recognized_2015 = pd.DataFrame(recognized_2015)
total_decisions_2015 = pd.DataFrame(total_decisions_2015)
recognized_total_decisions_2015 = recognized_2015.merge(total_decisions_2015, on='country')
recognized_total_decisions_2015['recognition_rate'] = 100 * recognized_total_decisions_2015.recognized / recognized_total_decisions_2015.total_decisions
recognized_total_decisions_2015.to_csv('recognized_total_decisions.csv')