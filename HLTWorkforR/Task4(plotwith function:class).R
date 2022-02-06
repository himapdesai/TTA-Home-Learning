
install.packages("dplyr")
install.packages("dslabs")
install.packages("ggplot2")
library(ggplot2)
library(dslabs)
data(murders)
class(murders)
ggplot(data = murders)
str(murders)
murders$population

# murders %>% gglpot(data = murders) + geom_point(aes(x = population/10^6, y = total))
p <- ggplot(data = murders)
p + geom_point(aes(x = population/10^6, y = total))


# print(p)





