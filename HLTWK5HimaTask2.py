import altair as alt
import pandas as pd
from pandas.core.frame import DataFrame

covid19data = pd.read_csv("covid19_sg.csv")
print(covid19data)

d = {'Date' : ['23/01/2020', '24/01/2020', '25/01/2020'],
     'Daily Conform' : [1,2,1],
     'Cumulative Confirmed' : [1,3,4]}
df = DataFrame(d)
print(df)