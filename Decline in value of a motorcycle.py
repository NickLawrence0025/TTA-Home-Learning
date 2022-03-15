#Shows the decline in value of a motorcycle
print("Yearly reduction of motorcycles value")
#1.Set parameters
motorcycle = 2000
year = 2022
number_of_years = 0

#2.Perform calculation
while motorcycle >  1000:
    motorcycle = (motorcycle - motorcycle*0.1)
    year += 1
    number_of_years += 1
    format_motorcycle = "{:.2f}".format(motorcycle)
    print ("In", str(year) + " the motorcycle is worth £" + format_motorcycle)
print("This motorcycle will be worth less than £1000 in " + str(number_of_years) + " years time.")
      
    

