#James Campbell
#Sept 2022
#gold 2

print("Enter an operator and then a number between 1 and 10")
ques=input(">")
#cut the input into the first character (the operator)
#and the rest of the input.  convert that to an integer
operator=ques[0]
number=int(ques[1:])

#create two strings,  one for title line and one to underline it
title =operator+" |"
line="-----"

#loop from 0 to the actual number entered (so + 1 required)
for n in range(number+1):
    title = title + " "+ str(n)
    line=line+"--"
#end for
print(title)
print(line)

#two loops required.  outer one for each line in the result table
#inner for the actual line itself
#loop from 0 to the actual number entered (so + 1 required)
# n is the row number
# m is the column number
for n in range(number+1):
    line= str(n) + " |"
    for m in range(number+1):
        #calc the output based on the operator requested
        if operator=="+":
            ans=n + m
        elif operator=="-":
            ans=n-m
        elif operator =="*":
            ans=n*m
        line=line+" "+str(ans)
    #end for
    print(line)
#end for