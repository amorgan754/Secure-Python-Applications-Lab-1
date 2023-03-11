"""this code is to determine voting elgibility"""
CONTINUE = True
ELIGIBLE = True

print("Welcome to the voter registration!")
print("This will determine if you are eligible for voting")
print()

#ask user for age and country of citizenship then first name, last name,
# state of residence, zipcode if elgible
while CONTINUE is True:
    age = int(input("In whole numbers, how old are you?:\n"))
    if 18 <= age >= 90:
        CONTINUE = True
        ELIGIBLE = True
        VALID = True
    elif 17 >= age <= 91:
        print("Sorry, you are not eligible to vote.")
        CONTINUE = False
        ELIGIBLE = False
        break
    country = input("Using two letters, what is your country of citizenship?:\n")
    if country.lower() == "us":
        CONTINUE = True
        ELIGIBLE = True
        VALID = True
    elif country.lower() != "us":
        print("Sorry, you are not eligible to vote.")
        CONTINUE = False
        ELIGIBLE = False
        break
    continue_on = input("Do you wish to continue at this point?:\n")
    if continue_on.lower() == "yes":
        CONTINUE = True
    elif continue_on.lower() != "yes":
        print("Thank you, have a good day")
        CONTINUE = False
        VALID = False
        break
    first_name = input("What is your first name?:\n")
    last_name = input("What is your last name?:\n")
    continue_on = input("Do you wish to continue at this point?:\n")
    if continue_on.lower() == "yes":
        CONTINUE = True
    elif continue_on != "yes":
        print("Thank you, have a good day")
        CONTINUE = False
        VALID = False
        break
    state = input("Using two letters, what is your state of residence?:\n")
    if len(state) == 2:
        CONTINUE = True
    zipcode = input("What is the zip code you are voting from?:\n")
    if len(zipcode) == 5:
        CONTINUE = True
    CONTINUE = False

#if cant move forward not presented with remaining questions

#display information
if ELIGIBLE is True and VALID is True:
    print("Thank you for the information!\nOn file we now have: ")
    print("Name (last, first):\t" + last_name + ", " + first_name)
    print("Age:\t", age)
    print("Citizenship:\t" + country)
    print("State of residence:\t" + state)
    print("Zipcode:\t" + zipcode)
    print("Have a great day")
elif ELIGIBLE is True and CONTINUE is False and VALID is False:
    print("Come back at any time")
else:
    print("Have a good day")
