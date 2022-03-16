# A programme that outputs a users favourite meal combination

starter = input("What is your favourite starter?")
starter = starter.capitalize()
main_meal = input("What is your favourite main meal?")
main_meal = main_meal.lower()
dessert = input("What is your favourite dessert?")
dessert = dessert.lower()
drink = input("What would you like to drink?")
drink = drink.lower()


print("Your favourite meal is: ", starter + " to start, followed by ", main_meal +  " and ", dessert + " to finish. Your drink of choice is", drink + ". Enjoy!")



