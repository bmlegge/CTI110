#CTI 110
#P3HW2: Software Sales
#Bradley Legge
#3/3/2018

def main():

    cost = 99
    quantity = int(input("How many copies do you wish to purchase? "))
    totalCost = cost * quantity

    if quantity >= 10 and quantity <= 19:
        discount = totalCost * .10
        print("The discounted amount is: $", discount)
        disCost = totalCost - discount
        print("The total cost is: $", disCost)
    elif quantity >= 20 and quantity <= 49:
        discount = totalCost * .20
        print("The discounted amount is: $", discount)
        disCost = totalCost - discount
        print("The total cost is: $", disCost)
    elif quantity >= 50 and quantity <= 99:
        discount = totalCost * .30
        print("The discounted amount is: $", discount)
        disCost = totalCost - discount
        print("The total cost is: $", disCost)
    elif quantity >= 100:
        discount = totalCost * .40
        print("The discounted amount is: $", discount)
        disCost = totalCost - discount
        print("The total cost is: $", disCost)
    else:
        print("There is no discounted price.")
        print("The total cost is : $", totalCost)


main()
