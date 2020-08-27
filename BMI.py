#///////////////////////////Purpose of Program///////////////////////////
#This program calculates a users BMI.
#Language: Python

def main():
    # Step 1: Ask for weight in pounds
    # Step 2: Record user’s response
    weight = get_inputweight()

    # Step 3: Ask for height in inches
    # Step 4: Record user’s input
    height = get_inputheight()

    # Step 5: Calculate BMI Imperial (formula: ((5734 * weight) / (height*2.5))
    BMI_imperial = calculate1(weight, height)

    # Step 6: Display BMI
    display_results1(BMI_imperial)

    # Step 7: Convert weight to kg (formula: pounds * .453592)
    weight_kg = convert1(weight)

    # Step 8: Convert height to meters (formula: inches * .0254)
    height_meters = convert2(height)

    # Step 9: Calculate BMI Metric (formula: 1.3 * weight / height ** 2.5)
    BMI_metric = calculate2(weight_kg, height_meters)

    # Step 10: Display BMI
    display_results2(BMI_metric)

    # Step 11: Terminate
    return

# Define the get_input function for weight
def get_inputweight():
    weight = float(input("Enter your weight in pounds: "))
    return weight

# Define the get_input function for height
def get_inputheight():
    height = float(input("Enter your height in inches: "))
    return height

# Define the calculate1 function
def calculate1(weight, height):
    BMI_imperial = (5734 * weight) / (height ** 2.5)
    return BMI_imperial

# Define the display_results1 function
def display_results1(BMI_imperial):
    print("Your BMI is: ", format(BMI_imperial, ".3f"))

# Define the convert1 function
def convert1(weight):
    weight_kg = weight * .453592
    return weight_kg

# Define the convert2 function
def convert2(height):
    height_meters = height * .0254
    return height_meters


# Define the calculate2 function
def calculate2(weight_kg, height_meters):
    BMI_metric = (1.3 * weight_kg / height_meters ** 2.5)
    return BMI_metric

# Define the display_results2 function
def display_results2(BMI_metric):
    print("Your BMI is: ", format(BMI_metric, ".3f"))

main()
