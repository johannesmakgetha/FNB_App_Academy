name = "Python"
name[0] = 'f'
print(name[0])
print(name[-1])
print(name[2])

# Creating a email system generator

first_name = input("Enter your first name: ").strip().title()
last_name = input("Enter your last name: ").strip().title()

username = f"{first_name[0]}{last_name}"
print('Your username is: ',username)

print(f"Your email is: {username.lower()}@university.co.za")