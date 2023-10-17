import math
import statistics
print("HOW MANY GOD DAMN BROWNIES WILL TI TAKE TO GET TO YOUR DREAM WEIGHT ? WELL MY FRIEND, LET US FIND OUT WITH THIS WODNERFUL CALCULATOR THAT I MADE. WOOHOO!!")
# Function to calculate BFP
def calculate_bfp(waist, neck, height):
    BFP = 495 / (1.0324 - 0.19077 * math.log10(waist - neck) + 0.15456 * math.log10(height)) - 450
    return BFP

# Function to calculate BMR for men
def calculate_bmr_for_men(weight, height, age):
    BMR = 13.397 * weight + 4.799 * height - 5.677 * age + 88.362
    return BMR

# Function to calculate BMR for women
def calculate_bmr_for_women(weight, height, age):
    BMR = 9.247 * weight + 3.098 * height - 4.330 * age + 447.593
    return BMR

def cal_needed (bfp, weight, goal_weight):
    if goal_weight > weight:
     cal_needed = {[bfp/100]*(goal_weight)-[bfp/100]*(weight)}*7700
    elif goal_weight < weight:
     cal_needed = {[bfp/100](weight)-(goal_weight)}*7700
    elif goal_weight == weight:
     cal_needed = 0 

def calculate_calplusmin (bmr, calorie):
    if bmr>calorie:
        calplusmin = calorie-bmr
    elif calorie<bmr:
        calplusmin = bmr-calorie 

def calculate_weightplusmin(weight, goal_weight,deficit):
    if weight > goal_weight:
        weight_loss=abs(weight-goal_weight)*7700/deficit
        print(weight_loss)
    elif weight < goal_weight:
        weight_gain=abs(goal_weight-weight)


def calculate_brownies_needed(weight, goal_weight, bmr, bfp):
    calorie_needed = weight-goal_weight 

while True:
    try:
        # Initialize variables to store BMR and BFP
        bmr = None
        bfp = None

        # Prompt the user to select gender
        gender = int(input("Enter your gender (1 for male, 2 for female): "))

        while gender not in (1, 2):
            print("Invalid input. Please enter 1 for male or 2 for female.")
            gender = int(input("Enter your gender (1 for male, 2 for female): "))

        calorie=float(input("You want to eat. If you want to eat as much as humanly possible, enter 1"))
        
        while calorie <=0:
            print("Invalid measurement. Weight should be greater than 0")
            calorie=float(input("re-enter your goal weight"))

        goal_weight=float(input("enter your goal weight"))

        while goal_weight<=0:
            print("Invalid amount, weight should be greater than 0")
            goal_weight=float(input("re-enter your goal weight"))
            

        weight = float(input("Enter your weight in kg: "))
        
        while weight <= 0:
            print("Invalid measurement. Weight should be greater than zero.")
            weight = float(input("Enter your weight in kg: "))

        height = float(input("Enter your height in cm: "))

        while height <= 0:
            print("Invalid measurement. Height should be greater than zero.")
            height = float(input("Enter your height in cm: "))
        age = int(input("Enter your age: "))

        while age <= 0:
            print("Invalid measurement. Age should be greater than zero.")
            age = int(input("Enter your age: "))

    

        if gender == 1:
            print("--------")
            print("Measurements for your waist and neck should be non zero. The difference of the measurements should be non zero and non negative numbers")
            waist = float(input("Enter your waist measurement in cm: "))
            neck = float(input("Enter your neck measurement in cm: "))

            while waist <= 0 or neck <= 0:
                print("Invalid measurements. Waist and neck should be greater than zero.")

                waist = float(input("Enter your waist measurement in cm: "))
                neck = float(input("Enter your neck measurement in cm: "))

            while waist < neck:
                print(f"Your neck is not bigger than your waist... Your input ({waist}) for waist and ({neck}) for neck is not physically possible..")
                waist = float(input("Enter your waist measurement in cm: "))
                neck = float(input("Enter your neck measurement in cm: "))

            while waist == neck:
                print(f"Your neck is not the size of your waist... Your input {waist} for waist and {neck} for neck is not physically possible..")
                waist = float(input("Enter your waist measurement in cm: "))
                neck = float(input("Enter your neck measurement in cm: "))

            bmr = calculate_bmr_for_men(weight, height, age)
            bfp = calculate_bfp(waist, neck, height)

        elif gender == 2:
            print("--------")
            print("Measurements for your waist and neck should be non zero. The difference of the measurements should be non zero and non negative numbers")
            waist = float(input("Enter your waist measurement in cm: "))
            neck = float(input("Enter your neck measurement in cm: "))

            while waist <= 0 or neck <= 0:
                print("Invalid measurements. Waist and neck should be greater than zero.")

                waist = float(input("Enter your waist measurement in cm: "))
                neck = float(input("Enter your neck measurement in cm: "))

            while waist < neck:
                print(f"Your neck is not bigger than your waist... Your input ({waist}) for waist and ({neck}) for neck is not physically possible..")
                waist = float(input("Enter your waist measurement in cm: "))
                neck = float(input("Enter your neck measurement in cm: "))

            while waist == neck:
                print(f"Your neck is not the size of your waist... Your input {waist} for waist and {neck} for neck is not physically possible..")
                waist = float(input("Enter your waist measurement in cm: "))
                neck = float(input("Enter your neck measurement in cm: "))

            bmr = calculate_bmr_for_men(weight, height, age)
            bfp = calculate_bfp(waist, neck, height)
        # Check if BMR and BFP have been calculated and print or use them as needed

        if bmr is not None:
            print(f"Your BMR is {bmr:.2f} calories per day.")
        if bfp is not None:
            print(f"Your Body Fat Percentage (BFP) is {bfp:.2f}%.")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

    repeat = input("Do you want to calculate again? (y or n): ")
    if repeat.lower() != 'y':
        break
    if repeat.lower() != 'Y':
        break
    if repeat.lower() != 'yes':
        break