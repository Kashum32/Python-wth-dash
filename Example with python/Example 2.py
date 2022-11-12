# if else statement 

# get a marks as a input from user 
marks = int(input("Enter user marks : "))

#using if else statement
if marks >= 75 : # Whether the condition is True or False
    print("This is a mark : ", marks, " and got a the A Grade")

elif (marks < 75) and (marks >= 65) :
    print("This is a mark : ", marks, " and got a the B Grade") 

elif (marks < 65) and (marks >= 55) :
    print("This is a mark : ", marks, " and got a the C Grade")

elif (marks < 55) and (marks >= 35) :
    print("This is a mark : ", marks, " and got a the D Grade")

else :
    print("This is a mark : ", marks, " and got a the F Grade")


## Out put : 

    # Enter user marks : 72
    # This is a mark :  72  and got a the B Grade

