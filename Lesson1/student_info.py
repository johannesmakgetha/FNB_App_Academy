first_name = input("Enter your First Name: ")
surname = input("Enter your Surname: ")
age = int(input("Enter your age: "))
favourite_num = float(input("Enter your favourite number: "))

#Display
print("\n ~~ Display ~~ \n")
print(f"Welcome, {first_name}!")
print('First Name in UPPERCASE: ',first_name.upper())
print('First Name in Title format: ',first_name.title())
print(f"{age* 12} in months")
print('Favourite number in 2 decimal place: ', round(favourite_num,2))

#Data Types
print("\n ~~ Data types ~~ \n")
print('First Name type: ',type(first_name))
print('Surname type: ',type(surname))
print('Age type: ',type(age))
print('Favourite number type: ',type(favourite_num))
