import json
import requests
from django.core.management.base import BaseCommand

from get_data_app.models import Chart, DataRow, Country

class Command(BaseCommand):

    def handle(self, *args, **options):

        # PURGE DATA
        Chart.objects.all().delete()
        DataRow.objects.all().delete()
        Country.objects.all().delete()


        # csvs = [{
        #     'file': 'file1.csv',
        #     'chart data type': 'population'
        # }]

        #for csv in csvs:
            # load the file csv['file']
            # save the data into the table with the type csv['chart data type']
        
        chart_data = [    
    {'name' : 'population',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json&date=2015&per_page=300',
     'long_name' : 'Population',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Population)'
     },
        
# International migrant stock (% of population    
        
    {'name' : 'migrant_stock',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SM.POP.TOTL.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'International migrant stock (% of population)',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'International migrant stock (% of population)'
     },

        
# gross domestic product per capita, current USD at PPP

    {'name' : 'gdp_per_capita',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.PP.CD?format=json&date=2015&per_page=300',
     'long_name' : 'Gross Domestic Product per capita, Current USD at PPP, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'GDP per capita'
     },
     
# maternal mortality rate per 100000 live births
    {'name' : 'maternal_mortality_rate',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SH.STA.MMRT?format=json&date=2015&per_page=300',
     'long_name' : 'Maternal Mortality Rate: materal deaths per 100,000 live births, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Maternal Mortality Rate'
     },

#life expectancy at birth
    {'name' :'life_expectancy',
     'url': 'http://api.worldbank.org/v2/country/all/indicator/SP.DYN.LE00.IN?format=json&date=2015&per_page=300',
     'long_name' : 'Life Expectancy at Birth, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Life Expectancy'
     },
     
# hiv prevalence
    {'name' : 'hiv_prevalence',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SH.DYN.AIDS.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'HIV prevalance, %, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'HIV Prevalence'
     },
     
# urban population, percent of population
    {'name' : 'urbpop',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SP.URB.TOTL.IN.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'Urban Population (% of Total), 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Urban Population'
     },

     
# share of income held by lowest 20% of population
    {'name' : 'lowest_twenty_income_share',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SI.DST.FRST.20?format=json&date=2015&per_page=300',
     'long_name' : 'Share of income held by lowest 20% of population, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Income share'
     },
     
# net official development assistance as percent of gross national income
    {'name' :'oda_pct_of_gni',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/DT.ODA.ODAT.GN.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'Official development assistance (net), % of gross national income, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'ODA as % of GNI'
     },

# net migration
    {'name' : 'net_migration',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SM.POP.NETM?format=json&date=2017&per_page=300',
     'long_name' : 'Net migration, 2017',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Net migration'
     },

# poverty headcount ratio, $1.90 at 2011 PPP
    {'name' : 'poverty_headcount_ratio_190_2011_ppp',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SI.POV.DDAY?format=json&date=2015&per_page=300',
     'long_name' : 'Poverty headcount ratio, USD $1.90 at 2011 PPP, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Poverty headcount ratio'
     },

# access to electricity, % of population
    {'name' : 'access_to_electricity_pct_of_population',
     'url': 'http://api.worldbank.org/v2/country/all/indicator/EG.ELC.ACCS.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'Access to electricity, % of population, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Access to electricity'
     },
         
# CO2 emissions, metric tons per capita -- 2014 is latest available
    {'name' : 'co2_tons_per_capita',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/EN.ATM.CO2E.PC?format=json&date=2014&per_page=300',
     'long_name' : 'C02 emissions, metric tons per capita, 2014',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'C02 emissions per capita'
     },
     
# mortality rate under 5 per 1000 live births
    {'name' : 'mortality_under_5_per_1000_live_births',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SH.DYN.MORT?format=json&date=2015&per_page=300',
     'long_name' : 'Mortality rate under age 5 per 1000 live births, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Mortality rate under age 5'
     },

# energy use per capita (kg equiv oil) -- 2014 is the latest available
    {'name' : 'energy_use_per_capita',
     'url': 'http://api.worldbank.org/v2/country/all/indicator/EG.USE.PCAP.KG.OE?format=json&date=2014&per_page=300',
     'long_name' : 'Energy use per capita, kg equivalent of petroleum, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Energy use per capita'
     },


