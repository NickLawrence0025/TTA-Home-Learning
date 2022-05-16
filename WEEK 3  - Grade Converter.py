def grade_converter(score):
    if score >= 90:
        return "A"
    elif score>= 80:
        return "B"
    elif score >= 70 :
        return "C"
    elif score >= 65 :
        return "D"
    else: 
        return "F"
    
grades = ["A","B","C","D","F"]

score = int(input("What is your score? "))
letter = grade_converter(score)
print("You achieved a grade " + str(letter))
predicted_grade = input("What is your predicted grade? ")

ind1 = (grades.index(predicted_grade))
ind2 = (grades.index(letter))

def grade_comparison(ind1,ind2):
    if ind2 > ind1:
        print("You achieved " + str(ind2-ind1) + " grades lower than predicted")
    elif ind2 == ind1:
        print("You achieved your predicted grade")
    else:
        print("You achieved " + str(ind1-ind2) + " grades higher than predicted")
        
grade_comparison(ind1,ind2)









