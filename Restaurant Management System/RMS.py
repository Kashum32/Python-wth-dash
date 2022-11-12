
########## RESTAURANT MANAGEMENT SYSTEM ##########




# for admin
admin = {}

admin['password1'] = ''

# admin registration
def Registration() :
    print('#### Admin Registration Details #####\n\n')
    admin['fname'] = input('Enter first name : ')
    print('first name : ', admin['fname'])
    admin['lname'] = input('Enter last name : ')
    print('last name : ', admin['lname'])
    admin['username'] = input('Enter username : ')
    print('user name : ', admin['username'])
    admin['password'] = input('Enter password : ')
    print('password : ', admin['password'])
    admin['cpassword'] = input('Enter confirm password : ')
    print('confirm password : ', admin['cpassword'])
    print('\n###### Registration is very successfully ######\n')

    # admin login
    def Login() :
        print("#### Admin Login Details ######\n\n")

        username = input('Enter user name : ')
        if admin['username'] == username :
            print('user name : ',  admin['username'])
            print('username is correct')
            password = input('Enter password : ')

            admin['password1'] = password

            if admin['password'] == password :
                print('password : ', admin['password'])
                print('password is correct')
            else:
                print('password is incorrect')
        else:
            print('username is incorrect')

        print('\n###### Login is very successfully ######\n\n')

    Login()






# Login addmin
def Login_addmin():
    print('press the "admin" for admin registration')

    admin = input('Who are you at the restaurant?')

    if 'admin' == admin :
        Registration()
    else :
        print('you are not admin at the restaurant')

Login_addmin()


# Other management options

if admin['password1'] == admin['password1'] :
    
    while True:

        print('press 1 for staff managment')
        print('press 2 for stock control')
        print('press 3 for transation')
        print('press 4 for reservation')
        print('press 5 for table managment')
        print('press 6 for menu management')

        number = input('\nEnter task option : ')

        if number == '1' :
            def  staff_managment():
                print()
            staff_managment()
        elif number == '2' :
            def stock_control() :
                print()
            stock_control()

        elif number == '3' :
            def transation() :
                print()
            transation()

        elif number == '4' :
            def reservation() :
                print()
            reservation()

        elif number == '5' :
            def table_reservation() :
                print()
            table_reservation()

        elif number == '6' :
            def menu_managment() :
                print()
            menu_managment()

        else :
            print('do not included your task option\n')

    
else :
    print("sorry, you are not admin\n")



