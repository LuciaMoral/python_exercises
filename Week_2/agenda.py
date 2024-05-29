# 3. contact list: name, phone no and email. Search user info and display

def show_contacts(contact_list: dict):
        if len(contact_list) > 0:
            for contact, data in contact_list.items():
                print(contact, data)
                print(f"Contact: {contact}")
                print(f"Phone: {data[0]}")
                print(f"Email: {data[1]}")
        else:
            print("There are no contacts registered")

def search_contact(contact_list: dict):
     if len(contact_list) > 0:
          name = input("Enter name: ")
          found_contacts = 0
          for contact, data in contact_list.items():
               if name in contact:
                    print(f"Name: {contact}")
                    print(f"Phone: {data[0]}")
                    print(f"Email: {data[1]}")
                    found_contacts +=1
               if found_contacts == 0:
                print(f"this {contact} was not found.")
               else:
                 print(f"these {found_contacts} contacts were found")
     else:
        print("There are no contacts registered")

def add_contact(contact_list: dict):
        name = input("Enter name: ")
        if name in contact_list:
            print("this contact already exists")
        else:
            phone = int(input("Enter phone number: "))
            email = input("Enter email address: ")
            contact_list.setdefault(name, [phone, email])
            print("Contact added successfully")

while True:
    my_agenda = {}
    print("1. Show contacts")
    print("2. Search contact")
    print("3. Add contact")
    print("4. Exit")

    option = int(input("Select an option"))
    if option == 1:
        show_contacts(my_agenda)
    elif option == 2:
        search_contact(my_agenda)
    elif option == 3:
        add_contact(my_agenda)
    elif option == 4:
        print("Exiting...")
        break
