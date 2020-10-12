#///////////////////////////Purpose of Program///////////////////////////
#This program calculates a users BMI.
#Language: Python

from enum import Enum

class Unit(Enum):
    Imperial = 1
    Metric = 2

def main():
    weight = input_float("Enter your weight in pounds: ")
    height = input_float("Enter your height in inches: ")
    bmi = bmi_formula(weight, height, Unit.Imperial)
    display_bmi(bmi)

    # Convert from imperial to metric units
    weight = lb_to_kg(weight)
    height = in_to_m(height)
    bmi = bmi_formula(weight, height, Unit.Metric)
    display_bmi(bmi)

    return

def input_float(query):
    return float(input(query))

def display_bmi(bmi, method):
    print("Your BMI is:", format(bmi, ".3f"), "kg/m^2")

def bmi_formula(weight, height, unit):
    if unit == Unit.Imperial:
        return 5734 * weight / height ** 2.5
    if unit == Unit.Metric:
        return 1.3 * weight / height ** 2.5

# Note: This website has a different formula for BMI calculation.
#       Perhaps it is more (or less) accurate? 
#       It yield different results from the original formula.
#       https://www.thecalculatorsite.com/articles/health/bmi-formula-for-bmi-calculations.php
#
def bmi_formula_Alastair_Hazell(weight, height, unit):
    if unit == Unit.Imperial:
        return 703 * weight / height ** 2
    if unit == Unit.Metric:
        return weight / height ** 2

def lb_to_kg(pounds):
    return pounds * .453592

def in_to_m(inches):
    return inches * .0254

main()
