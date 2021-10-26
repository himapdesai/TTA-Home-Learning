import pandas as pd
holidaydata = pd.read_csv("holiday_data.csv")
print(holidaydata)

print("How many rows and columns in your file?  ")
df = pd.DataFrame(holidaydata, index=None)
rows = len(df.axes[0])
cols = len(df.axes[1])

print(df)
print("Number of Rows: ", rows)
print("Number of Columns: ", cols)


print("Print row 3-8 using iloc/loc :  ")
print(df.iloc[3:8])


print("Print mean of all-inclusive hotels :  ")
print(df["All-inclusive hotels"].mean())


print("Print lower scoring destination :  ")
print(df["Feedback Score"].min())


print("Print highest scoring destination :  ")
print(df["Feedback Score"].max())




top_city_filter = (holidaydata["All-inclusive hotels"] > 9)
filter = holidaydata[top_city_filter]
print(filter)


print ("Filter the data by score above 8 :  ")
top_score_filter = (holidaydata["Feedback Score"] > 8)
filter = holidaydata[top_score_filter]
print(filter)



print ("Filter the data score below :   ")

low_score_filter = (holidaydata["Feedback Score"] < 2)
filter = holidaydata[low_score_filter]
print(filter)

