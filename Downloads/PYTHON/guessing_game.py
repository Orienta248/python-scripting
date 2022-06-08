# Store the number guess
our_fav_number = 7

#ourFavNumber

#take user number
user_guess = input("Enter user guess: ")
type_of_user_guess = type(user_guess) #str


print(user_guess)

user_guess = int(user_guess)

print(type(user_guess))

if user_guess == our_fav_number:
    print("Success,you guessed the number! Our favorite number is:" + str(our_fav_number))
    
if user_guess < our_fav_number:
    print("Nah,you guessed a low number! Try another number" )

if user_guess > our_fav_number:
    print("Nah,you guessed a high number! Try another number" )