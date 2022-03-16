import random
from time import sleep

my_name= input("Hello! What is your name?")
number = random.randint(1, 10)
print("Well, " + my_name +"I am thinking of a number between 1 and 10.")
guess = int(input("Take a guess:"))
print("Were you correct?...")
sleep(3)
if guess == number:
    print("Good job,", my_name + "! You guessed my number")
else:
    print("Wrong, better luck next time. I was thinking of the number ", + number)


