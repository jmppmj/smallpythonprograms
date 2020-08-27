#///////////////////////////Purpose of Program///////////////////////////
#This program calculates letter grades and a final average letter grade for and from 5 integer test scores.
#Language: Python

def main ():
    #1 - Declare variables
    #2 - Prompt user for score
    #3 - Record score
    #4 - Return letter grade/score to user
    #5 - Go to step 2 until counter is 5
    score, counter, runtotal = get_score()

    #6 - Return average of all 5 test scores
    average = calc_average(runtotal, counter)
    score = average

    #7 - Return letter grade for average
    determine_grade(score)

    #8 - End program

def get_score():
    counter = 0
    runtotal = 0
    for i in range(5):
        score = int(input("Please enter a test score: "))
        counter += 1
        runtotal += score
        determine_grade(score)
    return score, counter, runtotal

def determine_grade(score):
    if score >= 90:
        print("an A")
    elif score >= 80 and score < 90:
        print ("a B")
    elif score >= 70 and score < 80:
        print ("a C")
    elif score >= 60 and score < 70:
        print ("a D")
    elif score <= 59:
        print ("a F")
    return

def calc_average(runtotal, counter):
    average = runtotal / counter
    print ("The average of your test scores is:", average)
    return average

main()
