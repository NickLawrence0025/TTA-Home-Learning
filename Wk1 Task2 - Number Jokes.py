#Tells user a joke based on their number choice

from time import sleep

number = int(input("Pick a number between 1 and 100: "))
print ("Your joke is....")

if number == 6:
    print("Why was 6 afraid of 7?")
    sleep(3)
    print("Because 7 eight 9")
elif number == 9:
    print("Why 7 ate 9...")
    sleep(3)
    print("Because he needed 3 square meals a day")
elif number == 10:
    print("What are 10 things we can always count on?")
    sleep(3)
    print("Our fingers!")
else:
    answer = input("Still thinking of a joke for that number")
          

    
