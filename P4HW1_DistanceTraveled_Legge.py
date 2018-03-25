#CTI-110
#P4HW1: Distance Traveled
#Bradley Legge
#3/25/2018


count = 0
hours = 0
print("What is the speed of the vehicle in mph? ")
speed = int(input())
print("How many hours has it traveled? ")
time = int(input())

while count < time:
    hours = hours + 1
    distance = hours * speed
    print("Hour          Distance Traveled")
    print(hours,"            ", distance)
    count = count + 1
    
