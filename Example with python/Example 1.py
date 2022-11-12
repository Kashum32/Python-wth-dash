
'''
 Write a program to compute the Circumference and Area of a circle
 given its radius.

 Implement computation of circumference and Area as two seperate function.

 Circumference of a circle = 2 * Pi * r
 Area of a circle = Pi * r * r

  Hint: r - radius of the circle can be passed as an input perameter for the 
  function, and the function return the calculated values.
 '''

#  Circumference of a circle
def Circumference(r) :
    Pi = 3.14
    circumference = 2 * Pi * r
    print("Circumference of a circle = ",circumference)

Circumference(5) # r = 5, call to a function

# Answer :
    # Circumference of a circle =  31.400000000000002


# Area of a circle
def Area(r) :
    Pi = 3.14
    area = Pi * r * r
    print("Area of a circle = ",area)


Area(5) # r = 2, call to a function


# Answer :
   # Area of a circle =  78.5
