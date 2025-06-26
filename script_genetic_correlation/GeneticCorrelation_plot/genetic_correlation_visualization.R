# Genetic correlation plot

rm(list=ls())
library(data.table)
library(dplyr)
library(readxl)
library(corrplot)
 
#read the genetic correlation result data
rg_data <- read_excel("correlation_result.xlsx", sheet=3)
names <-  unlist(rg_data[, 1])
dim(rg_data)
rg_data <- rg_data  %>% mutate_all(~replace(., . == "NA", 0))
rg_data<- rg_data %>% dplyr::select(-Trait)

#get the data matrix and name the columns and rows
mydata <- as.data.frame(rg_data[1:9, 1:9])
rownames(mydata) <- names
mydata <- as.data.frame(lapply(mydata, function(x) as.numeric(x)))
colnames(mydata)<-  names
rownames(mydata)<-  names

#reorder the rg data by the distances of clusters
reorder_cormat <- function(cormat) {
  dd <- as.dist((1 - cormat) / 2)
  hc <- hclust(dd)
  cormat[hc$order, hc$order]
}

reordered_corr_matrix <- reorder_cormat(mydata)

numeric_matrix <- do.call(rbind, lapply(reordered_corr_matrix, function(x) unlist(x)))
colnames(numeric_matrix)<-  unlist(rownames(reordered_corr_matrix))
str(numeric_matrix)

png(file="genetic_correlation.png",width=12,height=8,units="cm",res=300)
corrplot(numeric_matrix ,type="upper", method = "circle")
dev.off()

pdf(file="genetic_correlation.pdf",width=12,height=8 )
corrplot(numeric_matrix , type="upper", method = "circle")
dev.off()


