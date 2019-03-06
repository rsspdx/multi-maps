setwd("~/data/geo/multi-maps")

happiness <- read.csv("happiness-cantril-ladder.csv", stringsAsFactors = FALSE)
happiness.2015 <- happiness[happiness$Year == 2015,]
names(happiness.2015) <- c("country", "country.code", "year", "happiness")
head(happiness.2015)
unhcr.country.to.iso3 <- read.csv("unhcr-country-to-iso3.csv", stringsAsFactors = FALSE)
happiness.2015 <- merge(unhcr.country.to.iso3, happiness.2015, by = "country.code", all.x=TRUE)
head(happiness.2015)
write.csv(happiness.2015, file="happiness.2015.csv")

