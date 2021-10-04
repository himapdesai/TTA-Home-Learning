BikePrice = 2000.0
condition = True
year = 1
while condition:
    BikePrice = BikePrice - (BikePrice * (10/100))

    if BikePrice > 1000.0:
        print("New Price in Year : " + str(year))
        print(BikePrice)
        year = year + 1
    else :
        condition = False
        print("Final Price in Year: " + str(year))
        print(BikePrice)
        year = year + 1

    
