starter = input("Enter your Starter please! ")
cond1 = False
while cond1 == False:
    if starter == "":
        print("You missed it try again. ")
        starter = input("Enter your Starter please! ")
    else:
        cond1 = True

maincourse = input("Enter your Maincourse: ")
cond2 = False
while cond2 == False:
    if maincourse == "":
        print("Sorry enter your item please: ")
        maincourse = input("Enter your Maincourse: ")
    else:
        cond2 = True

dessert = input("Enter your Dessert: ")
cond3 = False
while cond3 == False:
    if dessert == "":
        print("sorry enter your choice please: ")
        dessert = input("Enter your Dessert: ")
    else:
        cond3 == True
        break

print(f"List of your meal {starter} , {maincourse} , {dessert} enjoy! ")
