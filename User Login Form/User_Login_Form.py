# User Registration
def Registration():

    file = open('file3.txt','a')

    print("\n\n###### User Registration Form ########\n\n")
    fname = input("enter first name : ")
    print('first name : ' + fname)

    lname = input("enter last name : ")
    print("last name : " + lname)

    username = input("enter user name : ")
    print("last name : " + username)

    email = input("enter user email : ")
    print("last name : " + email)

    password = input("enter user password : ")
    print("last name : " + password)
    file.write(fname + '\t' + lname + '\t' + username + '\t' + password + '\t' + email )
    file.write('\n')
# User Login
def Login() :
    file2 = open("file3.txt",'r')

   
    username1 = input("enter user name : ")
    print("user name : " + username1)
    password1 = input("enter user password : ")
    print("password : " + password1)
    f = file2.readlines()
    # add the details to list
    for data in f :
        d = data.split('\t')
        print(d,end='')
    print('\n')
    print(d[2])

    if d[2] == username1 :
        if d[3] == password1:
            print('Login successfully')
        else:
            print('invalid password')
    else:
        print('invalid username')
   
  

while(True) :
    print("\n\nEnter 1 for user Registration ")
    print("Enter 2 for user Login ")
    
    choice = int(input("\n\nEnter your choice : "))

    if (choice == 1) :
       Registration() 
    elif (choice == 2):
        Login()
    

