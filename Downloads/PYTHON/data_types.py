# #Data Type

# # String
# print("Hello"[4])
# print("123" + "456")

# # Integars
# print(123 + 456)

# #Float
# float = print(3.0 +  4.2)

# # Boolean
# True & False

# USE TYPE FUNCTION TO KNOW DATA TYPE
# e.g 
# a= float(123)
# print(type(a)) 

# # Convert Integar to string
# num_char = len(input("what is your name:\n"))
# new_num_char = str(num_char)
# print( "your name has " + new_num_char + " characters.")


# # Mathematical operations PEMDASLR


# BMI Calculator

# height = input("enter your height in m:\n")
# weight = input("enter your weight in kg:\n ")
# meters = input("enter meters in ...:\n")

# bmi = print( int(weight) / float(height) ** 2)

# bmi_as_int = int(bmi)
# print(bmi_as_int)

# # Manipulation and floating numbers
# print(round(5/2, 2))
# #   floor division5

# print(8 // 3) 

# f-String
# score =0
# height= 1.8
# isWinning=True
# print(f"your score is {score},your height is {height}, and you are {isWinning}")

#Age calculator
# age_rem = input("what is your current age:\n")
# # years_rem = input('')


# age_as_int = int(age_rem)
# years_rem = 90 - age_as_int
# days_rem  = years_rem * 365
# weeks_rem = years_rem * 52
# months_rem = years_rem * 365
# print(f"your have  {days_rem} days, {weeks_rem} weeks, and {months_rem} left")

# Tip Calculator
print("Welcome to tip calculator")
bill= float(input("What is your total bill? $:"))
tip= float(input("what percentage of tip would you like to give? 10, 12, or 15?"))
people= int(input("How many people to split the bill?"))
bill_with_tip = tip/100 * bill
print(bill_with_tip)
# final_amount = round(bill_with_tip, 2)
#Implement float to string below
final_amount = "{:.2f}".format(bill_with_tip)     
print(f"Each person should pay: ${final_amount}")