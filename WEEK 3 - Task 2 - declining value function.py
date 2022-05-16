# define a function that takes motorcycle value and percentage as parameters
import datetime

def declining_value(value,percentage):
    date = datetime.date.today()
    year = int(date.strftime("%Y"))
    percentage = percentage/100
    while value >= 1000:
        format_value = "{:.2f}".format(value)
        print (str(year) + " - £" + format_value)
        value *= 1-percentage
        year += 1
           
        
# Procedure that asks for an input from the user, and returns yearly amounts
     
value = int(input("What is the motorcycle worth? "))
percentage = float(input("By what percentage does it decline in value each year? "))
amount = declining_value(value,percentage)

        

        

    
    
