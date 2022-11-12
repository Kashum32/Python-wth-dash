dic = {}
dic['balance'] = 20000.500
dic['totdeposit'] = 0
dic['totwithdraw'] = 0

def Registration():
    print('#### User Registration #####\n\n')
    
    dic['username'] = input("Enter user name : ")
    print('Username : ', dic['username'])
    dic['email'] = input('Enter user email : ')
    print('Email : ',dic['email'])
    dic['password'] = input('Enter user password : ')
    print('Password : ', dic['password'])
    dic['cpassword'] = input('Enter confirm password : ')
    print('Confirm Password : ', dic['cpassword'])
    
    print('\n\n####### User Login Details ######\n\n')
    def login():
        
        username = input('Enter user name : ')    
        if dic['username'] == username:
            print('correct username\n')
            dic['password1'] = input('Enter user password : ')
            if dic['password'] == dic['password1']:
                print('correct password\n')    
                print('login details successfully\n\n')
                
                
                
            else:
                print('invalid password\n')
        else:
            print('invalid username\n')
            
    login()
    
    while True:
        print('Enter 1 number for balance option')
        print('Enter 2 number for deposit option')
        print('Enter 3 number for withdraw option')
        print('Enter 4 number for Exit option\n')
        choice = input('Enter user number : ')
        
        if choice == '1' :

            if dic['password'] == dic['password1']:
                def Balance():
                    print('current balance is : ', float(dic['balance']))
                Balance()
            else:
                print('password is not equel \n')

        elif choice == '2':
            dic['dpt_balance'] = float(input('balance of deposit : '))
            if dic['password'] == dic['password1']:
                dic['balance'] = dic['balance'] + dic['dpt_balance']
                print('current balance : ', dic['balance'])
                print('deposit balnce : ', dic['dpt_balance'])

                # total deposit
                dic['totdeposit'] = dic['totdeposit'] + dic['dpt_balance']
                print('currently total deposit balance : ', dic['totdeposit'])

                print("### your deposit is successfully###\n\n")
            
            else:
                print('incorrect password')


        elif choice == '3':

            simcard = input('choose a mobile sim : ')
            if simcard == 'dialog':
                print('simcard is : ', simcard)
            elif simcard == 'hutch':
                print('simcard is : ', simcard)
            elif simcard == 'mobitel':
                print('simcard is : ', simcard)
            elif simcard == 'airtel':
                print('simcard is : ', simcard)
            else :
                print('Invalid simcard\n')

            mobile_no = int(input('Mobile Number : '))
            if mobile_no == '':
                print('please enter your mobile number')
            else :
                print('mobile number : ',mobile_no)

            dic['withbalance'] = float(input('balance of withdraw : '))
            if dic['password'] == dic['password1']:
                dic['balance'] = dic['balance'] - dic['withbalance'] 
                print('\ncurrent balance : ', dic['balance'])
                print('withdraw balnce : ', dic['withbalance'])

                # total withdraw
                dic['totwithdraw'] = dic['totwithdraw'] + dic['withbalance']
                print('currently total withdraw balance : ', dic['totwithdraw'])

                print("\n### your withdrwal is successfully###\n\n")
                
                # store the details
                simcard1 = simcard
                mobile_no1 = mobile_no
                with_balance = dic['withbalance']


                file = open('print_details.txt','a')
                file.write("\n\nWithdrawal its successfully\n\n")
                file.write('Sim Card - ' + str(simcard1) + '\n' + 'Mobile Number - ' + str(mobile_no1) + '\n' + 'Withdrwal Balance - ' + str(with_balance) + '\n\n')
                print("print is the successfully")
                print('Sim Card - ' + str(simcard1) + '\n' + 'Mobile Number - ' + str(mobile_no1) + '\n' + 'Withdrwal Balance - ' + str(with_balance))
            
            else:
                print('incorrect password')
        else:
            print('invalid number')


# Online Banking system
def main():
    print('enter 1 for user registration and login ')
    
    choice = input('Enter user choice ')
    if(choice == '1'):
        Registration()   
    else:
         print('invalid option')
            
       
        
main()





