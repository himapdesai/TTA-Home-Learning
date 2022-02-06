marks = c(70,95,80,74,85)
barplot(marks, main = "Comparing marks of 5 subjects", 
        xlab = "Marks", 
        ylab = "Subject",
        names.arg = c("English","Math","Science","History","Drowing"),
        col = "darkred",
        horiz = FALSE)
