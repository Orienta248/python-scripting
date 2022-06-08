user_no = input("Enter a number :")


 # validation
try:
    #runs if input is valid
    user_no = int(user_no)
    print ("Hurray you entered a number")

    if user_no >= 0:
        print(True)

    else:
        print("Do as you are told")

except:
   #runs if input is invalid
    print('This is not a number')