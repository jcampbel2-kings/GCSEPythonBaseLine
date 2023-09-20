#James Campbell
#Sept 2022
#platnium 1

print("This program displays all the factors of a positive integer")
print("Enter a number greater than 1")
number=input(">")

#convert to integer
number=int(number)

isPrime=True

print("The factors of",number, "are...")

print(1)    # automatically a factor

#The loop starts from 2 and runs to half the actual number
#this is because the highest possible factor is half the actual number
for div in range(2,(number//2)+1):
    #check if number can be evenly divided by the div
    if number % div == 0:
        print(div)
        #number can no longer be prime
        isPrime=False
        
#end for
print(number)    # automatically a factor
#output whether the number is prime
if isPrime:
    print("The number",number,"is Prime")
else:
    print("The number",number,"is not Prime")
#endif