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

# run this file first.
# quit python and run download_unhcr_data.py
# run lowess_models.py
# then run merge_wdi_vars.py and merge_unhcr_wdi.py
# to create map_data.csv

import requests
import zipfile
import io
import os
import pandas as pd

wd = os.path.expanduser('~/multi-maps/data')
os.chdir(wd)

# download zip archives of csv data files from World Bank, World Development Indicators
# unzip them
# manipulate them to keep relevant years, remove regions (leaving only countries)
# write to csv
# commented out data sets are left here to remind me not to retrieve them later; they are full of missing data



regions = ['ARB', 'CEB', 'CSS', 'EAP', 'EAR', 'EAS', 'ECA', 'ECS', 'EMU', 'EUU', 'FCS', 'HIC', 'HPC', 'IBD', 'IBT', 'IDA', 'IDB', 'IDX', 'INX', 'LAC', 'LCN', 'LDC', 'LIC', 'LMC', 'LMY', 'LTE', 'MEA', 'MIC', 'MNA', 'NAC', 'OED', 'OSS', 'PRE', 'PSS', 'PST', 'SAS', 'SSA', 'SSF', 'SST', 'TEA', 'TEC', 'TLA', 'TMN', 'TSA', 'TSS', 'UMC', 'WLD']

data_dictionary = [
      
        
# Population, total   
        
    {'name' : 'population',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SP.POP.TOTL?downloadformat=csv',
     'long_name' : 'Population, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Population)'
     },
        
# International migrant stock (% of population    
        
    {'name' : 'migrant_stock',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SM.POP.TOTL.ZS?downloadformat=csv',
     'long_name' : 'International migrant stock (% of population), 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'International migrant stock (% of population)'
     },

        
# gross domestic product per capita, current USD at PPP

    {'name' : 'gdp_per_capita',
     'url' : 'http://api.worldbank.org/v2/en/indicator/NY.GDP.PCAP.PP.CD?downloadformat=csv',
     'long_name' : 'Gross Domestic Product per capita, Current USD at PPP, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'GDP per capita'
     },
     
# maternal mortality rate per 100000 live births
    {'name' : 'maternal_mortality_rate',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SH.STA.MMRT?downloadformat=csv',
     'long_name' : 'Maternal Mortality Rate: materal deaths per 100,000 live births, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Maternal Mortality Rate'
     },

#life expectancy at birth
    {'name' :'life_expectancy',
     'url': 'http://api.worldbank.org/v2/en/indicator/SP.DYN.LE00.IN?downloadformat=csv',
     'long_name' : 'Life Expectancy at Birth, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Life Expectancy'
     },
     
# hiv prevalence
    {'name' : 'hiv_prevalence',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SH.DYN.AIDS.ZS?downloadformat=csv',
     'long_name' : 'HIV prevalance, %, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'HIV Prevalence'
     },
     
# urban population, percent of population
    {'name' : 'urbpop',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SP.URB.TOTL.IN.ZS?downloadformat=csv',
     'long_name' : 'Urban Population (% of Total), 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Urban Population'
     },

     
# share of income held by lowest 20% of population
    {'name' : 'lowest_twenty_income_share',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SI.DST.FRST.20?downloadformat=csv',
     'long_name' : 'Share of income held by lowest 20% of population, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Income share'
     },
     
# net official development assistance as percent of gross national income
    {'name' :'oda_pct_of_gni',
     'url' : 'http://api.worldbank.org/v2/en/indicator/DT.ODA.ODAT.GN.ZS?downloadformat=csv',
     'long_name' : 'Official development assistance (net), % of gross national income, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'ODA as % of GNI'
     },

# net migration
    {'name' : 'net_migration',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SM.POP.NETM?downloadformat=csv',
     'long_name' : 'Net migration, 2017',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Net migration'
     },

# poverty headcount ratio, $1.90 at 2011 PPP
    {'name' : 'poverty_headcount_ratio_190_2011_ppp',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SI.POV.DDAY?downloadformat=csv',
     'long_name' : 'Poverty headcount ratio, USD $1.90 at 2011 PPP, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Poverty headcount ratio'
     },

# access to electricity, % of population
    {'name' : 'access_to_electricity_pct_of_population',
     'url': 'http://api.worldbank.org/v2/en/indicator/EG.ELC.ACCS.ZS?downloadformat=csv',
     'long_name' : 'Access to electricity, % of population, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Access to electricity'
     },
         
# CO2 emissions, metric tons per capita -- 2014 is latest available
    {'name' : 'co2_tons_per_capita',
     'url' : 'http://api.worldbank.org/v2/en/indicator/EN.ATM.CO2E.PC?downloadformat=csv',
     'long_name' : 'C02 emissions, metric tons per capita, 2014',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'C02 emissions per capita'
     },
     
# mortality rate under 5 per 1000 live births
    {'name' : 'mortality_under_5_per_1000_live_births',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SH.DYN.MORT?downloadformat=csv',
     'long_name' : 'Mortality rate under age 5 per 1000 live births, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Mortality rate under age 5'
     },

# energy use per capita (kg equiv oil) -- 2014 is the latest available
    {'name' : 'energy_use_per_capita',
     'url': 'http://api.worldbank.org/v2/en/indicator/EG.USE.PCAP.KG.OE?downloadformat=csv',
     'long_name' : 'Energy use per capita, kg equivalent of petroleum, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Energy use per capita'
     },


# remittances received, current USD
    {'name' : 'remittances',
     'url' : 'http://api.worldbank.org/v2/en/indicator/BX.TRF.PWKR.CD.DT?downloadformat=csv',
     'long_name' : 'Remittances received, current USD, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Remittances received'
     },

# revenue, % of gdp
    {'name' : 'revenue_pct_gdp',
     'url' : 'http://api.worldbank.org/v2/en/indicator/GC.REV.XGRT.GD.ZS?downloadformat=csv',
     'long_name' : 'Government revenue, % of gross domestic product, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Revenue, % of GDP'
      },

# govt expenditure on education, % of GDP
    {'name' : 'govt_exp_educ_pct_gdp',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SE.XPD.TOTL.GD.ZS?downloadformat=csv',
     'long_name' : 'Government expenditures on education, % of gross domestic product, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Education expenditure, % of GDP'
     },

# female literacy, over 15, %
    {'name' : 'female_literacy_pct',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SE.ADT.LITR.FE.ZS?downloadformat=csv',
     'long_name' : 'Female literacy over age 15, %, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Female literacy'
     },

     
# external debt, % of GNI
    {'name' : 'external_debt_pct_GNI',
     'url' : 'http://api.worldbank.org/v2/en/indicator/DT.DOD.DECT.GN.ZS?downloadformat=csv',
     'long_name' : 'External debt, % of gross national income, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'External debt, % of GNI'
     },

# FDI, net, current USD
    {'name' : 'fdi_net_current_usd',
     'url' : 'http://api.worldbank.org/v2/en/indicator/BX.KLT.DINV.CD.WD?downloadformat=csv',
     'long_name' : 'Foreign direct investment, net, current USD, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Net FDI, current USD'
     },

# strength of legal rights, 0=low, 12=high
    {'name' : 'strength_legal_rights_0_12',
     'url' : 'http://api.worldbank.org/v2/en/indicator/IC.LGL.CRED.XQ?downloadformat=csv',
     'long_name' : 'Strength of legal rights, 0-12 scale, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Strength of legal rights'
    },     

# adolescent fertility rate, 15-19, per 1000 live births
    {'name' : 'adolescent_fertility_rate',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SP.ADO.TFRT?downloadformat=csv',
     'long_name' : 'Adolescent fertility rate (age 15-19), per 1000 live births, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Adolescent fertility rate'
     },
     
# fertility rate, births per woman
    {'name' : 'fertility_rate',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SP.DYN.TFRT.IN?downloadformat=csv',
     'long_name' : 'Fertility rate, births per woman, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Fertility rate'
     },

# female employment, % of total labor force
    {'name' :'female_employment_pct_of_total',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SL.TLF.TOTL.FE.ZS?downloadformat=csv',
     'long_name' : 'Female employment, % of total labor force, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Female employment'
     },
# share of income held by lowest 10% of population
  # ---------->  # NOTE: Indonesia data appears to be missing
     {'name' : 'lowest_ten_income_share',
      'url' : 'http://api.worldbank.org/v2/en/indicator/SI.DST.FRST.10?downloadformat=csv',
      'long_name' : 'Share of income held by lowest 10% of population, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Income share, lowest 10%'
      },
      
# share of income held by highest 10% of population
  # ---------->  # NOTE: Indonesia data appears to be missing
     {'name' : 'highest_ten_income_share',
      'url' : 'http://api.worldbank.org/v2/en/indicator/SI.DST.10TH.10?downloadformat=csv',
      'long_name' : 'Share of income held by highest 10% of population, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Income share, highest 10%'
      },
      

      
      

# safety net (etc.) data commented out because data is almost all missing
     
## adequacy of unemployment and active labor market programs
#     {'name' : 'adequacy_unemployment_almp',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_lm_alllm.adq_pop_tot?downloadformat=csv',
#      'long_name' : 'Adequacy of unemployment benefits and active labor market programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Adequacy of unemployment benefits and ALMP'
#      },
      
## coverage of unemployment and active labor market programs
#     {'name' : 'coverage_unemployment_almp',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_lm_alllm.cov_pop_tot?downloadformat=csv',
#      'long_name' : 'Coverage of unemployment benefits and active labor market programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Coverage of unemployment benefits and ALMP'
#      },
      
## adequacy of social safety net programs
#     {'name' : 'adequacy_social_safety_net',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_sa_allsa.adq_pop_tot?downloadformat=csv',
#      'long_name' : 'Adequacy of social safety net programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Adequacy of social safety net programs'
#      },
#      
## coverage of social safety net programs
#     {'name' : 'coverage_social_safety_net',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_sa_allsa.cov_pop_tot?downloadformat=csv',
#      'long_name' : 'Coverage of social safety net programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Coverage of social safety net programs'
#      },
      
## adequacy of social protection and labor programs
#     {'name' : 'adequacy_social_protection',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_allsp.adq_pop_tot?downloadformat=csv',
#      'long_name' : 'Adequacy of social protection and labor programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Adequacy of social protection and labor programs'
#      },

## coverage of social protection and labor programs
#     {'name' : 'coverage_social_protection',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/per_allsp.cov_pop_tot?downloadformat=csv',
#      'long_name' : 'Coverage of social protection and labor programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Coverage of social protection and labor programs'
#      },

# trade (% of GDP)
     {'name' : 'trade_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/en/indicator/NE.TRD.GNFS.ZS?downloadformat=csv',
      'long_name' : 'Trade, % of gross domestic product, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Trade, % of GDP'
      },
      
# Individuals using the Internet (% of population)
     {'name' : 'use_internet_pct_pop',
      'url' : 'http://api.worldbank.org/v2/en/indicator/IT.NET.USER.ZS?downloadformat=csv',
      'long_name' : 'Individuals using the Internet (% of population), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Internet users, & of population'
      },
     
# Mobile cellular subscriptions (per 100 people)
     {'name' : 'mobile_phone_subscriptions_pct_pop',
      'url' : 'http://api.worldbank.org/v2/en/indicator/IT.CEL.SETS.P2?downloadformat=csv',
      'long_name' : 'Mobile cellular subscriptions, % of population, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Mobile phone subscriptions, & of population'
      },
     
# Time required to start a business (days)
     {'name' : 'days_required_to_start_business',
      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.REG.DURS?downloadformat=csv',
      'long_name' : 'Time required to start a business (days), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Time required to start a business (days)'
      },
   
# data mostly missing
## Firms with female participation in ownership (% of firms)
#     {'name' : 'firms_female_top_mgmt_pct',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.FRM.FEMO.ZS?downloadformat=csv',
#      'long_name' : 'Firms with female participation in ownership (% of firms)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Firms with female participation in ownership (% of firms)'
#      },
     
# data mostly missing
## Informal payments to public officials (% of firms)
#     {'name' : 'informal_payments_to_officials_pct_firms',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.FRM.CORR.ZS?downloadformat=csv',
#      'long_name' : 'Informal payments to public officials (% of firms)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Informal payments to public officials (% of firms)'
#      },
#      
## Bribery incidence (% of firms experiencing at least one bribe payment request)
#     {'name' : 'bribe_incidence_pct_firm',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.FRM.BRIB.ZS?downloadformat=csv',
#      'long_name' : 'Bribery incidence (% of firms experiencing at least one bribe payment request)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Bribery incidence (% of firms experiencing at least one bribe payment request)'
#      },
      
# Ease of doing business index (1=most business-friendly regulations)
# ------------> # NOTE: data from 2018
     {'name' : 'ease_doing_business',
      'url' : 'http://api.worldbank.org/v2/en/indicator/IC.BUS.EASE.XQ?downloadformat=csv',
      'long_name' : 'Ease of doing business index (1=most business-friendly regulations), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Ease of doing business index (1=most business-friendly regulations)'
      },
      
# Tax revenue (% of GDP)
     {'name' : 'tax_revenue_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/en/indicator/GC.TAX.TOTL.GD.ZS?downloadformat=csv',
      'long_name' : 'Tax revenue (% of GDP), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Tax revenue (% of GDP)'
      },
      
# Net lending (+) / net borrowing (-) (% of GDP)
     {'name' : 'net_lending_borrowing_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/en/indicator/GC.NLD.TOTL.GD.ZS?downloadformat=csv',
      'long_name' : 'Net lending (+) / net borrowing (-) (% of GDP), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Net lending (+) / net borrowing (-) (% of GDP)'
      },

# Central government debt, total (% of GDP)
     {'name' : 'central_govt_debt_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/en/indicator/GC.DOD.TOTL.GD.ZS?downloadformat=csv',
      'long_name' : 'Central government debt, total (% of GDP), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Central government debt, total (% of GDP)'
      },  

# all data missing      
# Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)
#     {'name' : 'account_ownership_pct_population_15_plus',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/FX.OWN.TOTL.ZS?downloadformat=csv',
#      'long_name' : 'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)'
#      }, 

# Risk premium on lending (lending rate minus treasury bill rate, %)
     {'name' : 'risk_premium',
      'url' : 'http://api.worldbank.org/v2/en/indicator/FR.INR.RISK?downloadformat=csv',
      'long_name' : 'Risk premium on lending (lending rate minus treasury bill rate, %), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Risk premium on lending'
      },
       
# Terrestrial and marine protected areas (% of total territorial area)
     # data are from 2016
     {'name' : 'biodiversity_protected_areas',
      'url' : 'http://api.worldbank.org/v2/en/indicator/ER.PTD.TOTL.ZS?downloadformat=csv',
      'long_name' : 'Terrestrial and marine protected areas (% of total territorial area), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Terrestrial and marine protected areas (% of total territorial area)'
      },
      
# Renewable internal freshwater resources per capita (cubic meters)
     {'name' : 'renewable_freshwater_per_capita',
      'url' : 'http://api.worldbank.org/v2/en/indicator/ER.H2O.INTR.PC?downloadformat=csv',
      'long_name' : 'Renewable internal freshwater resources per capita (cubic meters), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Renewable internal freshwater resources per capita (cubic meters)'
      },
      
## all data missing
## Level of water stress: freshwater withdrawal as a proportion of available freshwater resources
#     {'name' : 'frewshwater_stress',
#      'url' : 'http://api.worldbank.org/v2/en/indicator/ER.H2O.FWST.ZS?downloadformat=csv',
#      'long_name' : 'Level of water stress: freshwater withdrawal as a proportion of available freshwater resources',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Level of water stress: freshwater withdrawal as a proportion of available freshwater resources'
#      }, 

# Population living in slums (% of urban population)
# NOTE: data from 2014
     {'name' : 'slum_population_pct_urban_population',
      'url' : 'http://api.worldbank.org/v2/en/indicator/EN.POP.SLUM.UR.ZS?downloadformat=csv',
      'long_name' : 'Population living in slums (% of urban population), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Population living in slums (% of urban population)'
      }, 

# PM2.5 air pollution, population exposed to levels exceeding WHO guideline value (% of total)
     {'name' : 'pm25_pct_population',
      'url' : 'http://api.worldbank.org/v2/en/indicator/EN.ATM.PM25.MC.ZS?downloadformat=csv',
      'long_name' : 'PM2.5 air pollution, population exposed to levels exceeding WHO guideline value (% of total), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'PM2.5 air pollution exposure, % of population)'
      }, 

