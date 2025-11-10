print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
tip_as_decimal = tip_percentage / 100
total_tip = total_bill * tip_as_decimal
total_bill_with_tip = total_bill + total_tip
bill_per_person = total_bill_with_tip / number_of_people
final_amount_per_person_integer = int(bill_per_person)
final_amount_per_person_rounded = round(bill_per_person, 2)
print(f"Each person should pay (integer): ${final_amount_per_person_integer}")
print(f"Each person should pay (rounded): ${final_amount_per_person_rounded}")
