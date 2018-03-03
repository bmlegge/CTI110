#CTI-110
#P3HW1 - Age Classifier
#Bradley Legge
#3/3/2018

def main():
                 
    age = int(input("Enter a person's age: "))

    if age >= 0 and age <=1:  
        print("He or she is an infant")
    elif age > 1 and age < 13:
        print("He or she is a child.")
    elif age >= 13 and age < 20:
        print("He or she is a teenager.")
    elif age >= 20:
        print("He or she is an adult.")

main()
