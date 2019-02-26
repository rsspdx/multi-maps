setwd('~/data/geo/multi-maps/data')
library(ggplot2)
mmr = read.csv('maternal_mortality_rate.csv')
gdpcap = read.csv('gdp_per_capita.csv')
df = merge(mmr, gdpcap)
df = df[complete.cases(df), ]
model = loess(maternal_mortality_rate ~ gdp_per_capita, data=df)
str(model)
df$resid <- model$residuals
df


g <- ggplot(df, aes(gdp_per_capita, maternal_mortality_rate)) +
      geom_smooth() +
      geom_point() +
      ggtitle("Maternal Mortality Rate vs. GDP per Capita, 2015 ") +
      xlab("GDP per Capita, Current $US") + 
      ylab("Maternal Mortality Rate (deaths per 100,000 live births") +
      theme(plot.title = element_text(hjust = 0.5))

g
