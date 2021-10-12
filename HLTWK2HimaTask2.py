
def moter_bike(bikeprice, condition, year):
    while condition:
        bikeprice = bikeprice - (bikeprice * (10/100))

    if bikeprice > 1000.0:
        print("New Price in Year : " + str(year))
        print(bikeprice)
        year = year + 1
    else:
        condition = False
        print("Final Price in Year: " + str(year))
        print(bikeprice)
        year = year + 1

moter_bike(2000.0,True,1)