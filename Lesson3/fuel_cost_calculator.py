# The South African Fuel Cost Calculator
print("\n ~~ The South African Fuel Cost Calculator ~~ \n")

killo_m = float(input("How many kilometers are you driving?: ").strip())
petrol_price = float(input("How much is the current petrol price per liter?: ").strip())

print("\nThe car uses 1 liter of fuel for every 10 kilometers:")

liters_needed = killo_m / 10

total_cost = round(liters_needed * petrol_price,2)

print(f"\nThe cost of fuel needed for {killo_m}km is: R{total_cost}")
