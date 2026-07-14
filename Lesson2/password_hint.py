# The Secure Password Hint Tool

password = input("Enter a secret password: ").strip()

print(password)

print(f"Your password hint: It starts with {password[0].upper()} and ends with {password[-1].upper()}")