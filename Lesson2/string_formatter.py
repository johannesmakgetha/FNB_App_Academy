first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
bio_message = input("Enter a short bio: \n")

print("\n~~ String formatter ~~\n")
username = first_name[0].lower() + last_name.lower()
print('Full name: ',first_name.title())
print("bio: ",bio_message.strip())
print("number of characters in bio: ",len(bio_message))
edited_bio = bio_message.replace("I am","I'm")

print(edited_bio)
