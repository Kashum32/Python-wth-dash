
fname = " "
lname = " "
uname = " "
email = " "
password = " "
cpassword = " "
balanace = 0


details = {}
## Rgistration Deatails
def Registration():

    global fname
    global lname
    global uname
    global email
    global password
    global cpassword
    global balance

    print("############ REGISTRATION #############\n\n")
    print("\nEnter user first name : ")
    fname = input()
    print("\nEnter user last name : ")
    lname = input()
    print("\nEnter user name : ")
    uname = input()
    print("\nEnter user e-mail : ")
    email = input()
    print("\nEnter user password : ")
    password = input()
    print("\nEnter user confirm password : ")
    cpassword = input()
    print("\nEnter user balance : ")
    balance = int(input())

    

    if(password != cpassword):

       print("Invalid user confirm password ")
        
    else:
        
        print("\n\n\n$$$$$$ User Registration Successfully $$$$$$")
        print("\nFirst Name : ",fname)
        print("\nLast Name : ",lname)
        print("\nUsername : ",uname)
        print("\nPassword : ",password)
        print("\nConfirm Password : ",cpassword)
        print("\nBalance : ",balance)

        # add to the dictionary
        details['fname'] = fname
        details['lname'] = lname
        details['uname'] = uname
        details['password'] = password
        details['cpassword'] = cpassword
        details['balance'] = balance

        print(details)

        ## Login Details

        print("\n###### Login details #########\n\n")
        print("\nEnter user name : ")
        uname1 = input()
        print("\nUser Name : ",uname1)
        print("\nEnter user password : ")
        password1 = input()
        print("\npassword : ",password1)

        if(uname1 == details['uname']):
            if(password1 == details['password']):
                print("\n\nUser login successfully\n\n")
            else:
                print("\nInvalid password")
        else:
            print("\nInvalid username")

# deposit option
def Deposit(amount):
    global balance
    balance = balance + amount
    Balance()

# withdraw option
def Withdraw(amount):
    global balance
    balance = balance - amount
    Balance()


# checking Balance option
def Balance():
    print("\nCurrent Balance : ",balance)


def Online_Bank():
    while(True):

        print("Enter 1 for User Registration")
        print("Enter 2 for Deposit your money ")
        print("Enter 3 for Withdraw your money ")
        print("Enter 4 for Transfer your money ")
        

        print("\n\nChoose your choice : ")
        choice = input()

        if(choice == '1'):
            Registration()   
        elif(choice == '2'):
            balance1 = float(input("Enter balance to deposit : "))
            Deposit(balance1)
        elif(choice == '3'):
            balance1 = float(input("Enter balance to withdraw : "))
            Withdraw(balance1)


   
Online_Bank()



