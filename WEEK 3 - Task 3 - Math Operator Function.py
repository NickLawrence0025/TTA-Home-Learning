#Create a calculator function that is determined by user input


def calculation(first,second):
    if operator == "A":
        print(first + second)
    elif operator == "B":
        print(first - second)
    elif operator == "C":
        print(first * second)
    elif operator == "D":
        print(first / second)
    elif operator == "E":
        print(first ** second)
    elif operator == "M":
        print(first % second)
    elif operator == "F":
        print(first // second)
    elif operator == 'X':
        start = False 
    else:
        print("Invalid Entry")
        

#Multiple choice math operator

first = int(input("What is your first number?: "))
second = int(input("What is your second number?: "))
operator = input("Select: \n [A] Add \n [B] Subtract \n [C] Multiply \n [D] Divide \n [E] Square \n [M] Modulo \n [F] Floor Division \n [X] Exit \n Choose your operator: " )
operator = operator.upper()
calculation(first,second)
