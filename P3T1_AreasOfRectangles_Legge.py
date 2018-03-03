#CTI-110
#P3T1: Areas of Rectangles
#Bradley Legge
#3/3/2018

print("This program will compare the area of two rectangles")
 
recOneLength = float(input("Enter the length of rectangle one: "))
recOneWidth = float(input("Enter the width of rectangle one: "))
recOneArea = float(recOneLength * recOneWidth)

recTwoLength = float(input("Enter the length of rectangle two: "))
recTwoWidth = float(input("Enter the width of rectangle two: "))
recTwoArea = float(recTwoLength * recTwoWidth)

if recOneArea == recTwoArea:
    print("The rectangles have the same area.")
elif recOneArea > recTwoArea:
    print("Rectangle one has the greater area.")
elif recOneArea < recTwoArea:
    print("Rectangle two has the greater area.")

