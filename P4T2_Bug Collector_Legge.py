#CTI-110
#P4T2: Bug Collector
#Bradley Legge
#3/25/2018

total = 0

for day in range(1, 8):
    print("Enter the number of bugs collected on day", day, ": ")
    bugs = int(input())
    total = total + bugs

print("The total number of bugs collected for the 7 days is: ", total)
