# P5T1
# Kilometer Converter
# Bradley Legge
# 4/18/2018

def main():
    kilometers = float(input('Enter a distance in kilometers: '))
    show_miles(kilometers)

def show_miles(km):
    miles = km * .06214
    print(km, 'kilometers equals' , miles, 'miles.')

main()
