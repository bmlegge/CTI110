#Converting Feet to Inches Function
#4/18/2018
#CTI-110 P5T2_FeetToInches
#Bradley Legge

INCHES_PER_FOOT = 12

def main():
    feet = int(input('Enter a number of feet: '))
    
    print(feet, 'equals', feet_to_inches(feet), 'inches.')
                     

def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

main()
