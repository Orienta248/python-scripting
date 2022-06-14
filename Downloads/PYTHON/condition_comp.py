# control flows if/else and comparison operator and logical operators
from re import L


print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?\n"))

if height >= 120:
    print("You can ride the rollercoaster! ")
    age = int(input("what is your age?"))
if age < 12:
    bill = 5
        print("child tickets are $5.")
elif age <= 18:
    bill = 7
        print("Youth tickets are $7.")
elif age >= 45 and age <= 55:
    print("Print everything is going to be OK.")
else:
    bill = 12
    print("Adult ticket are $12.")
    # if age <= 18:
    #     print("Please pay $7.")
    # else:
    #     print("please pay $12.")
# else:
#     print("Sorry, you have to grow taller before you ride.")


    # BMI CALCULATOR using if/elif/else
height = float(input("enter your height in m:\n"))
weight = float(input("enter your weight in kg:\n "))
bmi = weight/height ** 2
if bmi <= 18.5:
    print(f"Your bmi is {bmi} and you are underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")


year = int(input("which year do you want to check?"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
          
            print("Leap year.")
        elif:
            print("Not leap year.")
        elif:
            print("leap year.")
            else:
            print("Not a leap year.")
                
                
    # Pizza order app using multiple IF Statement.
    print("Welcome to PizzaHut")
    size=input("whats size of pizza do you want? S, M, or L")
    add_pepperoni=input("Do oyu want pepperoni? Y or N")
    extra_cheese=input("Do oyu want extra cheese Y or N")
    
    bill = 0
    
    if size == "S":
        bill += 15
    elif size == "M":
        bill += 20
    else:
        bill += 25
        
    if add_pepperoni == "Y":
        if size =="S":
            bill += 2
        else:
            bill += 3
    if extra_cheese =="Y":
        bill += 1
        
    print("Your bill is ${bill}")
    
    # Love calculator
    print("Welcome to the love Calculator")
    name1 = input("What is your name?\n")
    name2 = input("what is their name?\n")
    
    combined_string = name1 + name2
    lower_case_string = combined_string.lower()
    
    t = lower_case_string.count("t")
    r = lower_case_string.count("r")
    u = lower_case_string.count("u")
    e = lower_case_string.count("e")
    
    true = t + r + u + e
    
    l = lower_case_string.count("l")
    o = lower_case_string.count("o")
    v = lower_case_string.count("v")
    e = lower_case_string.count("e")
    
    love = l + o + v + e
    
    love_score = str(true) + str(love)
    print(love_score)
    
    
        
    