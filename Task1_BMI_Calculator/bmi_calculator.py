print("-- BMI CALCULATOR -- ")

def calculate_bmi(weight,height):
    bmi = weight/(height**2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "You are Underweight"
    elif 18.5 <= bmi < 25:
        return "Your weight is Normal"
    elif 25 <= bmi < 30:
        return "You are Overweight"
    else:
        return "Obese"

def main():
    try:
     weight=float(input("Enter your weight in kgs:"))
     height=float(input("Enter your height in meters:"))

     if weight<=0 and height<=0:
        print("--Height and Weight must be positive--")
        return

     bmi = calculate_bmi(weight,height)
    

     print(f"Your BMI is :{bmi:.2f}")
     print(f"Category:{get_bmi_category(bmi)}")

    except ValueError:
     print("Please enter valid numeric values!!!")



main()