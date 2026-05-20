def tip_calculator() -> None:
    print("Welcome to the tip calculator!")
    total_bill = float(input("What was the total bill? "))
    tip = int(input("How much % of tip would you like to give? "))
    total_people = int(input("How many people to split the bill? "))
    splitted_amount = float((total_bill + (total_bill * tip / 100)) / total_people)
    print(f"Each people should pay: ${splitted_amount:.2f}")

tip_calculator()
