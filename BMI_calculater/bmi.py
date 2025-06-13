def valid_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if value < min_val or value > max_val:
                print(f"Please enter a value between {min_val} and {max_val}.")
            else:
                return value 
        except ValueError:
            print("Invalid input. Please input number")


def cal_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 1)

def categorize_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi <29.9:
        return "overweight"
    else:
        return "Obesity"
    

def main():
    print("Welcome to BMI Calculator:")
    weight = valid_input("Enter weight in K.G.:",  10, 300)
    height = valid_input("Enter Height in meters:", 0.5, 2.5)

    bmi = cal_bmi(weight, height)
    category = categorize_bmi(bmi)

    print(f"Your bmi is {bmi}")
    print(f"You are categorized as: {category}")

if __name__ == "__main__":
    main()