# Foreign direct investment, net (BoP, current US$
     {'name' : 'net_fdi',
      'url' : 'http://api.worldbank.org/v2/en/indicator/BN.KLT.DINV.CD?downloadformat=csv',
      'long_name' : 'Foreign direct investment, net (BoP, current US$), 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Net foreign direct investment)'
      } ,

# Literacy rate, adults
    {'name': 'literacy_rate',
     'url' : 'http://api.worldbank.org/v2/en/indicator/SE.ADT.LITR.ZS?downloadformat=csv',
     'long_name' : 'Adult Literacy Rate, %, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Adult Literacy Rate'
     },
     
# Gini coefficient     
     {'name' : 'gini_coefficient',
      'url' : 'http://api.worldbank.org/v2/en/indicator/SI.POV.GINI?downloadformat=csv',
      'long_name' : 'Gini Coefficient',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Gini Coefficient'
      }
      
      
]

for i in range(len(data_dictionary)):
    data = requests.get(data_dictionary[i]['url'])
    zip = zipfile.ZipFile(io.BytesIO(data.content))
    names = zipfile.ZipFile.namelist(zip)
    csv = pd.read_csv(zipfile.ZipFile.extract(zip, names[1]), header=2)
    if data_dictionary[i]['name'] == 'co2_tons_per_capita' or data_dictionary[i]['name'] == 'energy_use_per_capita':
        csv = csv[['Country Name', 'Country Code', '2014']]
    elif data_dictionary[i]['name'] == 'net_migration':
        csv = csv[['Country Name', 'Country Code', '2017']]
    elif data_dictionary[i]['name'] == 'ease_doing_business':
        csv = csv[['Country Name', 'Country Code', '2018']]    
    elif data_dictionary[i]['name'] == 'biodiversity_protected_areas':
        csv = csv[['Country Name', 'Country Code', '2016']]    
    elif data_dictionary[i]['name'] == 'renewable_freshwater_per_capita':
        csv = csv[['Country Name', 'Country Code', '2014']]    
    elif data_dictionary[i]['name'] == 'slum_population_pct_urban_population':
        csv = csv[['Country Name', 'Country Code', '2014']]    
    else:
        csv = csv[['Country Name', 'Country Code', '2015']].copy()
        
    if data_dictionary[i]['name'] == 'co2_tons_per_capita' or data_dictionary[i]['name'] == 'energy_use_per_capita':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2014': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'net_migration':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2017': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'ease_doing_business':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2018': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'biodiversity_protected_areas':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2016': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'renewable_freshwater_per_capita':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2014': data_dictionary[i]['name']})
    elif data_dictionary[i]['name'] == 'slum_population_pct_urban_population':
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2014': data_dictionary[i]['name']})
    else:
        csv = csv.rename(index =  str, columns={'Country Name' : 'country', 'Country Code': 'country_code', '2015': data_dictionary[i]['name']})
    
# we want only countries, not regions
    for reg in regions:
        csv = csv[csv.country_code != reg] 
    csv.to_csv(data_dictionary[i]['name']+'.csv', index=False)

varnames = []
for i in range(len(data_dictionary)):
    varnames.append(data_dictionary[i]['name'])
varnames = pd.DataFrame(varnames)
varnames.to_csv('varnames.csv')

