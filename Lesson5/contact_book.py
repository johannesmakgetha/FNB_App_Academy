contacts = []
action = 4

while action != 5:
    
    def add_contact():
        name = input("Enter Name: ")
        phone = None
        while phone is None:
            try:
                phone = input("Enter phone number: ")
                if phone.isnumeric():
                    phone = int(phone)
                else:
                    raise ValueError
            except ValueError:
                print('`Error:` Enter Phone Numbers')
                phone = None
        email = input("Enter email address: ")
        contact_details = {
        'name' : name,
        'phone' : phone,
        'email' : email}
        
        contacts.append(contact_details)

    def search_contact(name):
        for i in contacts:
            if i['name'] == name:
                print("\nContact details: ")
                print( f'''Name: {i['name']}
Phone Number: {i['phone']}
Email addres: {i['email']}\n''')
                
            
        return None
    def delete_contact(name):
        for i,j in enumerate(contacts):
            if j['name'] == name:
                contacts.pop(i)
                return '\n~ Contact deleted successfully ~'

    def view_all():
        
        print(f'~~      ALL CONTACTS\n        Total: {len(contacts)} \n~~\n')
        #print(f'Total: {len(contacts)}')
        for j,i in enumerate(contacts):
            print(j+1,f'''Name: {i['name']}
Phone Number: {i['phone']}
Email addres: {i['email']}\n''')





    print()
    
    try:
        action = input("choose an action (1=Add, 2=Search, 3=Delete, 4=View All, 5=Exit): ")
        if action not in '12345':
            raise ValueError
        
        action  = int(action)
    except ValueError:
        print("`Error:` Enter a number from 1 to 5:")


    if action == 1:
        add_contact()
    elif action == 2:
        search_contact(input("`Search`: Enter a name: "))
    elif action == 3:
        print(delete_contact(input("`Delete`: Enter a name: ")))
    elif action == 4:
        view_all()
    else:
        print('~ Exit ~')

    
