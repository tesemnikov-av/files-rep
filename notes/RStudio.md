

# rstudio-rep

ШПАРГАЛКА

https://r-analytics.blogspot.com/p/blog-page_06.html

| general  |   |   |   |   |
|---|---|---|---|---|
| rm(list=ls())  |clear variables   |   |   |   |
|  cat("\014") | clear console  |   |   |   |
|  cat("\f") | clear console  |   |   |   |
|   vector    |  b <- c(-45 , 4, 0, 11)    |   |   |   |
|     df  | df <- data.frame(rost=a, ves=b)     |   |   |   |
|       |      |   |   |   |
|       |      |   |   |   |
|       |      |   |   |   |




Справка

?plot help.search("тема")

clear env

rm(list=ls())

clear console

cat("\014")

subset(mydata, gender == 'female')

mean(a, na.rm=TRUE)

rbind cbind 


Select open file
f <- file.choose()

setwd('/Users/tesemnikov-av/RStudio_example')

getwd()

dir()

 mydata <- read.csv('data.csv')
 write.csv(df , "evals.csv")

a <- 5:30





b[1]

b[c(2, 3)]

 c[c>10]
 


 
 View(dara)

str(data)

names(data)

summary(data)

mean(mydata$score)

mydata$new <- mydata$score * 2

nrow(mydata)

ncol(mydata)

mydata[1 , 1]

mydata[,3]
md[1,]



library(help = "datasets" ) # список доступных датасетов; mydata <- mtcars

df$vs   <- factor( df$vs , labels = c( "V" , "S")  ) #  0 - V ; 1 - S

mean(df$mpg[df$cyl == 6])
mean(df$mpg[df$cyl == 6 & df$vs == "V"])

mtcars$even_gear <- as.numeric(mtcars$gear %% 2 == 0)

as.vector(AirPassengers)

mtcars$mpg[mtcars$cyl == 4]

mini_mtcars <- mtcars[c(3, 7, 10, 12, nrow(mtcars)), ]

nrow(mtcars)
ncol(mtcars)

#if Для переменной 

if (a > 0) {print('ok')} else {print('Not ok') ; print(a+1)}

#ifelse

Для вектора произвольной длинны
ifelse( a > 0 , 'yes' ,'no')

#for

for (i in 1:nrow(df)) print(df$age[i])

#for + if

for (i in 1:nrow(df)) { if ( df$cls_perc_eval[i] == '55.81395' ) { print(df[i,]) } }

for (i in 1:nrow(df)) { if ( df$score[i] >= 4 ) { df$quality[i] = 'good' } else { df$quality[i] = 'bad' }}

df$quality <- ifelse(df$score >= 4 , 'good', 'bad')


#создать пустой столбец

df$quality <- rep(NA, nrow(df))

Хи Квадрат
mice <-matrix(c(18,55,27,25,50,25),nrow = 2,byrow = TRUE);
chisq.test(mice)

students <- rbind(c(15,9), c(11,6)) 
chisq.test(students)


>#воссоздадим таблицу
>patients <- rbind(c(18, 7), c(6, 13))
>#подпишем строки и столбцы
>colnames(patients) <- c("Yes", "No")
>rownames(patients) <- c("Placebo", "Aspirin")
>#вот график, который нам нужен
>mosaicplot(patients, color=T, shade=T, ylab="Thrombosis", xlab="Group")
>#а вот так можно в точности воспроизвести рисунок, который мы видели
>mosaicplot(patients, color=T, shade=T, ylab="Thrombosis", xlab="Group", cex.axis=1, main="")





air <- as.vector(AirPassengers)
good_months <- vector(mode="numeric", length=0)
for (i in 1:length(air)) {  if ( air[i] < air[i+1] & i != length(air) ) { good_months <- append(good_months , air[i+1] , length(good_months)  )  } }


air <- as.vector(AirPassengers)
moving_average <-  vector(mode="numeric", length=0)
for (i in 1:(length(air)-9)) {  moving_average <- append( moving_average , ( mean(AirPassengers[i:(i+9)]) ) , length(moving_average)) }

aggregate( x = df$hp , by = list(df$vs), FUN = mean )
 colnames(agg_hp_cyl) <- c("hp" , "mean cyl")
 
 aggregate(hp ~ vs , df , mean )
 aggregate(hp ~ vs + am, df , mean )

aggregate(x=df[,-c(8,9)] , by = list(df$am) , FUN = sd )
aggregate(cbind(df$mpg, df$disp) , by = list(df$am, df$vs) , FUN = sd )

При помощи функции aggregate рассчитайте стандартное отклонение переменной hp (лошадиные силы) и переменной disp (вместимости двигателя)  у машин с автоматической и ручной коробкой передач. aggregate( cbind(df$hp, df$disp) , by = list(df$am) , FUN = sd )

Описательные статистики для дата фрейма
describe(df)
describeBy(df[,-c(8,9)] , group = df$vs , mat = T , digits = 1  )

sum(is.na(df))
mean(df , na.rm = T)

replace(my_vector , is.na(my_vector), mean(my_vector, na.rm = TRUE))


Графики

|hist |boxplot |plot |
|---|--- |--- |
| Гистограмма частот - один вектор - одна переменная| Распределение признака(mpg) по группам(am)| Взаимосвязь двух признаков |
|  hist(mtcars$mpg , breaks = 20) |boxplot(mpg ~ am , mtcars) | plot(mtcars$mpg , mtcars$hp)|


|hist | dotplot |density - кривая плотности |
|---|---|---|
|ggplot(mtcars, aes(x = mtcars$mpg)) + geom_histogram( fill = 'white' , col = 'black' , binwidth = 1 ) |ggplot(mtcars, aes(x = mtcars$mpg)) + geom_dotplot() | ggplot(mtcars, aes(x = mtcars$mpg)) + geom_density()|