# remittances received, current USD
    {'name' : 'remittances',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/BX.TRF.PWKR.CD.DT?format=json&date=2015&per_page=300',
     'long_name' : 'Remittances received, current USD',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Remittances received'
     },

# revenue, % of gdp
    {'name' : 'revenue_pct_gdp',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/GC.REV.XGRT.GD.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'Government revenue, % of gross domestic product, 2015',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Revenue, % of GDP'
      },

# govt expenditure on education, % of GDP
    {'name' : 'govt_exp_educ_pct_gdp',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SE.XPD.TOTL.GD.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'Government expenditures on education, % of gross domestic product, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Education expenditure, % of GDP'
     },

# female literacy, over 15, %
    {'name' : 'female_literacy_pct',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SE.ADT.LITR.FE.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'Female literacy over age 15, %, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Female literacy'
     },

     
# external debt, % of GNI
    {'name' : 'external_debt_pct_GNI',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/DT.DOD.DECT.GN.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'External debt, % of gross national income, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'External debt, % of GNI'
     },

# FDI, net, current USD
    {'name' : 'fdi_net_current_usd',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/BX.KLT.DINV.CD.WD?format=json&date=2015&per_page=300',
     'long_name' : 'Foreign direct investment, net, current USD, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Net FDI, current USD'
     },

# strength of legal rights, 0=low, 12=high
    {'name' : 'strength_legal_rights_0_12',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/IC.LGL.CRED.XQ?format=json&date=2015&per_page=300',
     'long_name' : 'Strength of legal rights, 0-12 scale, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Strength of legal rights'
    },     

# adolescent fertility rate, 15-19, per 1000 live births
    {'name' : 'adolescent_fertility_rate',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SP.ADO.TFRT?format=json&date=2015&per_page=300',
     'long_name' : 'Adolescent fertility rate (age 15-19), per 1000 live births, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Adolescent fertility rate'
     },
     
# fertility rate, births per woman
    {'name' : 'fertility_rate',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SP.DYN.TFRT.IN?format=json&date=2015&per_page=300',
     'long_name' : 'Fertility rate, births per woman, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Fertility rate'
     },

# female employment, % of total labor force
    {'name' :'female_employment_pct_of_total',
     'url' : 'http://api.worldbank.org/v2/country/all/indicator/SL.TLF.TOTL.FE.ZS?format=json&date=2015&per_page=300',
     'long_name' : 'Female employment, % of total labor force, 2015',
     'source' : 'World Bank, World Development Indicators',
     'short_name' : 'Female employment'
     },
# share of income held by lowest 10% of population
  # ---------->  # NOTE: Indonesia data appears to be missing
     {'name' : 'lowest_ten_income_share',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/SI.DST.FRST.10?format=json&date=2015&per_page=300',
      'long_name' : 'Share of income held by lowest 10% of population',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Income share, lowest 10%'
      },
      
# share of income held by highest 10% of population
  # ---------->  # NOTE: Indonesia data appears to be missing
     {'name' : 'highest_ten_income_share',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/SI.DST.10TH.10?format=json&date=2015&per_page=300',
      'long_name' : 'Share of income held by highest 10% of population',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Income share, highest 10%'
      },
      

      
      

# safety net (etc.) data commented out because data is almost all missing
     
## adequacy of unemployment and active labor market programs
#     {'name' : 'adequacy_unemployment_almp',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/per_lm_alllm.adq_pop_tot?format=json&date=2015&per_page=300',
#      'long_name' : 'Adequacy of unemployment benefits and active labor market programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Adequacy of unemployment benefits and ALMP'
#      },
      
## coverage of unemployment and active labor market programs
#     {'name' : 'coverage_unemployment_almp',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/per_lm_alllm.cov_pop_tot?format=json&date=2015&per_page=300',
#      'long_name' : 'Coverage of unemployment benefits and active labor market programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Coverage of unemployment benefits and ALMP'
#      },
      
