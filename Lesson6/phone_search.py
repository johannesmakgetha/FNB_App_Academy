# The Phone Directory Search
print("\n~~ The Phone Directory Search ~~\n")

while True:

    contacts = [
        {'name':"Tb",
        "phone": "0821112222"},
        {'name':"J",
        "phone": "0821112222"},
        {'name':"LM",
        "phone": "0821112222"}

    ]

    # Search

    user_input = input("`Search`: name: ")
    found = False
    for i in contacts:
        if i['name'].lower() == user_input.lower():
            found = True
            print(f'Found! {user_input}’s number is {i['phone']}')
            
 
    if found == False:
        print('Contact not found.\n')

        again = False
        user_input2 = None
        while user_input2 is None:
            try:
                user_input2 = input("`Search again?` 'yes or no:' ")

                if user_input2.lower() not in ['yes','no','y','n']:
                    raise ValueError
                else:
                    if user_input2.lower() in ['yes','y']:
                        again = True
                        break
                    else:
                        break
            except ValueError:
                print("'Please Enter: yes or no'")
                user_input2 = None


        if again:
            continue
        else:
            break
    else:
        break