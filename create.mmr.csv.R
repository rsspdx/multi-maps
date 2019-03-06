setwd("~/data/geo/multi-maps")

mmr <- read.csv("API_SH.STA.MMRT_DS2_en_csv_v2_10319249.csv", skip=3, stringsAsFactors = FALSE)
mmr.2015 <- as.data.frame(cbind(mmr$Country.Name, mmr$Country.Code, mmr$X2015), stringsAsFactors = FALSE)
names(mmr.2015) <- c('country', 'country.code', 'mmr')
write.csv(mmr.2015, file="mmr.2015.csv")