## adequacy of social safety net programs
#     {'name' : 'adequacy_social_safety_net',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/per_sa_allsa.adq_pop_tot?format=json&date=2015&per_page=300',
#      'long_name' : 'Adequacy of social safety net programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Adequacy of social safety net programs'
#      },
#      
## coverage of social safety net programs
#     {'name' : 'coverage_social_safety_net',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/per_sa_allsa.cov_pop_tot?format=json&date=2015&per_page=300',
#      'long_name' : 'Coverage of social safety net programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Coverage of social safety net programs'
#      },
      
## adequacy of social protection and labor programs
#     {'name' : 'adequacy_social_protection',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/per_allsp.adq_pop_tot?format=json&date=2015&per_page=300',
#      'long_name' : 'Adequacy of social protection and labor programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Adequacy of social protection and labor programs'
#      },

## coverage of social protection and labor programs
#     {'name' : 'coverage_social_protection',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/per_allsp.cov_pop_tot?format=json&date=2015&per_page=300',
#      'long_name' : 'Coverage of social protection and labor programs',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Coverage of social protection and labor programs'
#      },

# trade (% of GDP)
     {'name' : 'trade_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/NE.TRD.GNFS.ZS?format=json&date=2015&per_page=300',
      'long_name' : 'Trade, % of gross domestic product',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Trade, % of GDP'
      },
      
# Individuals using the Internet (% of population)
     {'name' : 'use_internet_pct_pop',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/IT.NET.USER.ZS?format=json&date=2015&per_page=300',
      'long_name' : 'Individuals using the Internet (% of population)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Internet users, & of population'
      },
     
# Mobile cellular subscriptions (per 100 people)
     {'name' : 'mobile_phone_subscriptions_pct_pop',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/IT.CEL.SETS.P2?format=json&date=2015&per_page=300',
      'long_name' : 'Mobile cellular subscriptions, % of population',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Mobile phone subscriptions, & of population'
      },
     
# Time required to start a business (days)
     {'name' : 'days_required_to_start_business',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/IC.REG.DURS?format=json&date=2015&per_page=300',
      'long_name' : 'Time required to start a business (days)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Time required to start a business (days)'
      },
   
# data mostly missing
## Firms with female participation in ownership (% of firms)
#     {'name' : 'firms_female_top_mgmt_pct',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/IC.FRM.FEMO.ZS?format=json&date=2015&per_page=300',
#      'long_name' : 'Firms with female participation in ownership (% of firms)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Firms with female participation in ownership (% of firms)'
#      },
     
# data mostly missing
## Informal payments to public officials (% of firms)
#     {'name' : 'informal_payments_to_officials_pct_firms',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/IC.FRM.CORR.ZS?format=json&date=2015&per_page=300',
#      'long_name' : 'Informal payments to public officials (% of firms)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Informal payments to public officials (% of firms)'
#      },
#      
## Bribery incidence (% of firms experiencing at least one bribe payment request)
#     {'name' : 'bribe_incidence_pct_firm',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/IC.FRM.BRIB.ZS?format=json&date=2015&per_page=300',
#      'long_name' : 'Bribery incidence (% of firms experiencing at least one bribe payment request)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Bribery incidence (% of firms experiencing at least one bribe payment request)'
#      },
      
# Ease of doing business index (1=most business-friendly regulations)
# ------------> # NOTE: data from 2018
     {'name' : 'ease_doing_business',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/IC.BUS.EASE.XQ?format=json&date=2018&per_page=300',
      'long_name' : 'Ease of doing business index (1=most business-friendly regulations)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Ease of doing business index (1=most business-friendly regulations)'
      },
      
# Tax revenue (% of GDP)
     {'name' : 'tax_revenue_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/GC.TAX.TOTL.GD.ZS?format=json&date=2015&per_page=300',
      'long_name' : 'Tax revenue (% of GDP)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Tax revenue (% of GDP)'
      },
      
# Net lending (+) / net borrowing (-) (% of GDP)
     {'name' : 'net_lending_borrowing_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/GC.NLD.TOTL.GD.ZS?format=json&date=2015&per_page=300',
      'long_name' : 'Net lending (+) / net borrowing (-) (% of GDP)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Net lending (+) / net borrowing (-) (% of GDP)'
      },

