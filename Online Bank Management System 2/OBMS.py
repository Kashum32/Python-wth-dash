import csv
import pandas

## registration form
def registration():
    print('\n#### User Registration #####\n\n')
    username = input('Enter user name : ')
    print('user name : ', username)
    email = input('Enter email : ')
    print('email : ',email)
    password = input('Enter password : ')
    print('password : ',password)
    cpassword = input('confirm password : ')
    if password == cpassword:
        print('confirm password : ',cpassword)
    else:
        print('Invalid password')

    print('\nUser Registration successfully...\n\n')

   
   ## store user details into the datasheet
    with open('user_registration.csv','a') as csv_file:
        fieldnames = ['username','email','password','cpassword']
        writer = csv.DictWriter(csv_file,fieldnames= fieldnames)

        writer.writerow({'username':username,'email':email,'password':password,'cpassword':cpassword})
    
        print('store user details successfully\n\n')

    # store details in the other file
    loan_df = pandas.read_csv('user_registration.csv',header = 0,
                            names=['username','email','password','cpassword'])
    loan_df.to_csv('print_user_registration.csv')
    
    # print other file
    print('\nprint registration details\n')
    with open('print_user_registration.csv', encoding='utf8') as csv_file:
        contacts = csv.DictReader(csv_file)
        for contact in contacts:
            print(contact['username'],contact['email'])

    # login form
    def login():
        print('\n##### User Login #####\n\n')
        username1 = input('Enter user name : ')
        if username == username1 :
            print('valid username')
            print('user name : ',username1)
            password1 = input('Enter user password ')
            if password == password1 :
                print('valid password')
                print('user password : ',password1)
            else:
                print('invalid password')
        else:
            print('invalid username')
        
        print('\nUser Login successfully..\n\n')
    login()


# for user registration
def user_registration():
    print('enter 1 for user registration')

    choice = input("choose your choice")
    return choice


number = user_registration()
print(number)

if number == '1':
    registration()

else:
    print('Invalid number ')



