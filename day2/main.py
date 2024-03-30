print("Welcome to the tip calculator! \n")

total_bill = float(input("What was the total bill? $ \n"))

tip = int(input("How much tip would you like to give? 10%, 12%, or 15%? \n"))

people_number = int(input("How many people to split the bill? \n"))

total_bill_for_each_person = "{:.2f}".format(total_bill * (1 + tip / 100) / people_number)

print(f"Each person should pay: ${total_bill_for_each_person}")