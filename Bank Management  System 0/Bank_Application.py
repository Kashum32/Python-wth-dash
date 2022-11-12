
Account_No = 0
Cus_Name = " "
BCode = " "
Mobile_No = 0
Bal = 0

def CreateAccount():

    global Account_No
    global Cus_Name
    global BCode
    global Mobile_No
    global Bal 


    Account_No = int(input("Enter account number : "))
    Cus_Name = input("Enter custemer name : ")
    BCode = input("Enter Branch code : ")
    Mobile_No = int(input("Enter mobile number : "))
    Bal = int(input("Enter current balance : "))

def ShowAcntDetails():
    print("Account Number : ",Account_No)
    print("Custemer Name : ",Cus_Name)
    print("Branch Code : ",BCode)
    print("Mobile Number : ", Mobile_No)

def Deposit(amount):
    global Bal
    Bal = Bal + amount
    CheckBalance()

def Withdraw(amount):
    global Bal
    Bal = Bal - amount
    CheckBalance()

def CheckBalance():
    print("\nCurrent Balance : ",Bal)


# main function

ch1 = 'y'
while(ch1 == 'y'):       
    print("1.Create Account \n 2.Withdraw \n 3.Deposit \n 4.Check Balance \n")
    ch = int(input("\nSelect any option : "))

    if(ch == 1):
        CreateAccount()
    elif (ch == 2):
        amt = int(input("Enter amount to withdraw : "))
        Withdraw(amt)
    elif (ch == 3):
        amt = int(input("Enter amount to deposit : "))
        Deposit(amt)
    elif (ch == 4):
        CheckBalance()
    else:
        print("please select any 4 option avilable above ")
    print("do you want to continue ")
    ch1 = input()   


