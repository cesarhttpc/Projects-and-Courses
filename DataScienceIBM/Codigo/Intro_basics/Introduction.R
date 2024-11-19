cars <- c(5,4,6,2,3)

plot(cars, type = "o")
title(main = "Cars vs Index")

library(ggplot2)
ggplot(mtcars, aes(x = mpg, y= wt)) + geom_point() + ggtitle("Miles per gallon vs weight") + labs(y = "weight", x = 'Miles per gallon')


# make vs a factor
mtcars$vs <- as.factor(mtcars$vs)
# create boxplot of the distribution for v-shaped and straight Engine
ggplot(aes(x = vs, y = mpg), data = mtcars) + geom_boxplot()

ggplot(aes(x = vs, y = mpg, fill = vs), data = mtcars) +
    geom_boxplot(alpha = 0.3) +
    theme(legend.position = "none")

ggplot(aes(x = wt), data = mtcars) +
    geom_histogram(binwidth = 0.5)

