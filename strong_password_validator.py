#Validate password strenght.
import re

#Create regex for strong password.
passRegex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]){8,}$')

#Create a function to validate for password strenght.
def validate_password(int):

    validate = passRegex.search(password)
    if validate == None:
        return "Not a valid password!\nPlease Try another password."
    else:
        return validate.group() + " is a strong password"


while True:
    password = input('Please enter password: ')
    print(validate_password(password))