# Central government debt, total (% of GDP)
     {'name' : 'central_govt_debt_pct_gdp',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/GC.DOD.TOTL.GD.ZS?format=json&date=2015&per_page=300',
      'long_name' : 'Central government debt, total (% of GDP)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Central government debt, total (% of GDP)'
      },  

# all data missing      
# Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)
#     {'name' : 'account_ownership_pct_population_15_plus',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/FX.OWN.TOTL.ZS?format=json&date=2015&per_page=300',
#      'long_name' : 'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Account ownership at a financial institution or with a mobile-money-service provider (% of population ages 15+)'
#      }, 

# Risk premium on lending (lending rate minus treasury bill rate, %)
     {'name' : 'risk_premium',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/FR.INR.RISK?format=json&date=2015&per_page=300',
      'long_name' : 'Risk premium on lending (lending rate minus treasury bill rate, %)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Risk premium on lending'
      },
       
# Terrestrial and marine protected areas (% of total territorial area)
     # data are from 2016
     {'name' : 'biodiversity_protected_areas',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/ER.PTD.TOTL.ZS?format=json&date=2016&per_page=300',
      'long_name' : 'Terrestrial and marine protected areas (% of total territorial area)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Terrestrial and marine protected areas (% of total territorial area)'
      },
      
# Renewable internal freshwater resources per capita (cubic meters)
     {'name' : 'renewable_freshwater_per_capita',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/ER.H2O.INTR.PC?format=json&date=2014&per_page=300',
      'long_name' : 'Renewable internal freshwater resources per capita (cubic meters)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Renewable internal freshwater resources per capita (cubic meters)'
      },
      
## all data missing
## Level of water stress: freshwater withdrawal as a proportion of available freshwater resources
#     {'name' : 'frewshwater_stress',
#      'url' : 'http://api.worldbank.org/v2/country/all/indicator/ER.H2O.FWST.ZS?format=json&date=2015&per_page=300',
#      'long_name' : 'Level of water stress: freshwater withdrawal as a proportion of available freshwater resources',
#      'source' : 'World Bank, World Development Indicators',
#      'short_name' : 'Level of water stress: freshwater withdrawal as a proportion of available freshwater resources'
#      }, 

# Population living in slums (% of urban population)
# NOTE: data from 2014
     {'name' : 'slum_population_pct_urban_population',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/EN.POP.SLUM.UR.ZS?format=json&date=2014&per_page=300',
      'long_name' : 'Population living in slums (% of urban population)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Population living in slums (% of urban population)'
      }, 

# PM2.5 air pollution, population exposed to levels exceeding WHO guideline value (% of total)
     {'name' : 'pm25_pct_population',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/EN.ATM.PM25.MC.ZS?format=json&date=2015&per_page=300',
      'long_name' : 'PM2.5 air pollution, population exposed to levels exceeding WHO guideline value (% of total)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'PM2.5 air pollution exposure, % of population)'
      }, 

# Foreign direct investment, net (BoP, current US$
     {'name' : 'net_fdi',
      'url' : 'http://api.worldbank.org/v2/country/all/indicator/BN.KLT.DINV.CD?format=json&date=2015&per_page=300',
      'long_name' : 'Foreign direct investment, net (BoP, current US$)',
      'source' : 'World Bank, World Development Indicators',
      'short_name' : 'Net foreign direct investment)'
      } 
]

        for item in chart_data:
            chart = Chart()
            chart.name = item['name']
            chart.url = item['url']
            chart.longname = item['long_name']
            chart.source = "World Bank, World Development Indicators"
            chart.shortname = item['short_name']
            chart.save()

            response = requests.get(item['url'])
            data = json.loads(response.text)
            data = data[1] # list of data rows (dictionaries)
            print(f'Downloading {item["name"]}')
            for datum in data:
                country_name = datum['country']['value']
                country_code = datum['countryiso3code']
                country, created = Country.objects.get_or_create(name=country_name, code=country_code)

                data_row = DataRow()
                data_row.country = country
                data_row.value = datum['value']
                data_row.year = datum['date']
                data_row.indicator = datum['indicator']['id']
                data_row.name = datum['indicator']['value']
                data_row.varname = chart
                data_row.save()
