# Question3(i)
# enter the year of birth of the user
age = int(input("Year of Birth: "))
#check if tthe user is 18 years and above for the year of birth given and prints the ouput
if age >= 18:
    print("You are eligible to Vote")
else:
    print("You are not yet eligible")


# question 3(ii)
def classify_student(Score):
    #Check the students score and returns the correspnding grades
   
    if Score >= 75:
        return "Distiction"
    elif Score >= 65 < 75:
        return "Credit"

    elif Score >= 50 < 65:
        return "Pass"

    elif Score < 50:
        return "Fail"


# quetion3(iii)
result = classify_student(70)
print(result)


# Question 3(iv)
def classify_student(Score):
#     # Check if input is a  valid number
 if not isinstance(Score, (int, float)):
     return "Invalid Input"
 
 if Score >= 75:
        return "Distiction"
 elif Score >= 65 < 75:
        return "Credit"

 elif Score >= 50 < 65:
        return "Pass"

 elif Score < 50:
        return "Fail"
 

#if the input is not a valid number
print(classify_student("Ninety"))



#If input is a valid score
print(classify_student(60))



