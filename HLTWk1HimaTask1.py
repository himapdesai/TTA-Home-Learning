import random
random_number= random.randint(1, 10) 
user_name = input ("Your name : ")
guess_number = int(input ("Guess the number between 1 to 10: "))
if guess_number == random_number :
    print("You have guessed corretly.")
else:
    print("You have gissed wrong number....")