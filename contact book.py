contact=[]
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts ={"name": name, "phone": phone,"email": email,"address": address}
    contact.append(contacts)
    print("Contact",name,"saved successfully..")
def view_contact():
    print("list of all contacts..")
    if len(contact)==0:
        print("contact book is empty.. please create new contact")
    j=1
    for i in contact:
        print(j,"name:",i['name'])
        print("  Phone:",i['phone'])
        j+=1
def search_contact():
    search=input("Enter contact name to search:")
    for i in contact:
        if search==i['name']:
            print("\nname:",i['name'],"\nPhone:",i['phone'],"\nemail:",i['email'],"\naddress:",i['address'])
            break
    else:
            print("contact not found..")
    if len(contact)==0:
        print("contact book is empty.. please create new contact")


def update_contact():
    k=input("Enter a contact name to upadate")
    
    for i in contact:
        if  i['name']==k:
            i['phone']=input("Enter new phone number:")
            i['email']=input("Enter new mail id:")
            i['address']=input("Enter new address:")
            print("contact",k,"updated succcessfully:")
            break
    else:
            print("contact not found ")
    if len(contact)==0:
        print("contact book is empty.. please create new contact")
            

def delete_contact():
    k=input("Enter a contact name to delete")
   
    for i in contact:
        if i['name']==k:
            contact.remove(i)
            print("contact deleted successfully")
            break
    else:
            print("contact not found")
            
def contact_book():
    while True:
        print('\n')
        print("Contact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option (1-6):")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book....")
            break
        else:
            print("Invalid option! Please try again")
contact_book()
        
    

