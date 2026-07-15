num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n~~ Multi-Function Calculator ~~\n")

# four basic arithmetic operations



addition = round(num1 + num2,2)
substraction = round(num1 - num2,2)
multiplication = round(num1 * num2,2)
error = False
error_message = "'Error: The second number cannot be zero'"
try:
	division = round(num1 / num2,2)
	floor_division = num1 // num2
	modulus = num1 % num2
except ZeroDivisionError :
	error = True
	print(error_message)
finally:
	if error == True:
		division = error_message
		floor_division = error_message
		modulus = error_message


pr2 = f"\nAdvanced operations"




print(f"""four basic arithmetic operations: 
Addition: {addition}
Subtraction: {substraction}
Multiplication: {multiplication}
Division: {division}

Advanced operations:
Floor Division: {floor_division}
Modulus: {modulus}""")
