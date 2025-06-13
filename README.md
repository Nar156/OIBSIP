Objective: This project is a simple command-line based BMI Calculator built using Python. It helps users determine their Body Mass Index (BMI) based on their weight and height, and then classifies them into standard health categories such as Underweight, Normal Weight, Overweight, or Obesity.

Tools & Libraries Used - Python

Steps Performed: 1)Input Validation: Ensures the user enters reasonable numeric values for weight and height using the valid_input() function. Weight must be between 10–300 kg. Height must be between 0.5–2.5 meters.

2)BMI Calculation:

BMI is calculated using the formula: BMI = weight (kg) / [height (m)]2​

3)BMI Categorization:

Categorizes the BMI into: Underweight: BMI < 18.5 Normal Weight: 18.5 ≤ BMI < 24.9 Overweight: 25 ≤ BMI < 29.9 Obesity: BMI ≥ 30

4)Display Output Displays the calculated BMI value and its corresponding category.

Outcome: Accepts user inputs interactively and safely. Computes BMI and provides health classification. Helps users become aware of their weight category. Example Output:

Welcome to BMI Calculator: Enter weight in K.G.: 70 Enter Height in meters: 1.75 Your bmi is 22.9 You are categorized as: Normal Weight
