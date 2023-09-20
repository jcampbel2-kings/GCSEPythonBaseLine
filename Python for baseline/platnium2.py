#James Campbell
#Sept 2022
#platnium 2


#this subroutine checks if number is prime using same approach as plat 1
#returns true if it is
#this is for the extension only
def isPrime(n):
    #assume it is prime
    rval=True
    #loop from 2 until half the number being checked
    for div in range(2,(n//2)+1):
        #check if number is prime
        if n % div==0:
            rval=False
    
    return rval

print("This program plays FizzBuzz")
print("Enter a number between 1 and 1000")
print("The program will print out all the numbers from 1 to the entered number")
print("If the number is a multiple of 3 then it will say Fizz instead")
print("If the number is a multiple of 5 then it will say Bomb instead")
print("If the number is a multiple of 3 and 5 then it will say FizzBomb instead")

number=input(">")

#convert to integer
number=int(number)

#loop from 1 to the number entered
for n in range(1,number):
    #check if number prime
    #this part is only required for the extention
    if isPrime(n):
        print("OPPS!")
    #check if number can be evenly divided by the 3 and 5
    elif (n % 3 == 0) and (n % 5==0):
        print("FizzBomb")
    elif n % 3 == 0 :
        print("Fizz")
    elif n % 5 == 0:
        print("Bomb")
    else:
        print(n)
        
#end for

