import random
import string

print("--Random Password Generator--")
def generate_password(length,characters):
    password =""

    for _ in range (length):
       password += random.choice(characters)

    return password

def get_user_preferences():
    try:
        length =int(input("Enter the passsword length:"))

        if length<= 0:
            print("Password length must be greater than 0")
            return None,None
        
        characters=""
        
        if input("Include Letters?(y/n):").lower() == "y":
            characters+=string.ascii_letters
        
        if input("Include Digits?(y/n):").lower() == "y":
            characters+=string.digits

        if input("Include Symbols?(y/n):").lower() == "y":
            characters+=string.punctuation

        if characters=="":
            print("You must select atleast one character type")
            return None,None
        
        return length,characters
    
    except ValueError:
        print("Please enter a valid number")
        return None,None

length,characters = get_user_preferences()

if length and characters:
    password = generate_password(length,characters)
    print(f"Generated Password:{password}")



    

